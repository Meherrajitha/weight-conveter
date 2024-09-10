def weight_converter():
    print("Weight Converter")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        grams = float(input("Enter weight in grams: "))
        kilograms = grams / 1000
        print(f"{grams} grams is equal to {kilograms} kilograms")

    elif choice == 2:
        kilograms = float(input("Enter weight in kilograms: "))
        grams = kilograms * 1000
        print(f"{kilograms} kilograms is equal to {grams} grams")

    elif choice == 3:
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds * 0.453592
        print(f"{pounds} pounds is equal to {kilograms} kilograms")

    elif choice == 4:
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is equal to {pounds} pounds")

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

weight_converter()

