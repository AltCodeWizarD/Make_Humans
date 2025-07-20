import os
import random

from faker import Faker

from skills_dictionary import skills
from letters_dictionary import letters
import file_operations

fake = Faker("ru_RU")
RUNIC_SKILLS = []
GENDER = ['male', 'female']
CHARACTERISTICS = range(3, 18)

os.makedirs("char_cards", exist_ok=True)

for skill in skills:
    runic = skill
    for letter, replacement in letters.items():
        runic = runic.replace(letter, replacement)
    RUNIC_SKILLS.append(runic)


def generate_character(number):
    file_number = number + 1
    filename = os.path.join("char_cards", f"result{file_number}.svg")

    random_gender = random.choice(GENDER)

    (
        random_strength,
        random_agility,
        random_endurance,
        random_intelligence,
        random_luck
    ) = random.sample(CHARACTERISTICS, 5)

    (
        random_skill_1,
        random_skill_2,
        random_skill_3
    ) = random.sample(RUNIC_SKILLS, 3)

    if random_gender == 'male':
        first_name = FAKE.first_name_male()
        last_name = FAKE.last_name_male()
    else:
        first_name = FAKE.first_name_female()
        last_name = FAKE.last_name_female()

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "job": FAKE.job(),
        "town": FAKE.city(),
        "strength": random_strength,
        "agility": random_agility,
        "endurance": random_endurance,
        "intelligence": random_intelligence,
        "luck": random_luck,
        "skill_1": random_skill_1,
        "skill_2": random_skill_2,
        "skill_3": random_skill_3,
    }

    file_operations.render_template("charsheet.svg", filename, context)


def main():
    for number in range(10):
        generate_character(number)


if __name__ == '__main__':
    main()
