print("Welcome to Tip calculator")
bill = int(input("What was your total bill : "))
tip = int(input("What percentage you would like to give as tip : "))
people = int(input("How many guys are there : "))
each_persons = ((bill * (tip / 100)) + bill) / people
print(f"Each person will get {each_persons} in their share")
