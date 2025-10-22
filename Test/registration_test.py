from selene import be, have
import sys
import os
from Pages.registration_page import RegistrationPage


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_form_filling(open_registration_page):
    registration_form = RegistrationPage()

    # Заполнение формы
    (registration_form
     .fill_firstname('Vadim')
     .fill_lastname('Tatarnikov')
     .fill_useremail('example@mmail.ru')
     .select_gender('Male')
     .fill_user_phone_number('1232323239')  # 10 цифр
     .fill_date_of_birth('2003', 'March', '23')
     .select_subject('Chemistry')
     .select_hobby('Reading')
     .upload_file('examplePhoto.png')  # Убедитесь что файл существует в папке resources
     .fill_current_address('test,Test str, 412')
     .select_state('Haryana')
     .select_city('Karnal')
     .click_submit_button())

    # Проверки
    registration_form.get_modal_popup().should(have.exact_text('Thanks for submitting the form'))

    # Проверка данных в таблице
    registration_form.should_registered_user_with.should(have.exact_texts(
        'Vadim Tatarnikov',
        'example@mmail.ru',
        'Male',
        '1232323239',
        '23 March,2003',
        'Chemistry',
        'Reading',
        'examplePhoto.png',
        'test,Test str, 412',
        'Haryana Karnal'
    ))