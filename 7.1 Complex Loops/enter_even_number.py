while True:
    print("Enter even number: ", end="")
    n = int(input())
    if n % 2 == 0:
        break
    print("The number is not even.")
print(("Even number entered: %d" % n))
