class Spider(object):
    def __init__(self, name, url, headers=None, cookies=None, params=None, data=None):
        self.name = name
        self.url = url
        self.headers = headers if headers is not None else {}
        self.cookies = cookies if cookies is not None else {}
        self.params = params if params is not None else {}
        self.data = data if data is not None else {}

    def __repr__(self):
        return f"Spider(name={self.name}, url={self.url})"
