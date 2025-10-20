from selene import be, have
import sys
import os

# Добавляем путь к папке Pages в sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Pages.registration_page import RegistrationPage


def test_form_filling(open_registration_page):
    registration_form = RegistrationPage()

    # Заполнение формы
    (registration_form
     .fill_firstname('Vadim')
     .fill_lastname('Tatarnikov')
     .fill_useremail('example@mmail.ru')
     .select_gender('Male')
     .fill_user_phone_number('2232323232')  # 10 цифр
     .fill_date_of_birth('2003', 'March', '23')
     .select_subject('Chemistry')
     .select_hobby('Reading')
     .upload_file('examplePhoto.png')  # Убедитесь что файл существует в папке resources
     .fill_current_address('SPLSFD,Test str., 1')
     .select_state('Haryana')
     .select_city('Karnal')
     .click_submit_button())

    # Проверки
    registration_form.get_modal_popup().should(have.exact_text('Thanks for submitting the form'))

    # Проверка данных в таблице
    registration_form.should_registered_user_with.should(have.exact_texts(
        'Vadim Tatarnikov',  # Имя и фамилия
        'example@mmail.ru',  # Email
        'Male',  # Gender
        '2232323232',  # Mobile (10 digits)
        '23 March,2003',  # Date of Birth
        'Chemistry',  # Subjects
        'Reading',  # Hobbies
        'examplePhoto.png',  # Picture
        'SPLSFD,Test str., 1',  # Address
        'Haryana Karnal'  # State and City
    ))