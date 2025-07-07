class Config:
    """
    Configuration class for the application.
    """

    # wild_box related
    wild_box_base_url = "https://www.macaudb.com/api/news"
    api_name = "saveNews"
    api_id = "news"
    api_secret = "ad23e510f94ad15c1338b2328a50023fcbf0a1889c53488a98c785d6dd67fa3a"
    wild_box_url = (
        f"{wild_box_base_url}?apiName={api_name}&appId={api_id}&appSecret={api_secret}"
    )
