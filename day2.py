print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? \n$"))
people = float(input("How many people to split the bill ?\n"))
tip = int(input("What percentage tip would you like to give? 10 , 12 or 15?\n"))
print("Each person should pay: $" , round(((((bill*tip)/100)+bill)/people),2))