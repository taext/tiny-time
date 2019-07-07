import datetime
import string
from collections import OrderedDict


def build_int_dict():

    integers = OrderedDict()

    integers[0] = 'z'
    for i, character in enumerate(string.ascii_lowercase):
        if character == 'z':
            break
        integers[i+1] = character
        
    for i, character in enumerate(string.ascii_uppercase):
        if character == 'Z':
            break
        integers[i+26] = character

    for i, character in enumerate([9,8,7,6,5,4,3,2,1]):
        integers[51+i] = character
        
    return (integers)


def build_character_dict():

    numbers = build_int_dict()

    characters = {v: k for k, v in numbers.items()}

    return characters


def now():

    numbers = build_int_dict()

    now = datetime.datetime.now()
    now_time = str(now).split(" ")[1]
    hour, minute, secs =  str(now_time).split(":")
    
    now_date = str(now).split(" ")[0]
    year, month, day = now_date.split("-")

    hour_char, minute_char = (numbers[int(hour)], numbers[int(minute)])
    year_char, month_char, day_char = (numbers[int(year[-2:])], numbers[int(month)], numbers[int(day)])
    full_tiny_time = year_char + '_' + month_char + day_char + ':' + hour_char + minute_char

    return full_tiny_time