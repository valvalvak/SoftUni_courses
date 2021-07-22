from collections import deque


def get_ques():
    queue = deque(int(x) for x in input().split(", "))
    return queue


def are_ques(customers, taxi):
    return len(customers) > 0 and len(taxi) > 0


def main(customers, taxi, time=0):
    while True:
        if not are_ques(customers, taxi):
            return customers, taxi, time
        current_customer = customers.popleft()
        current_taxi = taxi.pop()
        if current_customer <= current_taxi:
            time += current_customer
            continue
        else:
            customers.appendleft(current_customer)


def print_solution(customers_left, drive_time):
    if not customers_left:
        print(f"All customers were driven to their destinations\n"
              f"Total time: {drive_time} minutes")
    else:
        print(f"Not all customers were driven to their destinations\n"
              f"Customers left: {', '.join(map(str, customers_left))}")


if __name__ == '__main__':
    customers = get_ques()
    taxi = get_ques()
    customers_left, taxi_left, drive_time = main(customers, taxi)
    print_solution(customers_left, drive_time)
