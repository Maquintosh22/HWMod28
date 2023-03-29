from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_31_char = 'МаксиммаксиммаксиммаксиммаксимМ'
    last_name_1_char = 'А'
    password_21_char = 'QwertyQwertyQwertyQwe'
    password_without_simbol = "Qwertyui"
    email_without_domain = 'sf22test@'


class Valid_Data:
    valid_first_name = 'Максим'
    valid_last_name = 'Алексеевич'
    valid_password = 'SF22test'
