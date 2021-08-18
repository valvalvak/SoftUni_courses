"""retake exam solution 1"""
from collections import deque


def collect_honey(value_a, value_b, str_symbol):
    if str_symbol == "+":
        return value_a + value_b
    elif str_symbol == "-":
        return value_a - value_b
    elif str_symbol == "*":
        return value_a * value_b
    elif str_symbol == "/":
        return value_a / value_b


def get_int_ques(list_input):
    queue = deque([int(x) for x in list_input.split(" ")])
    return queue


def get_opreation_symbols_in_que(str_letters):
    queue = deque(x for x in str_letters.split(" "))
    return queue


worker_bees = get_int_ques(input())
nectar_que = get_int_ques(input())
honey_making_symbol_commands = input()
command_symbols_que = get_opreation_symbols_in_que(honey_making_symbol_commands)

result = 0

while True:
    if len(worker_bees) <= 0 or len(nectar_que) <= 0:
        break
    bee_value = worker_bees.popleft()
    nectar_value = nectar_que.pop()
    curren_symbol = command_symbols_que.popleft()
    if bee_value <= nectar_value:
        result += abs(collect_honey(bee_value, nectar_value, curren_symbol))
    else:
        worker_bees.appendleft(bee_value)
        command_symbols_que.appendleft(curren_symbol)

print(f"Total honey made: {result}")
if worker_bees:
    print(f"Bees left: {', '.join([str(x) for x in worker_bees])}")
if nectar_que:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_que])}")
