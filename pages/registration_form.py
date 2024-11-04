import os
from importlib import resources

from selene import (
    browser,
    be,
    have,
)

class RegistrationPage:

    def open(
            self,
            value
            ):
        browser.open(value)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(
            self,
            value
    ):
        browser.element('#firstName').type(value)

    def fill_last_name(
            self,
            value
    ):
        browser.element('#lastName').type(value)

    def fill_email(
            self,
            value
    ):
        browser.element('#userEmail').type(value)

    def fill_gender(
            self
    ):
        browser.element('[name=gender][value=Female]+label').click()

    def fill_phone_number(
            self,
            value
    ):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(
            self,
            day,
            month,
            year
    ):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def select_subject(
            self,
            value
    ):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(
            self,
            value
    ):
        browser.element(f'//label[text()="{value}"]').click()

    def upload_picture(
            self,
            file_name
    ):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/it.jpg'))

    def fill_current_address(
            self,
            value
    ):
        browser.element('#currentAddress').type(value)

    def fill_state(
            self,
            value
    ):
        browser.element('#state').click()
        browser.element(f'//*[text()="{value}"]').click()

    def fill_city(
            self,
            value
    ):
        browser.element('#city').click()
        browser.element(f'//*[text()="{value}"]').click()

    def submit_form(
            self
    ):
        browser.element('#submit').click()

    def should_have_registered_user_with_data(
            self,
            first_name,
            last_name,
            email,
            gender,
            phone_number,
            birth_year,
            birth_month,
            birth_day,
            subjects,
            hobbies,
            picture_name,
            current_address,
            state,
            city
    ):
        browser.element('table').should(be.visible)
        browser.element('//table//td[text()="Student Name"]/../td[2]').should(
            have.exact_text(f'{first_name} {last_name}')
        )
        browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text(email))
        browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.exact_text(gender))
        browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.exact_text(phone_number))
        browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(
            have.exact_text(f'{birth_day} {birth_month},{birth_year}')
        )
        browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text(subjects))
        browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text(hobbies))
        browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text(picture_name))
        browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text(current_address))
        browser.element('//table//td[text()="State and City"]/../td[2]').should(
            have.exact_text(f'{state} {city}')
        )
