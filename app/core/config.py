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

    # tdm related
    # tdm_live_program_url = "https://www.tdm.com.mo/api/v1.0/live/3/playlist"
    tdm_online_feed_url = "https://live3.tdm.com.mo/live/rch2.live/playlist.m3u8"
    tdm_live_chunk_list_base_url = "https://live5.tdm.com.mo/live/rch2.live"
    tdm_live_audio_base_url = "https://live5.tdm.com.mo/live/rch2.live"

    # ASR related
    whisper_model_version = "large-v2"
    # initial_prompt = "這是澳門的一個電臺節目文本內容，一定要有標點符號。大家好，歡迎收聽澳門講場。早安，感謝邀請我來參加節目。今天我們將討論澳門的最新發展，請嘉賓分享一下看法。好的，非常樂意。最近澳門的經濟發展非常迅速。一定要有標點符號。"
    initial_prompt = "這是澳門電臺節目轉文字內容，需包含完整標點符號。請注意澳門方言與專有名詞。範例：『大家好，歡迎收聽澳門講場。早安，感謝邀請我來參加節目。』"
    whisper_word_timestamps = True
    whisper_temperature = 0.0
    whisper_temperature_increment_on_fallback = None
    whisper_beam_size = 5
    whisper_best_of = 5

    # LLM related
    llm_api_key = "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"
    llm_model = "sonar-reasoning-pro"
    llm_prompt = '這是只關注澳門地方消息的澳門電臺澳門講場的語音識別內容，我只要分析這段內容，給我以上內容分析後的標題，以上內容分析厚的總結（總結要列點說明，並且字數要 1000字以上，列點方式以 （一），（二），（三）中文大寫字爲一點，每一點中要有對該點字數不少於 300字 的單點分析），和主題點分析（要有5點以上，要有标题和 30到50字之間的句子段落的解释）。總結和主題點分析出來的內容不要有太多專業術語，因爲用戶是普通市民。並且分析出來的內容來源最好主要依賴上傳的文本。並且結合聯網功能搜索出來的內容比例最多 30% 。全部內容文字中不要出現搜索來源等的提示。最後分析出來的內容要給我結構化輸出：{title: "", summarization: [{title：""， content: ""}], subjects: [{title: "", content: ""}]}'
    llm_text_format_model = "sonar"
    llm_text_format_prompt = '將以上文本內容抽取 ```json 和 ``` 之間的內容，並且轉換爲結構化的 JSON 格式，格式如下：{title: "", summarization: [{title：""， content: ""}], subjects: [{title: "", content: ""}]}, 我要用於結構化數據分析。 '

    # wild box related
    wild_box_base_url = "https://www.macaudb.com/api/news"
    api_name = "saveNews"
    api_id = "news"
    api_secret = "ad23e510f94ad15c1338b2328a50023fcbf0a1889c53488a98c785d6dd67fa3a"
    wild_box_url = (
        f"{wild_box_base_url}?apiName={api_name}&appId={api_id}&appSecret={api_secret}"
    )


config = Config()
