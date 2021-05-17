print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("enter the age"))
bill=0
if height>=120:
  print("woah!you can ride the roller coaster")
  if age<=12:
    bill=5
    print("pay $5")
  elif age>12 and age<18:
    bill=7
    print("pay $7")
  elif age>=18 and age<45:
    bill=12
    print("pay $12")
  elif age>=45 and age<=55:
    bill=0
    print("free ticket")
  photos=input("do you want photos?Y or N  ")
  if photos=="Y":
    bill+=3
    print("pay extra $3")
    print("your total amount is ",bill)
  else:
    print("your total amount is ",bill)


else:
  print("sorry!you have to grow taller")