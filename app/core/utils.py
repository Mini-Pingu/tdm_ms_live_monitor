import base64
from pathlib import Path


class Utils(object):
    @staticmethod
    def convert_audio_base64(audio_path: str) -> str:
        """將音頻文件轉換為 Base64 字符串"""
        with open(audio_path, "rb") as audio_file:
            audio_data = audio_file.read()
            return base64.b64encode(audio_data).decode("utf-8")
