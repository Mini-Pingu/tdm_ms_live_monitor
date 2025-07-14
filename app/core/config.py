import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for the application.
    """

    # General settings
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    max_min_per_section = 30
    temp_file_extension = "aac"
    temp_folder = "./temp"
    temp_wav = "temp.wav"
    source = "MS"

    # tdm related
    # tdm_live_program_url = "https://www.tdm.com.mo/api/v1.0/live/3/playlist"
    tdm_online_feed_url = "https://live3.tdm.com.mo/live/rch2.live/playlist.m3u8"
    tdm_live_chunk_list_base_url = "https://live5.tdm.com.mo/live/rch2.live"
    tdm_live_audio_base_url = "https://live5.tdm.com.mo/live/rch2.live"

    # ASR related
    # ToDo: 要處理的問題：whisper 模型的版本和語言模型的版本不一致，會導致語音識別結果不準確。
    whisper_model_version = "large-v2"
    initial_prompt = "這是澳門電臺節目轉文字內容，需包含完整標點符號。請注意澳門方言與專有名詞。範例：『大家好，歡迎收聽澳門講場。早安，感謝邀請我來參加節目。』"
    whisper_word_timestamps = True
    whisper_temperature = 0.0
    whisper_temperature_increment_on_fallback = None
    whisper_beam_size = 5
    whisper_best_of = 5

    interval = 120
    sentence_format_model = "sonar"
    sentence_format_prompt = "以上內容，給我更新最合適的標點符號，並且其中內容中有關類似澳門地方名稱的和澳門政府部門與單位都給我更改爲正確的，其他的文字內容一定要不變。只需要提供想要的文字就可以，其他除了修改後的文字都不要（譬如解釋，註釋等）。因爲我要直接用於結構化數據分析。"

    # LLM related
    llm_api_key = "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"
    llm_model = "sonar-reasoning-pro"
    llm_prompt = '這是只關注澳門地方消息的澳門電臺澳門講場的語音識別內容，我只要分析這段內容，給我以上內容分析後的標題，以上內容分析後的總結（總結只要列最多五點說明，並且總字數要 1000字 以上，每一點中要有對該點字數不少於 300字 的單點分析，並且每點開頭要有（一），（二），（三）之類的列點），和主題點分析（要有5點以上，要有标题和 70到100字之間的句子段落的解释）。總結和主題點分析出來的內容不要有太多專業術語，因爲用戶是普通市民。並且分析出來的內容來源最好主要依賴上傳的文本。並且結合聯網功能搜索出來的內容比例最多 30% 。全部內容文字中不要出現搜索來源等的提示。最後分析出來的內容要給我結構化輸出：{title: "", sumarization: "", subjects: [{title: "", content: ""}]}， 其中 title 是標題（類型是字符串），sumarization 是總結（類型是字符串），subjects 是主題點分析（類型是數組）。'
    llm_text_format_model = "sonar"
    llm_text_format_prompt = '將以上文本內容抽取 ```json 和 ``` 之間的內容，並且轉換爲結構化的 JSON 格式，格式如下：{title: "", sumarization: "", subjects: [{title: "", content: ""}]}, 我要用於結構化數據分析。 '

    # wild box related
    wild_box_base_url = "https://www.macaudb.com/api/news"
    api_name = "saveNews"
    api_id = "news"
    api_secret = "ad23e510f94ad15c1338b2328a50023fcbf0a1889c53488a98c785d6dd67fa3a"
    wild_box_url = (
        f"{wild_box_base_url}?apiName={api_name}&appId={api_id}&appSecret={api_secret}"
    )


config = Config()
