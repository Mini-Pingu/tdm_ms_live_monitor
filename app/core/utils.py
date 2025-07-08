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


utils = Utils()
