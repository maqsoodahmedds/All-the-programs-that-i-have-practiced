age = int(input("What is your age "))
country = str(input("Enter your country ")).capitalize() #capitalize means write any code it will  writtenword example PaK  
if age >=18 and country == "Pakistan":  # combine conditions
  print("Eligible voter")
else:
  print("Not Eligible voter")