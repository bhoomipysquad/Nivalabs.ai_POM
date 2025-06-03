import time
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Tests.conftest import Base_url


class Blog(BasePage):
    view_all = (By.XPATH , "//button[normalize-space()='View All']")
    logo = (By.XPATH , "//a[@class='navbar-brand']")
    blog_links = (By.CSS_SELECTOR, "a[href^='/blogs/']")

    def blog(self):
        self.scroll_down_only()
        self.click(*self.view_all)
        blog_url = f"{Base_url}blogs"
        if self.driver.current_url != blog_url:
            self.driver.save_screenshot("failed_blog_url.png")
            assert False, f"Blog page URL mismatch. Expected: {blog_url}, Found: {self.driver.current_url}"
        time.sleep(2)
        self.scroll_blogs_page()
        self.scroll_up_only()

        for i in range(2):
            blog_links = self.driver.find_elements(*self.blog_links)
            blog = blog_links[i]
            blog_url = blog.get_attribute("href")
            blog.click()
            self.scroll_up_down()
            # print(self.driver.current_url)
            # print(blog_url)
            if self.driver.current_url != blog_url:
                self.driver.save_screenshot("failed_to_open_Blog.png")
                assert False, f"Failed to open blog. Expected URL: {blog_url}, Actual URL: {self.driver.current_url}"
            self.driver.back()
            time.sleep(2)

        self.click(*self.logo)



        #to open particular blog(static code) :-
        # blogs = [
        #     {
        #         "title": "Pandas Profiling: Automated Data Insights in Python",
        #         "url": "https://www.nivalabs.ai/blogs/pandas-profiling-automated-data-insights-in-python"
        #     },
        #     {
        #         "title": "AI Agent in a Nutshell: Quick Implementation with Python",
        #         "url": "https://www.nivalabs.ai/blogs/ai-agent-in-a-nutshell-quick-implementation-with-p"
        #     }
        # ]
        # for blog in blogs:
        #     self.click(By.XPATH, f"//a[contains(text(),'{blog['title']}')]")
        #     self.scroll_up_down()
        #     assert self.driver.current_url == blog["url"]
        #     self.driver.back()

