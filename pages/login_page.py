from pages.base_page import BasePage


class LoginPage(BasePage): #созд класс логинпейдж, который наследуется от бейспейдж
    def __init__(self, page):
        super().__init__(page) #чтобы при создании экземпляра логин пейдж изнутри тест у нас автоматически вызвался конструктор из бейспедж и мы получили доступ к эндпоинду
        self._endpoint = ''

    USERNAME_SELECTOR = '#user-name'
    PASSWORD_SELECTOR = '#password'
    LOGIN_BUTTON_SELECTOR = '#login-button'

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.page.wait_for_url('**/inventory.html')