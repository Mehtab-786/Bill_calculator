print("Welcome to Tip calculator\n")

bill = int(input("What was your total bill : "))
tip = int(input("What percentage you would like to give as tip : "))
people = int(input("How many guys are there : "))

share = ((bill * (tip / 100)) + bill) / people

# "%.2f"  is used for only 2 number after decimal points

print(f"Each person will get ${'%.2f' % share} in their share")
