# #Q1. enter marks of 5 subjects print total and percentage and Division Merit, First , Second, Third, Fail

# S1 = int(input("Enter marks of subject 1: "))
# S2 = int(input("Enter marks of subject 2: "))
# S3 = int(input("Enter marks of subject 3: "))
# S4 = int(input("Enter marks of subject 4: "))
# S5 = int(input("Enter marks of subject 5: "))

# total = S1 + S2 + S3 + S4 + S5
# percentage = total / 5

# print(f"Total marks: {total}")
# print(f"Percentage: {percentage}")

# if percentage >= 80:
#     print("Division: Merit")
# elif percentage >= 70:
#     print("Division: First")
# elif percentage >= 60:
#     print("Division: Second")
# elif percentage >= 50:
#     print("Division: Third")
# else:
#     print("Division: Fail")


#-------------------------------------------------------------------------------------------------------------



# #Q2. In your factory workers come to work on daily wage Your factory Rate Chart Working Hour Wage 8 250/- >8 and <=10 50/- hr >10 and <=12 75/- hr >12 and <=14 100/- hr other invalid working hour

# WH = int(input("Enter working hours: "))

# if WH ==8:
#     wage = 250
#     print(f"Wage for {WH} hours is : {wage}/-")
# elif WH > 8 and WH <= 10:
#     wage = 250 + (WH - 8) * 50
#     print(f"Wage for {WH} hours is : {wage}/-")
# elif WH > 10 and WH <= 12:
#     wage = 250 + 2 * 50 + (WH - 10) * 75
#     print(f"Wage for {WH} hours is : {wage}/-")
# elif WH > 12 and WH <= 14:
#     wage = 250 + 2 * 50 + 2 * 75 + (WH - 14) * 100
#     print(f"Wage for {WH} hours is : {wage}/-")
# else:
#     print("Invalid working hour ")



#--------------------------------------------------------------------------------------------------------------


# ITR slab for income tax calculation
# 0-4 lac         0%
# >4 upto 8       5%
# >8 upto 12      10%
# >12 upto 16     15%
# >16 upto 20     20%
# >20 upto ...    25%


income = float(input("Enter your income in lakhs: "))

if income <= 400000:
    tax = 0 
    print(f"Tax for income {income} lakhs is : {tax}")

elif income > 400000 and income <= 800000:
    tax = (income - 400000) * 0.05               # isme total 4 lac ka tax 20000 hh
    print(f"Tax for income {income} lakhs is : {tax} ")

elif income > 800000 and income <= 1200000:
    tax = (income - 800000) * 0.10 + 20000        # isme total 8 lac ka tax 40000 hh 
    print(f"Tax for income {income} lakhs is : {tax} ")

elif income > 1200000 and income <= 1600000:
    tax = (income - 1200000) * 0.15 + 60000       # isme total 12 lac ka tax 60000 hh 
    print(f"Tax for income {income} lakhs is : {tax} ")

elif income > 1600000 and income <= 2000000:
    tax = (income - 1600000) * 0.20 + 120000      # isme total 16 lac ka tax 80000 hh 
    print(f"Tax for income {income} lakhs is : {tax} ")

elif income > 2000000:
    tax = (income - 2000000) * 0.25 + 200000      # isme total 20 lac ka tax 160000 hh 
    print(f"Tax for income {income} lakhs is : {tax} ")

else:
    print("Invalid income")
