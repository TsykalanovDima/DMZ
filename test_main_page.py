from page.main_page import MainPage
from data.data import BaseData

# def test_demo():
#     driver = webdriver.Chrome()
#     driver.get('https://youtube.com')
#     assert driver.title == 'YouTube', f'Error: Title must be {driver.title}'

# def test_demo_test():
#     driver = webdriver.Chrome()
#     driver.get('https://youtube.com')
#     print(driver.get_credentials)
#     assert 'youtube.com' in driver.current_url

def test_open_garage(browser):
    mp = MainPage(browser, 'https://qauto.forstudy.space/')
    # mp.open()
    # mp.auth_form(BaseData.baseLogin, BaseData.basePassword)
    mp.auth_by_url(BaseData.baseLogin, BaseData.basePassword, BaseData.host)
    mp.BUTTON()
    mp.add()
    mp.add_car1()
    mp.mlg_1()
    mp.lastbut()
    assert mp.is_url_changed('https://guest:welcome2qauto@qauto.forstudy.space/panel/garage')

