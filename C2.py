def parallel_resistance(resistors):
    sum_of_inverses = 0
    for r in resistors:
        sum_of_inverses = sum_of_inverses + 1 / r
    return round(1 / sum_of_inverses, 2)

print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))
