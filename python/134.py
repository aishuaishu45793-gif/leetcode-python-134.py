try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    target = int(input("Enter the number to count: "))

    frequency = numbers.count(target)

    print("Frequency of", target, ":", frequency)

except ValueError:
    print("Invalid input! Please enter integers only.")