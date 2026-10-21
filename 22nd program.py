age = int(input("Enter your age:"))
country = str(input("Enter your country:"))
if age >=18:
   if country == "Pakistan":
    print("You can vote  in Pakistan")  # nested if condition
   else:
    print("You can not vote in pakistan")
else:
  print("You can not vote")

