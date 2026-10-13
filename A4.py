a = int(input("Enter A: "))
b = int(input("Enter B: "))

if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("Bits must be 0 or 1")
else:
    if a == 1 and b == 1:
        and_output = 1
    else:
        and_output = 0

    if a == 1 or b == 1:
        or_output = 1
    else:
        or_output = 0

    if a != b:
        xor_output = 1
    else:
        xor_output = 0

    print("AND =", and_output)
    print("OR =", or_output)
    print("XOR =", xor_output)
