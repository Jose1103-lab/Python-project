def first_funct (a, b):
    res = a + b
    return res


def main():
    input1 = float(input("No1: "))
    input2 = float(input("No2: "))

    result = first_funct(input1, input2)
    print(result)

main()
