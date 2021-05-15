percents = int(input())
progressed = "%" * (percents // 10)
remaining = "." * (10-(len(progressed)))
result = list(progressed + remaining)
if percents == 100:
    print(f"100% Complete!\n"
          f"[{''.join(result)}]")
else:
    print(f"{percents}% [{''.join(result)}]\n"
          f"Still loading...")

