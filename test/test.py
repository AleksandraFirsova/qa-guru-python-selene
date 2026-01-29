from page.registration_page import RegistrationPage
from utils.users import student


def test_form():
    registration_page = RegistrationPage()

    registration_page.open()
    (
        registration_page
        .fill_first_name("First Name")
        .fill_last_name("Last Name")
        .fill_email("blabla@mail.com")
        .select_gender()
        .fill_phone("8911111111")
        .fill_birth_date()
        .fill_subject("English")
        .select_hobbies()
        .upload_picture("492x328.jpeg")
        .fill_address("Current address")
        .select_state_and_city()
        .submit()
    )

    registration_page.should_have_registered([
        "First Name Last Name",
        "blabla@mail.com",
        "Male",
        "8911111111",
        "20 February,2002",
        "English",
        "Sports, Reading, Music",
        "492x328.jpeg",
        "Current address",
        "NCR Delhi",
    ])


def test_register_user():
    reg_page = RegistrationPage()
    reg_page.open().register(student)
    reg_page.should_have_registered_user(student)
