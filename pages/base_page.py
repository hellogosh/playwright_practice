from playwright.sync_api import expect

class BasePage:
    __BASE_URL = 'https://www.saucedemo.com/'

    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _get_full_url(self): #метод сборщик полного урла
        if self._endpoint:
            return f'{self.__BASE_URL}/{self._endpoint}'
        return self.__BASE_URL

    def navigate_to(self):  #метод перехода на поный урл и проверки
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector):  #метод ждет селектор и кликает по нему
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector, value):  #метод ждет селектор и заполняет текст
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def wait_for_selector_and_type(self, selector, value, delay):  #метод ждет селектор и набирает текст
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    def assert_element_is_visible(self, selector): #метод проверит виден ли элемент на странице
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text): #метод проверит отображается ли текст на странице
        expect(self.page.locator("body")).to_contain_text()

    def assert_text_in_element(self, selector, text): #метод проверит
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector, expected_value): #метод проверит
        expect(self.page.locator(selector)).to_have_value(expected_value)

