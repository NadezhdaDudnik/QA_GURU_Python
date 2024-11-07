from pages.registration_form import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open('/automation-practice-form')
    registration_page.remove_banners_and_footer()
    registration_page.fill_first_name('Nadezhda')
    registration_page.fill_last_name('Dudnik')
    registration_page.fill_email('nadintest_test@mail.ru')
    registration_page.fill_gender('Female')
    registration_page.fill_phone_number('8995114236')
    registration_page.fill_date_of_birth('02', 8, 1986)
    registration_page.select_subject('Computer Science')
    registration_page.select_hobby('Sports')
    registration_page.upload_picture('it.jpg')
    registration_page.fill_current_address('Moscow, Lenina steet, 9/7')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Merrut')

    registration_page.submit_form()

    # проверки

    registration_page.should_have_registered_user_with_data(
        {
            'first_name': 'Nadezhda',
            'last_name': 'Dudnik',
            'email': 'nadintest_test@mail.ru',
            'gender': 'Female',
            'phone_number': '8995114236',
            'birth_year': '1986',
            'birth_month': 'November',
            'birth_day': '02',
            'subjects': 'Computer Science',
            'hobbies': 'Sports',
            'picture_name': 'it.jpg',
            'current_address': 'Moscow, Lenina steet, 9/7',
            'state': 'Uttar Pradesh',
            'city': 'Merrut'
        }
    )
