try:
    a = int(input("Enter a number: "))

    print(a + 3)
except Exception as e:
    print(f"Please enter a valid number \n{e}")
