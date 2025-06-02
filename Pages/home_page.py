from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Tests.conftest import Base_url


class Home_page(BasePage):
    page_up_button  = (By.XPATH ,"//*[name()='path' and contains(@stroke,'currentCol')]")
    nivalabs_logo = (By.XPATH , "//a[@class='navbar-brand']")
    view_all = (By.XPATH , "//button[normalize-space()='View All']")

    def check_page_up_button(self):
        self.scroll_down_only()
        instagram = self.driver.find_element(By.XPATH, "//a[contains(@aria-label,'Instagram')]//*[name()='svg']")
        assert instagram.is_displayed() or self.driver.save_screenshot("failed_page_up_button.png")
        self.click(*self.page_up_button)

    def check_logo(self):
        self.scroll_down_only()
        self.click(*self.view_all)
        blog_url = self.driver.current_url
        self.click(*self.nivalabs_logo)
        logo = self.driver.current_url
        assert blog_url != logo  and  logo == Base_url or self.driver.save_screenshot("failed_logo.png")
