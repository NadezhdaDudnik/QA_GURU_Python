import allure
from allure_commons.types import Severity

from pages.registration_form import RegistrationPage
from data.user_info import user_data


@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'nv.dudnik')
@allure.feature('Форма регистрации для пользователя')
@allure.story('Заполнение и отправка данных для регистрации пользователя')
@allure.link('https://demoqa.com/automation-practice-form', name='Testing form + allure + jenkins + selenoid')
def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open('/automation-practice-form')
    registration_page.register(user_data)
    registration_page.should_have_registered_user_with_data(user_data)
    registration_page.close_table()
