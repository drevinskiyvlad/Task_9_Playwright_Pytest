import random
import string

from data.data import Data


class Faker:
    def generate_random_string(self, length: int) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_valid_email(self) -> str:
        username = self.generate_random_string(8)
        domain = self.generate_random_string(5) + ".com"
        return f"{username}@{domain}"

    def generate_random_number_in_range(self, start, end) -> int:
        return random.randint(start, end)

    def generate_random_number_with_length(self, length):
        if length > 0:
            return int(''.join(random.choices(string.digits, k=length)))
        else:
            raise ValueError("Length should be greater than 0")

    def generate_random_country(self) -> str:
        return random.choice(Data.countries)