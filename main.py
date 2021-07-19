print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")




combined_name= name1 + name2
lower_case_name= combined_name.lower()

####  true Love
a=lower_case_name.count("t")
b=lower_case_name.count("r")
c=lower_case_name.count("u")
d=lower_case_name.count("e")

first_digit= a+b+c+d

f=lower_case_name.count("l")
g=lower_case_name.count("o")
h=lower_case_name.count("v")
i=lower_case_name.count("e")

second_digit= f+g+h+i

score = int(str(first_digit) + str(second_digit))

if score<10 or score> 90:
  print(f"Your score is {score}, you go together like coke and menthos.")

if score >=40 and score <=50:
  print(f"Your score is {score}, you are alright together. ")

else:
  print(f"Your score is {score}")


  
 

