from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_browser(headless=False):
    """配置并启动Chrome浏览器"""
    # 创建Chrome选项
    chrome_options = Options()

    # 必要参数（解决Linux环境常见问题）
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 可选参数
    if headless:
        chrome_options.add_argument("--headless=new")  # 新版无头模式

    try:
        # 自动安装匹配的ChromeDriver
        service = Service(ChromeDriverManager().install())

        # 启动浏览器
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Chrome 启动成功！")
        return driver
    except Exception as e:
        print(f"浏览器启动失败: {str(e)}")
        print("解决方案:")
        print("1. 检查Chrome是否安装: google-chrome --version")
        print("2. 确保有网络连接")
        print("3. 尝试手动下载驱动: https://chromedriver.chromium.org/downloads")
        raise


# 使用示例
if __name__ == "__main__":
    # 启动浏览器（False表示显示浏览器窗口）
    browser = setup_browser(headless=False)

    # 访问网页
    browser.get("https://www.baidu.com")

    # 打印页面标题
    print("页面标题:", browser.title)

    # 保持浏览器打开10秒（方便观察）
    print("浏览器将在10秒后关闭...")
    time.sleep(10)

    # 关闭浏览器
    browser.quit()
    print("浏览器已关闭")
