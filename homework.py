while True:
    try:
        bill = float(input("Enter the bill amount: "))
        discount = float(input("Enter the discount percentage: "))
        person = int(input("Enter how many people there is: "))

        final = bill - (bill * discount / 100)
        print(f"final bill is: {final}")
        print(f"each pays: {final / person}")
        break
    except:
        print("Invalid input, please try again.")
