# # enter a number and count its digits

# num=int(input("Enter a number: "))
# x=0
# while num>0:
#     x=x+1
#     num=num//10
# print("Number of digits:",x)


#----------------------------------------------------------------------------------------------------------------


# #1. enter a number and print sum of its digits

# num = int(input("Enter a number: "))

# i=0
# sum=0

# while num>0:
#     sum = sum + num%10
#     num = num//10
#     i = i + 1

# print(f"Sum of digits is {sum}")


#----------------------------------------------------------------------------------------------------------------


# #2. enter a number and print reverse of the number


# num=int(input("Enter a number: "))

# i=0
# rev=0

# while num>0:
#     rev = rev*10 + num%10
#     num = num//10
#     i = i + 1
    
# print(f"Reverse of the number is {rev}")


#----------------------------------------------------------------------------------------------------------------


# #3. enter a number and print its palindrome or not
# # ex : 121 -> 121 is a palindrome
 
# num=int(input("Enter a number: "))
# original=num
# rev=0

# while num>0:
#     rev = rev*10 + num%10
#     num = num//10

# if original==rev:
#     print(f"{original} is a palindrome")
# else:
#     print(f"{original} is not a palindrome")


#----------------------------------------------------------------------------------------------------------------


# #4. enter a number and print its Armstrong or not
# # ex: 153 -> 1^3 + 5^3 + 3^3 = 153 is an Armstrong number

# num = int(input("Enter a number: "))
# original = num
# sum = 0
# while num > 0:
#     digit = num % 10x 
#     sum += digit ** 3
#     num //= 10

# if original == sum:
#     print(f"{original} is an Armstrong number")
# else:
#     print(f"{original} is not an Armstrong number")


#----------------------------------------------------------------------------------------------------------------


# #5. enter and number and print its binary equivalent

# num = int(input("Enter a number: "))

# binary = 0
# i=1

# while num > 0:
#     binary = binary + (num % 2) * i
#     num = num // 2
#     i = i * 10
# print(f"Binary equivalent is {binary}")


#----------------------------------------------------------------------------------------------------------------


# #6. enter a number and print it in words

words = ["Zero", "One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"]
num = int(input("Enter a number: "))

rev = 0
  
while num > 0:                                   # Reverse the number
    rev = rev * 10 + num % 10                  
    num = num // 10
 
while rev > 0:                                                      
    digit = rev % 10                                                             
    print(words[digit], end=" ")                                                      
    rev = rev // 10