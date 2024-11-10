import os
import allure

from selene import (
    browser,
    be,
    have,
)

from data.user_info import User


class RegistrationPage:
    @allure.step('Открыть форму регистрации')
    def open(
            self,
            url
    ):
        browser.open(url)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step('Заполнить поле "First Name"')
    def fill_first_name(
            self,
            value
    ):
        browser.element('#firstName').type(value)

    @allure.step('Заполнить поле "Last Name"')
    def fill_last_name(
            self,
            value
    ):
        browser.element('#lastName').type(value)

    @allure.step('Заполнить поле "Email"')
    def fill_email(
            self,
            value
    ):
        browser.element('#userEmail').type(value)

    @allure.step('Заполнить поле "Gender"')
    def fill_gender(
            self,
            gender_value
    ):
        browser.element(f'[name=gender][value={gender_value}]+label').click()

    @allure.step('Заполнить поле "Mobile(10 Digits)"')
    def fill_phone_number(
            self,
            value
    ):
        browser.element('#userNumber').type(value)

    @allure.step('Заполнить поле "Date of Birth"')
    def fill_date_of_birth(
            self,
            day,
            month,
            year
    ):
        day = f'0{day}' if len(day) == 1 else day
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    @allure.step('Заполнить поле "Subjects"')
    def select_subject(
            self,
            value
    ):
        browser.element('#subjectsInput').type(value).press_enter()

    @allure.step('Заполнить поле "Hobbies"')
    def select_hobby(
            self,
            value
    ):
        browser.element(f'//label[text()="{value}"]').click()

    @allure.step('Загрузить картинку')
    def upload_picture(
            self,
            file_name
    ):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/it.jpg'))

    @allure.step('Заполнить поле "Current Address"')
    def fill_current_address(
            self,
            value
    ):
        browser.element('#currentAddress').type(value)

    @allure.step('Заполнить поле "State"')
    def fill_state(
            self,
            value
    ):
        browser.element('#state').click()
        browser.element(f'//*[text()="{value}"]').click()

    @allure.step('Заполнить поле "City"')
    def fill_city(
            self,
            value
    ):
        browser.element('#city').click()
        browser.element(f'//*[text()="{value}"]').click()

    @allure.step('Подтвердить данные на форме')
    def submit_form(
            self
    ):
        browser.element('#submit').click()

    @allure.step('Зарегистрировать пользователя')
    def register(
            self,
            user: User
    ):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth_day, user.date_of_birth_month, user.date_of_birth_year)
        self.select_subject(user.subject)
        self.select_hobby(user.hobby)
        self.upload_picture(user.picture)
        self.fill_current_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_form()

    @allure.step('Проверить данные пользователя в таблице')
    def should_have_registered_user_with_data(
            self,
            user: User
    ):
        browser.element('//table').should(be.visible)
        browser.element('//table//td[text()="Student Name"]/../td[2]').should(
            have.exact_text(f'{user.first_name} {user.last_name}')
        )
        browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text(user.email))
        browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.exact_text(user.gender))
        browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.exact_text(user.phone_number))
        browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(
            have.exact_text(f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}')
        )
        browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text(user.subject))
        browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text(user.hobby))
        browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text(user.picture))
        browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text(user.address))
        browser.element('//table//td[text()="State and City"]/../td[2]').should(
            have.exact_text(f'{user.state} {user.city}')
        )

    @allure.step('Закрыть таблицу с проверенными данными')
    def close_table(
            self
    ):
        browser.element('#closeLargeModal').click()
        browser.element('#example-modal-sizes-title-lg').should(be.not_.visible)
