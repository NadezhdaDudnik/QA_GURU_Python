import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import (
    have,
    be,
)


@allure.tag('WEB UI')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'nv.dudnik')
@allure.feature('Issues tab to GitHub')
@allure.story('Visibility number of issue')
@allure.link('https://github.com', name='Resource')
def test_check_issue_tab_with_decorator():
    open_repository()
    select_issue_tab()
    find_number_of_issue()


@allure.step('Открыть репозиторий')
def open_repository():
    browser.open('https://github.com/NadezhdaDudnik/QA_GURU_Python')


@allure.step('Перейти на вкладку Issues')
def select_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверить видимость первого Issue')
def find_number_of_issue():
    browser.all('.js-issue-row').element_by(have.text('#5')).should(be.visible)
