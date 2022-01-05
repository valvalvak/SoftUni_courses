capacity = int(input())
pipe_one = int(input())
pipe_two = int(input())
time_out = float(input())
first_pipe = pipe_one * time_out
second_pipe = pipe_two * time_out
fill = first_pipe + second_pipe
if fill <= capacity:
    print(f"The pool is {fill / capacity * 100:.2f}% full. "
          f"Pipe 1: {first_pipe / fill * 100:.2f}%. "
          f"Pipe 2: {second_pipe / fill * 100:.2f}%.")
else:
    print(f"For {time_out:.2f} hours the pool overflows with {abs(capacity - fill):.2f} liters.")
