import json
import base64


class Utils(object):
    @staticmethod
    def convert_audio_base64(audio_path: str) -> str:
        """將音頻文件轉換為 Base64 字符串"""
        with open(audio_path, "rb") as audio_file:
            audio_data = audio_file.read()
            return base64.b64encode(audio_data).decode("utf-8")

    @staticmethod
    def convert_sec_to_min(sec: float) -> str:
        """將秒數轉換為分鐘和秒的格式"""
        minutes = int(sec // 60)
        secs = sec % 60
        return f"{minutes}:{secs:.2f}"

    @staticmethod
    def format_interval(t):
        m = int(t // 60)
        s = int(t % 60)
        return f"{m:02}:{s:02}"

    @staticmethod
    def extract_json_from_markdown(text_string: str) -> dict:
        """
        從包含Markdown JSON代碼塊的字符串中抽取並解析JSON內容。

        這個函數會尋找字符串中第一個 '```json' 和 '```' 之間的內容，
        並嘗試將其解析為一個Python字典。

        Args:
            text_string (str): 包含JSON代碼塊的輸入字符串。

        Returns:
            dict: 解析後的JSON內容。

        Raises:
            ValueError: 如果在字符串中找不到有效的JSON代碼塊標籤。
            json.JSONDecodeError: 如果找到的內容不是有效的JSON格式。
        """
        json_start_tag = "```json"
        json_end_tag = "```"

        start_index = text_string.find(json_start_tag)
        if start_index == -1:
            raise ValueError("在字符串中找不到 '```json' 標籤。")

        # Move past the opening tag
        start_index += len(json_start_tag)

        end_index = text_string.find(json_end_tag, start_index)
        if end_index == -1:
            raise ValueError("在字符串中找不到 '```' 結束標籤。")

        json_content_string = text_string[start_index:end_index].strip()

        if not json_content_string:
            raise ValueError("在 '```json' 和 '```' 標籤之間沒有找到內容。")

        try:
            parsed_data = json.loads(json_content_string)
            return parsed_data
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"解析JSON內容時出錯: {e}", e.doc, e.pos)

    @staticmethod
    def extract_json_from_text(text_string: str) -> dict:
        text_string_list = text_string.split("\n")
        for index, line in enumerate(text_string_list):
            if line.strip() == "```json":
                json_lines = []
                for next_line in text_string_list[index + 1 :]:
                    if next_line.strip() == "```":
                        break
                    json_lines.append(next_line)
                json_content = "\n".join(json_lines)
                return json_content
        raise ValueError("No JSON code block found in the text.")


utils = Utils()
