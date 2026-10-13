count = int(input("How many resistors? "))
total_resistance = 0

for i in range(1, count + 1):
    resistance = float(input("Enter R" + str(i) + ": "))
    total_resistance = total_resistance + resistance

print("Total resistance =", total_resistance, "ohm")
