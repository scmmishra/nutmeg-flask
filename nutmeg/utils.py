from datetime import datetime
from box import Box
import string
import random

def get_current_session():
	return Box({"username": "joey", "email": "joey@example.com", "id": "44UXSB"})

def get_timestamp():
	return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
