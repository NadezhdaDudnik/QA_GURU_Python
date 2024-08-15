import os
from selene import (
    browser,
    command,
    have,
)


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('footer').perform(command.js.remove)
    browser.element('#firstName').type('Nadezhda')
    browser.element('#lastName').type('Dudnik')
    browser.element('#userEmail').type('nadintest_test@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('8995114236')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select option[value="1986"]').click()
    browser.element('.react-datepicker__month-select option[value="7"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Computer Science').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('it.jpg'))
    browser.element('#currentAddress').type('Moscow')
    browser.element("#react-select-3-input").type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()
    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            'Nadezhda Dudnik',
            'nadintest_test@mail.ru',
            'Female',
            '8995114236',
            '02 August,1986',
            'Computer Science',
            'Sports',
            'it.jpg',
            'Moscow',
            'Haryana Karnal',
        )
    )
