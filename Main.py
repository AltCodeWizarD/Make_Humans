import os
import random

from faker import Faker
import file_operations

os.makedirs("char_cards", exist_ok=True)

fake = Faker("ru_RU")

gender = ['male', 'female']
characteristics = range(3, 18)

def generate_character(number):
    file_number = number + 1
    filename = os.path.join("char_cards", f"result{file_number}.svg")
    
    random_gender = random.choice(gender)
    
    random_strength, random_agility, random_endurance, random_intelligence, random_luck = random.sample(characteristics, 5)
    
    skills = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
    ]
    
    letters = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }

    runic_skills = []
    for skill in skills:
        runic = skill
        for letter, replacement in letters.items():
            runic = runic.replace(letter, replacement)
        runic_skills.append(runic)

    random_skill_1, random_skill_2, random_skill_3 = random.sample(runic_skills, 3)

    if random_gender == 'male':
        context = {
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.choice(characteristics),
            "agility": random.choice(characteristics),
            "endurance": random.choice(characteristics),
            "intelligence": random.choice(characteristics),
            "luck": random.choice(characteristics),
            "skill_1": random_skill_1,
            "skill_2": random_skill_2,
            "skill_3": random_skill_3,
        }
    else:
        context = {
            "first_name": fake.first_name_female(),
            "last_name": fake.last_name_female(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.choice(characteristics),
            "agility": random.choice(characteristics),
            "endurance": random.choice(characteristics),
            "intelligence": random.choice(characteristics),
            "luck": random.choice(characteristics),
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
