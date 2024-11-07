from selene import browser
from selene.support.conditions import (
    have,
    be,
)


def test_check_issue_tab_to_github():
    browser.open('https://github.com/NadezhdaDudnik/QA_GURU_Python')
    browser.element('#issues-tab').click()
    browser.all('.js-issue-row').element_by(have.text('#5')).should(be.visible)
