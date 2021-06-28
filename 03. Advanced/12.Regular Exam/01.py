from collections import deque


def get_ques():
    queue = deque(int(x) for x in input().split(", "))
    return queue


def are_ques(chocolates, milks):
    return len(chocolates) > 0 and len(milks) > 0


def main(chocolates, milks, cups=0):
    while True:
        if not are_ques(chocolates, milks):
            return chocolates, milks, cups
        choco_val = chocolates.pop()
        milk_val = milks.popleft()
        if (choco_val <= 0) and (milk_val > 0):
            milks.appendleft(milk_val)
            continue
        if (milk_val <= 0) and (choco_val > 0):
            chocolates.append(choco_val)
            continue
        if choco_val == milk_val:
            cups += 1
            if cups > 4:
                return chocolates, milks, cups
        else:
            milks.append(milk_val)
            if not choco_val - 5 <= 0:
                choco_val -= 5
                chocolates.append(choco_val)


def print_solution(chocolates, milks, cups):
    if cups >= 5:
        print(f"Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")
    if chocolates:
        print(f"Chocolate: {', '.join(map(str, chocolates))}")
    else:
        print(f"Chocolate: empty")
    if milks:
        print(f"Milk: {', '.join(map(str, milks))}")
    else:
        print(f"Milk: empty")


if __name__ == '__main__':
    chocolates = get_ques()
    milks = get_ques()
    chocolates, milks, cups = main(chocolates, milks)
    print_solution(chocolates, milks, cups)
