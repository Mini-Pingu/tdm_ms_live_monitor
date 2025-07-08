class Config:
    """
    Configuration class for the application.
    """

    # General settings
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    max_min_per_section = 30
    temp_folder = "./temp"
    temp_mp3 = "temp.mp3"

    # tdm related
    # tdm_live_program_url = "https://www.tdm.com.mo/api/v1.0/live/3/playlist"
    tdm_online_feed_url = "https://live3.tdm.com.mo/live/rch2.live/playlist.m3u8"
    tdm_live_chunk_list_base_url = "https://live5.tdm.com.mo/live/rch2.live"
    tdm_live_audio_base_url = "https://live5.tdm.com.mo/live/rch2.live"

    # ASR related
    whisper_model_version = "large-v2"
    initial_prompt = "這是澳門的一個電臺節目文本內容，一定要有標點符號。大家好，歡迎收聽澳門講場。早安，感謝邀請我來參加節目。今天我們將討論澳門的最新發展，請嘉賓分享一下看法。好的，非常樂意。最近澳門的經濟發展非常迅速。一定要有標點符號。"
    whisper_word_timestamps = True
    whisper_temperature = 0.0
    whisper_temperature_increment_on_fallback = None

    # LLM related
    llm_api_key = "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"
    llm_model = "sonar-reasoning-pro"

    # wild box related
    wild_box_base_url = "https://www.macaudb.com/api/news"
    api_name = "saveNews"
    api_id = "news"
    api_secret = "ad23e510f94ad15c1338b2328a50023fcbf0a1889c53488a98c785d6dd67fa3a"
    wild_box_url = (
        f"{wild_box_base_url}?apiName={api_name}&appId={api_id}&appSecret={api_secret}"
    )


config = Config()
