import allure
from selene import browser
from selene.support.conditions import (
    have,
    be,
)


def test_check_issue_tab_with_allure_steps():
    with allure.step('Открыть репозиторий в GitHub'):
        browser.open('https://github.com/NadezhdaDudnik/QA_GURU_Python')

    with allure.step('Перейти на вкладку Issues данного репозитория'):
        browser.element('#issues-tab').click()

    with allure.step('Проверить видимость номера Issue'):
        browser.all('.js-issue-row').element_by(have.text('#5')).should(be.visible)
