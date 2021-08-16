import pytest
from selenium import webdriver
import time

def test_browser_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Кнопка добавления товара в корзину не найдена" 
    time.sleep(10)