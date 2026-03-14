from pathlib import Path
from datetime import datetime

import allure
from selene import browser, have
from selene.support.conditions import be

from models.user import User
from utils.users import Gender, Hobby


class RegistrationPage:

    @allure.step("Open registration form page")
    def open(self):
        browser.open("/automation-practice-form")
        browser.element(".practice-form-wrapper").should(
            have.text("Practice Form")
        )
        return self

    @allure.step("Fill first name: {value}")
    def fill_first_name(self, value):
        browser.element("#firstName").should(be.visible).type(value)
        return self

    @allure.step("Fill last name: {value}")
    def fill_last_name(self, value):
        browser.element("#lastName").should(be.visible).type(value)
        return self

    @allure.step("Fill email: {value}")
    def fill_email(self, value):
        browser.element("#userEmail").should(be.visible).type(value)
        return self

    @allure.step("Select gender (default)")
    def select_gender(self):
        browser.all("label[for^='gender-radio-']")[0].should(be.visible).click()
        return self

    @allure.step("Select gender: {gender}")
    def select_gender_by_enum(self, gender: Gender):
        if gender == Gender.MALE:
            browser.all("label[for^='gender-radio-']")[0].click()
        elif gender == Gender.FEMALE:
            browser.all("label[for^='gender-radio-']")[1].click()
        elif gender == Gender.OTHER:
            browser.all("label[for^='gender-radio-']")[2].click()
        else:
            raise ValueError("Unknown gender")
        return self

    @allure.step("Fill phone number: {value}")
    def fill_phone(self, value):
        browser.element("#userNumber").should(be.visible).type(value)
        return self

    @allure.step("Fill birth date (static)")
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

    @allure.step("Fill birth date: {birth_date}")
    def fill_birth_date_from_user(self, birth_date: str):
        date_obj = datetime.strptime(birth_date, "%d %B,%Y")
        day = date_obj.day
        month = date_obj.month - 1
        year = date_obj.year

        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(
            f'.react-datepicker__month-select option[value="{month}"]'
        ).click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(
            f'.react-datepicker__year-select option[value="{year}"]'
        ).click()
        browser.element(
            f'[aria-label="Choose {date_obj.strftime("%A")}, {date_obj.strftime("%B")} {day}th, {year}"]'
        ).click()
        return self

    @allure.step("Fill subject: {value}")
    def fill_subject(self, value):
        browser.element("#subjectsInput").should(be.visible).type(value).press_enter()
        return self

    @allure.step("Select all hobbies (default)")
    def select_hobbies(self):
        hobbies = browser.all("label[for^='hobbies-checkbox-']")
        hobbies[0].should(be.visible).click()
        hobbies[1].should(be.visible).click()
        hobbies[2].should(be.visible).click()
        return self

    @allure.step("Select hobbies: {hobbies}")
    def select_hobby_by_enum(self, hobbies):
        for hobby in hobbies:
            if hobby == Hobby.SPORTS:
                browser.all("label[for^='hobbies-checkbox-']")[0].should(be.visible).click()
            elif hobby == Hobby.READING:
                browser.all("label[for^='hobbies-checkbox-']")[1].should(be.visible).click()
            elif hobby == Hobby.MUSIC:
                browser.all("label[for^='hobbies-checkbox-']")[2].should(be.visible).click()
            else:
                raise ValueError(f"No such hobby: {hobby}")
        return self

    @allure.step("Upload picture: {file_name}")
    def upload_picture(self, file_name):
        file_path = Path(__file__).parent.parent / "resources" / file_name
        browser.element("#uploadPicture").send_keys(
            str(file_path.resolve())
        )
        return self

    @allure.step("Fill address")
    def fill_address(self, value):
        browser.element("#currentAddress").should(be.visible).type(value)
        return self

    @allure.step("Select state and city (default)")
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

    @allure.step("Select state: {state} and city: {city}")
    def select_state_and_city_dynamic(self, state, city):
        browser.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            browser.element("#state").locate(),
        )
        browser.element("#state").should(be.visible).click()
        browser.element("#react-select-3-input").should(be.existing).type(state).press_enter()
        browser.element("#city").should(be.visible).click()
        browser.element("#react-select-4-input").should(be.existing).type(city).press_enter()
        return self

    @allure.step("Submit registration form")
    def submit(self):
        browser.element("#submit").should(be.visible).should(be.enabled).click()
        return self

    @allure.step("Verify registration result (manual data)")
    def should_have_registered(self, expected_values):
        browser.element(".modal-header").should(
            have.text("Thanks for submitting the form")
        )
        browser.all(".table-hover tbody tr td")[1::2].should(
            have.exact_texts(*expected_values)
        )

    @allure.step("Verify registration result for user: {user.email}")
    def should_have_registered_user(self, user: User):
        expected_texts = [
            f"{user.first_name} {user.last_name}",
            user.email,
            user.gender.value,
            user.phone,
            user.birth_date,
            user.subjects,
            ", ".join([hobby.value for hobby in user.hobbies]),
            user.picture,
            user.address.replace("\n", " "),
            f"{user.state} {user.city}",
        ]
        browser.all(".table-hover tbody tr td")[1::2].should(
            have.exact_texts(*expected_texts)
        )

    @allure.step("Register user via User model")
    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender_by_enum(user.gender)
        self.fill_phone(user.phone)
        self.fill_birth_date_from_user(user.birth_date)
        self.fill_subject(user.subjects)
        self.select_hobby_by_enum(user.hobbies)
        self.upload_picture(user.picture)
        self.fill_address(user.address)
        self.select_state_and_city_dynamic(user.state, user.city)
        self.submit()
        return self