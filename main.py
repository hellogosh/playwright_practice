from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=500)
page = browser.new_page()
page.goto('https://www.saucedemo.com/')

page.type(selector='[id="user-name"]', text='standard_user', delay=100)
page.fill(selector='#password', value='secret_sauce')
page.click(selector='.submit-button')

page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
page.wait_for_selector('#inventory_container')
page.is_visible(selector='[data-test="add-to-cart-sauce-labs-backpack"]')
page.is_enabled(selector='[data-test="add-to-cart-sauce-labs-backpack"]')
page.click(selector='[data-test="add-to-cart-sauce-labs-backpack"]')

time.sleep(2)

browser.close()
playwright.stop()
