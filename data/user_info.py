from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user_data = User(
    first_name='Nadezhda',
    last_name='Dudnik',
    email='nadintest_test@mail.ru',
    gender='Female',
    phone_number='8995114236',
    date_of_birth_year='1986',
    date_of_birth_month='November',
    date_of_birth_day='02',
    subject='Computer Science',
    hobby='Sports',
    picture='it.jpg',
    address='Moscow, Lenina steet, 9/7',
    state='Uttar Pradesh',
    city='Merrut'
)
