import sys
from random import randint


def min_max(numbers):
    """Funkce na zjisteni nejmensiho a nejvetsiho cisla a jeho indexu."""
    min_n = f"Min number:{min(numbers)}, Index:{numbers.index(min(numbers))}"
    max_n = f"Max number:{max(numbers)}, Index:{numbers.index(max(numbers))}"

    return f"{min_n}\n{max_n}"

def bubblesort(list):
    """Funkce na serazeni listu pomoci bubblesortu."""
    for i in range(len(list)):
        for n in range(len(list) - 1):
            if list[n] > list[n + 1]:
                list[n], list[n + 1] = list[n + 1], list[n]
    return list

