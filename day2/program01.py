# # 1. enter 2 nos print subtraction  -

# n1 = int(input("enter first number"))
# n2 = int(input("enter second number"))

# total = n1 -n2

# print(f"the sum of {n1} and {n2} is {total}")


#-----------------------------------------------------------------------------------------------------------


# # 2. enter 3 nos print multiplication  *

# n1 = int(input("enter first number"))
# n2 = int(input("enter second number"))
# n3 = int(input("enter third number"))

# total = n1*n2*n3

# print(f"the multiplication of {n1} ,{n2} and {n3} is {total} ")


#-----------------------------------------------------------------------------------------------------------


# # 3. enter 2 nos print division  /

# n1 = int(input("enter first number"))
# n2 = int(input("enter second number"))

# total = n1/n2

# print(f"the division of {n1} and {n2} is {total}")


#-----------------------------------------------------------------------------------------------------------


# # 4. enter 2 nos print modulus  % this operator gives remainder 5%2=>1

# n1 = int(input("enter first number"))
# n2 = int(input("enter second number"))

# total = n1%n2

# print(f"the modulus of {n1} {n2} is {total}")


#-----------------------------------------------------------------------------------------------------------


# # 5. enter 2 nos print floor division  // this operator gives quotient

# n1 = int(input("enter first number"))
# n2 = int(input("enter second number"))

# total = n1//n2

# print(f"the floor division of {n1} and {n2} is {total}")


#-----------------------------------------------------------------------------------------------------------


# # 6. enter m and n print m to the power n  **  2**3=>8

# m = int(input("Enter m: "))
# n = int(input("Enter n: "))

# result = m ** n

# print(f"{m} to the power {n} = {result}")


#-----------------------------------------------------------------------------------------------------------


# # 7. enter marks of 5 subjects and print total and percentage

# s1 = int(input("Enter marks of Subject 1: "))
# s2 = int(input("Enter marks of Subject 2: "))
# s3 = int(input("Enter marks of Subject 3: "))
# s4 = int(input("Enter marks of Subject 4: "))
# s5 = int(input("Enter marks of Subject 5: "))

# total = s1 + s2 + s3 + s4 + s5
# percentage = (total / 500) * 100

# print(f"The total marks of 5 subjects is {total}")
# print(f"The percentage is {percentage}%")


#-----------------------------------------------------------------------------------------------------------


# # 8. enter principal, rate and time and print simple interest

# principal = float(input("Enter Principal Amount: "))
# rate = float(input("Enter Rate of Interest: "))
# time = float(input("Enter Time (in years): "))

# simple_interest = (principal * rate * time) / 100

# print(f"The principal amount is {principal}")
# print(f"The rate of interest is {rate}%")
# print(f"The time is {time} years")
# print(f"The simple interest is {simple_interest}")


#-----------------------------------------------------------------------------------------------------------


# # 9. enter temp in celsius and print in fahrenheit  (c*9/5)+32

# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9 / 5) + 32

# print(f"{celsius}°C is equal to {fahrenheit}°F")


#-----------------------------------------------------------------------------------------------------------


# # 10. enter temp in fahrenheit and print in celsius  (f-32)*5/9

# fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# celsius = (fahrenheit - 32) * 5 / 9

# print(f"{fahrenheit}°F is equal to {celsius}°C")


#-----------------------------------------------------------------------------------------------------------


# # 11. enter radius and print area of circle 3.14*r*r

# radius = float(input("Enter the radius: "))

# area = 3.14 * radius * radius

# print(f"The radius of the circle is {radius}")
# print(f"The area of the circle is {area}")


#-----------------------------------------------------------------------------------------------------------


# # 12. enter radius and print circumference of circle 2*3.14*r

# radius = float(input("Enter the radius: "))

# circumference = 2 * 3.14 * radius

# print(f"The radius of the circle is {radius}")
# print(f"The circumference of the circle is {circumference}")


#-----------------------------------------------------------------------------------------------------------


# # 13. enter length and breadth and print area of rectangle l*b

# length = float(input("Enter the length: "))
# breadth = float(input("Enter the breadth: "))

# area = length * breadth

# print(f"The length of the rectangle is {length}")
# print(f"The breadth of the rectangle is {breadth}")
# print(f"The area of the rectangle is {area}") 


#-----------------------------------------------------------------------------------------------------------


# # 14. enter basic salary of employee , calculate hra=10% of basic, da=55% of basic, pf=12% of basic and print gross salary
# #     grosssalary=basic+hra+da-pf

# basic_S = float(input("Enter the basic salary: "))

# hra = basic_S * 10 / 100
# da = basic_S * 55 / 100
# pf = basic_S * 12 / 100

# gross_salary = basic_S + hra + da - pf

# print(f"The basic salary is {basic_S}")
# print(f"The HRA is {hra}")
# print(f"The DA is {da}")
# print(f"The PF is {pf}")
# print(f"The gross salary is {gross_salary}")


#-----------------------------------------------------------------------------------------------------------


# # 15. enter 2 nos and print there value after swaping - using 3rd variable

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# temp = a
# a = b
# b = temp

# print(f"After swapping:")
# print(f"First number = {a}")
# print(f"Second number = {b}")


#-----------------------------------------------------------------------------------------------------------


# # 16. enter 2 nos and print there value after swaping - without using 3rd variable

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# a = a + b
# b = a - b
# a = a - b

# print(f"After swapping:")
# print(f"First number = {a}")
# print(f"Second number = {b}")


#-----------------------------------------------------------------------------------------------------------


# # 17. enter premium amount of rd and print maturity amount 
# # Rule:
# # 1. RD open for 5 years
# # 2. minimum amount of rd premium inr 5/- per month 
# # 3. max no limit but 5*?

# premium_A = float(input("Enter monthly RD premium: "))

# rate = 340.27 / 5                
# maturity = premium_A * rates


# print(f"The monthly premium is {premium_A}")
# print(f"The maturity amount is {maturity:.2f}")
