import random
from faker import Faker


from data.data import Person

faker_ru = Faker("ru_Ru")
Faker.seed()


def generated_file():
    path = rf"C:\Users\davle\PycharmProjects\automation_qa{random.randint(0, 777)}.txt"
    with open(path, "w+") as my_file:
        my_file.write(f"Hello world{random.randint(0, 777)}")

    return my_file.name, path


def generated_person():
    yield Person(
        full_name=faker_ru.first_name()
        + " "
        + faker_ru.last_name()
        + " "
        + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )
