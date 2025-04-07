import os
import re
import uuid
from random import randint


class Utils:
    @staticmethod
    def code_generator():
        return str(randint(100000, 999999))

    @staticmethod
    def generate_unique_filename(directory: str, filename: str) -> str:
        if not os.path.exists(directory):
            os.makedirs(directory)
        name, ext = os.path.splitext(filename)
        new_filename = filename

        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{uuid.uuid4().hex[:16]}{ext}"
        return new_filename

    @staticmethod
    def vilification_pattern_mobile(value):
        pattern = re.compile(r'^(\+98|0)?9\d{9}$')
        return pattern.match(value)

    @staticmethod
    def normalize_phone_number(phone_number: str) -> str:
        """Normalize the phone number to a standard format."""
        if phone_number.startswith("0"):
            return "+98" + phone_number[1:]
        return phone_number
