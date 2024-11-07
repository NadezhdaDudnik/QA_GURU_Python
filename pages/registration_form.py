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
            url
    ):
        browser.open(url)

    def remove_banners_and_footer(
            self
    ):
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
            self,
            gender_value
    ):
        browser.element(f'[name=gender][value={gender_value}]+label').click()

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
        day = f'0{day}' if len(day) == 1 else day
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def select_subject(
            self,
            value
    ):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobby(
            self,
            value
    ):
        browser.element(f'//label[text()="{value}"]').click()

    def upload_picture(
            self,
            file_name
            ):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'../resources/{file_name}'))

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
            data
            ):
        browser.element('table').should(be.visible)
        browser.element('//table//td[text()="Student Name"]/../td[2]').should(
            have.exact_text(f"{data['first_name']} {data['last_name']}")
        )
        browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text(data['email']))
        browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.exact_text(data['gender']))
        browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.exact_text(data['phone_number']))
        browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(
            have.exact_text(f"{data['birth_day']} {data['birth_month']},{data['birth_year']}")
        )
        browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text(data['subjects']))
        browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text(data['hobbies']))
        browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text(data['picture_name']))
        browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text(data['current_address']))
        browser.element('//table//td[text()="State and City"]/../td[2]').should(
            have.exact_text(f"{data['state']} {data['city']}")
        )
