from enum import Enum
from faker import Faker
from models.user import User
from datetime import date
import random

fake = Faker()


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


student = User(
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    email=fake.email(),
    gender=random.choice(list(Gender)),
    phone="".join([str(random.randint(0, 9)) for _ in range(10)]),
    birth_date=date(2000, 6, 15).strftime("%d %B,%Y"),
    subjects=random.choice(['Maths', 'English', 'Physics']),
    hobbies=random.sample(list(Hobby), 2),
    picture='492x328.jpeg',
    address=fake.address(),
    state=random.choice(['NCR', 'Uttar Pradesh', 'Haryana']),
    city=random.choice(['Delhi', 'Gurgaon', 'Noida'])
)
