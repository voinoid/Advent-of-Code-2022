class Monkey:
    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = format_check(name)
        self.items = format_items(items)
        self.operation = format_operation(operation)
        self.check = format_check(test)
        self.ifTrue = format_check(if_true)
        self.ifFalse = format_check(if_false)
        self.itemsInspected = 0

    def __str__(self) -> str:
        return f"Monkey {self.name}:\nItems: {self.items}\nNew = Old {self.operation}\nIf divisible by {self.check}\n   If True then throw to Monkey {self.ifTrue}\n   If False then throw to Monkey {self.ifFalse}"
    
    def inspect(self, item: int) -> tuple:
        self.itemsInspected += 1

        if self.operation[1] == "old":
            ops = {"+": plus(item, item),
               "*": times(item, item),}
        else:
            ops = {"+": plus(item, int(self.operation[1])),
               "*": times(item, int(self.operation[1])),}
            
        # worry_level_small = ops[self.operation[0]]//3
        worry_level = ops[self.operation[0]]

        if worry_level % self.check == 0:
            #worry_level /= self.check
            pass_to_monkey = self.ifTrue
        else:
            pass_to_monkey = self.ifFalse

        return (pass_to_monkey, worry_level)


def format_items(items: str) -> list[int]:
    items = items.strip()
    items_list = [int(x) for x in items.split(", ")]
    return items_list

def format_operation(operation: str) -> tuple:
    sign, amount = operation.split(" ")[-2:]
    return (sign, amount)  

def format_check(item:str) -> int:
    return int(item.split(" ")[-1])

def plus(num1: int, num2: int) -> int:
    return num1 + num2

def times(num1: int, num2: int) -> int:
    return num1 * num2