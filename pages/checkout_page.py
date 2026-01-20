from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '[id="checkout"]'
    FIRST_NAME_SELECTOR = '#first-name'
    POSTAL_CODE_SELECTOR = '#postal-code'
    LAST_NAME_SELECTOR = '#last-name'
    CONTINUE_CHECKOUT_SELECTOR = '#continue'
    FINISH_CHECKOUT_SELECTOR = '#finish'
    BURGER_MENU_SELECTOR = '#react-burger-menu-btn'
    LOGOUT_SIDEBAR_SELECTOR = '#logout_sidebar_link'

    def __init__(self, page):
        super().__init__(page)  # чтобы при создании экземпляра логин пейдж изнутри тест у нас автоматически вызвался конструктор из бейспедж и мы получили доступ к эндпоинду
        self._endpoint = '/ckeckout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)

    def continue_checkout(self):
        self.wait_for_selector_and_click(self.CONTINUE_CHECKOUT_SELECTOR)

    def finish_checkout(self):
        self.wait_for_selector_and_click(self.FINISH_CHECKOUT_SELECTOR)

    def start_logout_from_burger_menu(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)

    def start_logout_from_sidebar_link(self):
        self.wait_for_selector_and_click(self.LOGOUT_SIDEBAR_SELECTOR)







