from playwright.sync_api import sync_playwright, expect

class BasePage:
    __BASE_URL = 'https://www.saucedemo.com/'

    def __init__(self, page):
        self.page = page
        self._endpoint = ''
