from Day3.day3p1 import get_priority_number

def test_get_priority_number_upper() -> None:
    num = get_priority_number("P")
    assert num == 42

def test_get_priority_number_lower() -> None:
    num = get_priority_number("p")
    assert num == 16