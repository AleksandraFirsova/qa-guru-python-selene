from pathlib import Path

from selene import browser, have
from selene.support.conditions import be


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        browser.element(".practice-form-wrapper").should(
            have.text("Practice Form")
        )
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").should(be.visible).type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").should(be.visible).type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").should(be.visible).type(value)
        return self

    def select_gender(self):
        browser.all("label[for^='gender-radio-']")[0].should(be.visible).click()
        return self

    def fill_phone(self, value):
        browser.element("#userNumber").should(be.visible).type(value)
        return self

    def fill_birth_date(self):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element('.react-datepicker__month-select option[value="1"]').click()
        browser.element(".react-datepicker__year-select").click()
        browser.element('.react-datepicker__year-select option[value="2002"]').click()
        browser.element(
            '[aria-label="Choose Wednesday, February 20th, 2002"]'
        ).click()
        return self

    def fill_subject(self, value):
        browser.element("#subjectsInput").should(be.visible).type(value).press_enter()
        return self

    def select_hobbies(self):
        hobbies = browser.all("label[for^='hobbies-checkbox-']")
        hobbies[0].should(be.visible).click()
        hobbies[1].should(be.visible).click()
        hobbies[2].should(be.visible).click()
        return self

    def upload_picture(self, file_name):
        file_path = (
                Path(__file__).parent.parent / "resources" / file_name
        )
        browser.element("#uploadPicture").send_keys(
            str(file_path.resolve())
        )
        return self

    def fill_address(self, value):
        browser.element("#currentAddress").should(be.visible).type(value)
        return self

    def select_state_and_city(self):
        browser.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            browser.element("#state").locate(),
        )
        browser.element("#state").click()
        browser.element("#react-select-3-input").type("NCR").press_enter()
        browser.element("#city").should(be.visible).click()
        browser.element("#react-select-4-input").type("Delhi").press_enter()
        return self

    def submit(self):
        browser.element("#submit").should(be.visible).click()
        return self

    def should_have_registered(self, expected_values):
        browser.element(".modal-header").should(
            have.text("Thanks for submitting the form")
        )
        browser.all(".table-hover tbody tr td")[1::2].should(
            have.exact_texts(*expected_values)
        )