from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.locators = {
            "О нас": "header nav a:has-text(\"О нас\")",
            "Услуги": "header nav a:has-text(\"Услуги\")",
            "Проекты": "header nav a:has-text(\"Проекты\")",
            "Контакты": "header nav a:has-text(\"Контакты\")",
            "Отзывы": "header nav a:has-text(\"Отзывы\")",
        }

    def goto(self):
        self.page.goto(self.base_url)

    def click_nav(self, name: str):
        selector = self.locators[name]
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def get_current_url(self):
        return self.page.url
