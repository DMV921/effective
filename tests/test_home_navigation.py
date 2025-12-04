import pytest
from pages.home_page import HomePage
import allure

@pytest.mark.ui
def test_navigation_links(page, base_url):
    home = HomePage(page, base_url)
    home.goto()
    checks = [
        ("О нас", "about"),
        ("Услуги", "services"),
        ("Проекты", "projects"),
        ("Контакты", "contacts"),
        ("Отзывы", "reviews"),
    ]
    for name, expected in checks:
        with allure.step(f"Кликаем по '{name}'"):
            home.goto()
            home.click_nav(name)
            assert expected in home.get_current_url()
