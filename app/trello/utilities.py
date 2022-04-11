import random
import string
from django.core.exceptions import ValidationError
from typing import List

def title_validator(name:str, length:int):
    if not name or len(name) > length:
        raise ValidationError(message= f"Too long: {len(name)}. Max. allowed: {length} characters", code="401")

def random_title_generator(prefix:str, length: int):
    if not prefix or not length:
        raise ValidationError(message="Prefix and length are required")
    words = ''.join(random.choice(string.ascii_letters) for i in range(length))
    numbers = ''.join(random.choice(string.digits) for i in range(length))
    return prefix + "-" + words + "-" + numbers

def categoty_validator(categories:List[str], category:str):
    if categories.count(category) == 0:
        raise ValidationError(message= f"The category: {category} is not valid")
