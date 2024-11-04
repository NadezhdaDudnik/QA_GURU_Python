from pages.registration_form import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open('/automation-practice-form')
    registration_page.fill_first_name('Nadezhda')
    registration_page.fill_last_name('Dudnik')
    registration_page.fill_email('nadintest_test@mail.ru')
    registration_page.fill_gender()
    registration_page.fill_phone_number('8995114236')
    registration_page.fill_date_of_birth('02', 8, 1986)
    registration_page.select_subject('Computer Science')
    registration_page.select_hobbies('Sports')
    registration_page.upload_picture('it.jpg')
    registration_page.fill_current_address('Moscow, Lenina steet, 9/7')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Merrut')

    registration_page.submit_form()

    # проверки

    registration_page.should_have_registered_user_with_data(
        'Nadezhda',
    'Dudnik',
        'nadintest_test@mail.ru',
        'Female',
        '8995114236',
        '1986',
        'November',
        '02',
        'Computer Science',
        'Sports',
        'it.jpg',
        'Moscow, Lenina steet, 9/7',
        'Uttar Pradesh',
        'Merrut'
        )
