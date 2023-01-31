from Day3.day3p1 import get_priority_number, find_duplicates, find_badge

def test_get_priority_number():
    # Arrange and Act
    result1 = get_priority_number("a")
    result2 = get_priority_number("z")
    result3 = get_priority_number("A")
    result4 = get_priority_number("Z")

    # Assert
    assert result1 == 1
    assert result2 == 26
    assert result3 == 27
    assert result4 == 52

def test_find_duplicates():
     with open("Day3/day3_test_input.txt", "r") as f:
            data = f.readlines()
            result = find_duplicates(data)
            assert result == 157

def test_find_badge_one_group():
     with open("Day3/day3_test_input.txt", "r") as f:
            data = f.readlines()
            data = data[0:3]
            result = find_badge(data)
            assert result == 18

def test_find_badge_two_groups():
     with open("Day3/day3_test_input.txt", "r") as f:
            data = f.readlines()
            result = find_badge(data)
            assert result == 18 + 52