# def flights(*args):
#     destinations = args[0:-1:2]
#     passangers = args[1:-1:2]
#     flights_result = {}
#     for index in range(len(args)):
#         if destinations[index] == 'Finish':
#             return flights_result
#         elif destinations[index] not in flights_result:
#             flights_result[destinations[index]] = 0
#         flights_result[destinations[index]] += passangers[index]
#     return flights_result


from collections import deque


def flights(*args):
    flights_result = {}
    queue = deque(args)
    while queue:
        destination = queue.popleft()
        if destination == "Finish":
            return flights_result
        elif destination not in flights_result:
            flights_result[destination] = 0
        passangers = int(queue.popleft())
        flights_result[destination] += passangers
    return flights_result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
