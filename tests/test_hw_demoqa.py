import os
from selene import browser


def test_homework_demoqa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Nadezhda')
    browser.element('#lastName').type('Dudnik')
    browser.element('#userEmail').type('nadin869@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('89081145057')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select option[value="1986"]').click()
    browser.element('.react-datepicker__month-select option[value="7"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('it.jpg'))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').click().element('#react-select-3-option-3').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()


