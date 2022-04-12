import random
import string
from exceptions import appExceptions
from typing import List

def title_validator(name:str, length:int):
    if not name:
        raise appExceptions.BadRequest(detail="Empty name :(")
    if len(name) > length:
        raise appExceptions.ValidationError(detail= f"Too long: {len(name)}. Max. allowed: {length} characters")

def random_title_generator(prefix:str, length: int):
    if not prefix or not length:
        raise appExceptions.ValidationError(detail="Prefix and length are required")
    words = ''.join(random.choice(string.ascii_letters) for i in range(length))
    numbers = ''.join(random.choice(string.digits) for i in range(length))
    return prefix + "-" + words + "-" + numbers

def categoty_validator(categories:List[str], category:str):
    if categories.count(category) == 0:
        raise appExceptions.ValidationError(detail= f"The category: {category} is not valid")
