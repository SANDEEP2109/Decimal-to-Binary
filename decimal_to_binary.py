def decimal_to_binary(n):
    return  format(n, 'b')

while True:
    print("1) decimal to binary")
    print("2) Exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        decimal_number = int(input("Enter your number: "))
        binary_number = decimal_to_binary(decimal_number)
        print(f"The decimal number {decimal_number} into binary number is {binary_number}")
    elif choice == 2:
        break
    else:
        print("Invalid option")