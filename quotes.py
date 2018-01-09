from typing import Dict, List
import json
from random import randint


QUOTES_PATH = 'quotes.json'

def get_quotes() -> List[Dict[str, str]]:
    with open(QUOTES_PATH, 'r') as QUOTES_FILE_OBJ:
        quotes = json.loads(QUOTES_FILE_OBJ.read())
    return quotes

def get_rand_index(until_int: int) -> int:
    return randint(0, until_int)

def main():
    quotes = get_quotes()
    random_index = get_rand_index(len(quotes))
    print(quotes[random_index])

if __name__ == '__main__':
    main()
