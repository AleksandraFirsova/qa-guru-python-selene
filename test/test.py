from pathlib import Path

from selene import browser, have
from selene.support.conditions import be


def test_form(browser_settings):
    browser.open("/automation-practice-form")
    browser.element(".practice-form-wrapper").should(have.text("Practice Form"))

    browser.element("#firstName").should(be.visible).type("First Name")
    browser.element("#lastName").should(be.visible).type("Last Name")
    browser.element("#userEmail").should(be.visible).type("blabla@mail.com")
    browser.all("label[for^='gender-radio-']")[0].should(be.visible).click()
    browser.element("#userNumber").should(be.visible).type("8911111111")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element('.react-datepicker__month-select option[value="1"]').click()
    browser.element(".react-datepicker__year-select").click()
    browser.element('.react-datepicker__year-select option[value="2002"]').click()
    browser.element('[aria-label="Choose Wednesday, February 20th, 2002"]').click()
    browser.element("#subjectsInput").click().type("English").press_enter()
    browser.all("label[for^='hobbies-checkbox-']")[0].should(be.visible).click()
    browser.all("label[for^='hobbies-checkbox-']")[1].should(be.visible).click()
    browser.all("label[for^='hobbies-checkbox-']")[2].should(be.visible).click()
    file_path = Path(__file__).parent.parent / "resources" / "492x328.jpeg"
    browser.element("#uploadPicture").send_keys(str(file_path.resolve()))
    browser.element("#currentAddress").should(be.visible).type("Current address")
    browser.driver.execute_script(
        "arguments[0].scrollIntoView(true);", browser.element("#state").locate()
    )
    browser.element("#state").click()
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#city").should(be.visible).click()
    browser.element("#react-select-4-input").type("Delhi").press_enter()
    browser.element("#submit").should(be.visible).click()

    browser.element(".modal-header").should(have.text("Thanks for submitting the form"))
    browser.all(".table-hover tbody tr td")[1::2].should(
        have.exact_texts(
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
        )
    )
