from datetime import datetime
from pathlib import Path

from selene import browser, have
from selene.support.conditions import be

FIRST_NAME = "First Name"
LAST_NAME = "Last Name"
EMAIL = "blabla@mail.com"
GENDER = "Male"
PHONE = "8911111111"
DOB_INPUT = "20 Feb 2002"
SUBJECT = "English"
HOBBY_1 = "Sports"
HOBBY_2 = "Reading"
HOBBY_3 = "Music"
PICTURE = "492x328.jpeg"
ADDRESS = "Current address"
STATE = "NCR"
CITY = "Delhi"

first_name = browser.element("#firstName")
last_name = browser.element("#lastName")
email = browser.element("#userEmail")
gender = browser.all("label[for^='gender-radio-']")
phone_number = browser.element("#userNumber")

date_of_birth = browser.element("#dateOfBirthInput")
date_picker = browser.element(".react-datepicker__input-container input")
subject = browser.element("#subjectsInput")
hobby = browser.all("label[for^='hobbies-checkbox-']")
current_address = browser.element("#currentAddress")
state = browser.element("#state")
city = browser.element("#city")
submit_button = browser.element("#submit")
modal_popup = browser.element(".modal-header")


def test_form(browser_settings):
    browser.open("/automation-practice-form")
    browser.element(".practice-form-wrapper").should(have.text("Practice Form"))

    first_name.should(be.visible).type(FIRST_NAME)
    last_name.should(be.visible).type(LAST_NAME)
    email.should(be.visible).type(EMAIL)
    gender[0].should(be.visible).click()
    phone_number.should(be.visible).type(PHONE)
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element('.react-datepicker__month-select option[value="1"]').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element('.react-datepicker__year-select option[value="2002"]').click()
    browser.element('[aria-label="Choose Wednesday, February 20th, 2002"]').click()
    subject.click().type(SUBJECT).press_enter()
    hobby[0].should(be.visible).click()
    hobby[1].should(be.visible).click()
    hobby[2].should(be.visible).click()
    file_path = Path(__file__).parent.parent / "resources" / "492x328.jpeg"
    browser.element("#uploadPicture").send_keys(str(file_path.resolve()))
    current_address.should(be.visible).type(ADDRESS)
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", state.locate())
    state.click()
    browser.element("#react-select-3-input").type(STATE).press_enter()
    city.should(be.visible).click()
    browser.element("#react-select-4-input").type(CITY).press_enter()
    submit_button.should(be.visible).click()

    modal_popup.should(have.text("Thanks for submitting the form"))
    browser.all(".table-hover tbody tr td")[1].should(
        have.text(FIRST_NAME + " " + LAST_NAME)
    )
    browser.all(".table-hover tbody tr td")[3].should(have.text(EMAIL))
    browser.all(".table-hover tbody tr td")[5].should(have.text(GENDER))
    browser.all(".table-hover tbody tr td")[7].should(have.text(PHONE))
    browser.all(".table-hover tbody tr td")[9].should(
        have.text(datetime.strptime(DOB_INPUT, "%d %b %Y").strftime("%d %B,%Y"))
    )
    browser.all(".table-hover tbody tr td")[11].should(have.text(SUBJECT))
    browser.all(".table-hover tbody tr td")[13].should(
        have.text(HOBBY_1 + ", " + HOBBY_2 + ", " + HOBBY_3)
    )
    browser.all(".table-hover tbody tr td")[15].should(have.text(PICTURE))
    browser.all(".table-hover tbody tr td")[17].should(have.text(ADDRESS))
    browser.all(".table-hover tbody tr td")[19].should(have.text(STATE + " " + CITY))
