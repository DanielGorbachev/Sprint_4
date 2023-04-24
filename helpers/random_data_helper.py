import random
from faker import Faker


class RandomDataHelper:
    fake = Faker('ru_RU')

    @staticmethod
    def generate_random_name(self):
        return self.fake.first_name()

    @staticmethod
    def generate_random_surname(self):
        return self.fake.last_name()

    @staticmethod
    def generate_random_adress(self):
        s = ["Сишарп", "Сиплюсплюс", "Питон"]
        return f'ул.{random.choice(s)}, дом{random.randint(1,30)}, кв.{random.randint(1,300)}'

    @staticmethod
    def generate_random_phone_number(self):
        return f'+7{random.randint(0000000000,9999999999)}'

    @staticmethod
    def random_color_choice(self):
        colors = ["black", "gray", "black and gray"]
        return random.choice(colors)