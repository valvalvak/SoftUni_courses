from collections import deque

parentheses = input()

opening = "(", "{", "["
closing = ")", "}", "]"

queue = deque()
queue_len = 0
isTrue = True
for el in parentheses:
    if el in opening:
        queue.append(el)
        queue_len += 1
    else:
        if queue:
            last_el_in_queue = queue[-1]
            opening_index = opening.index(last_el_in_queue)
            if opening_index == closing.index(el):
                queue.pop()
            else:
                isTrue = False
                break

if isTrue and queue_len == len(parentheses) / 2:
    print("YES")
else:
    print("NO")
