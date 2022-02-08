from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class ProductsPage(PageObject):
    url_products = 'https://www.saucedemo.com/inventory.html'
    class_title_page = 'title'
    txt_products_title = 'PRODUCTS'
    class_products_list = 'inventory_list'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_products_url(self):
        return self.driver.current_url == self.url_products

    def has_products_title(self):
        products_title = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return products_title == self.txt_products_title

    def has_product_list(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.class_products_list)
            return True
        except NoSuchElementException:
            return False