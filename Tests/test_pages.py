from Pages.blog_page import Blog
from Pages.book_call import Book_Call
from Pages.check_responsive import Responsiveness
from Pages.home_page import Home_page
from Pages.hover_event import Hover_Check
from Tests.conftest import Base_url


def test_conf_test1(open_url):
    driver = open_url
    act_url = driver.current_url
    if act_url == Base_url:
        assert True
        driver.close()
    else:
        driver.save_screenshot("Base_url_issue.png")
        assert False


def test_blog_page(open_url):
    driver = open_url
    blog = Blog(driver)
    blog.blog()


def test_book_a_call(open_url):
    driver = open_url
    book_call = Book_Call(driver)
    book_call.book_call()


def test_home_page(open_url):
    driver = open_url
    home = Home_page(driver)
    home.check_page_up_button()
    home.check_logo()


def test_hover_event(open_url):
    driver = open_url
    hover = Hover_Check(driver)
    hover.solutions_url()
    hover.hover_over_menu()
    hover.open_social_media_pages()


def test_responsiveness(open_url):
    driver = open_url
    respo = Responsiveness(driver)
    respo.test_responsiveness_on_multiple_devices()