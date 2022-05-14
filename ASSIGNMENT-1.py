# 1 Write a Python program to get the Fibonacci series between 0 to 50

# def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n> 2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1,10):
#     print(n,":",fibonacci(n)) 



# 2 Write a Python program that accepts a word from the user and reverse it.

# word = input("Input a word or sentence to reverse: ")	
# for char in range(len(word) - 1, -1, -1):
# 	  print(word[char], end="")
# print("\n")


# 3  Write a Python program to count the number of even and odd numbers from a series of numbers.


# NumList = []
# Even_count = 0
# Odd_count = 0

# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)

# for j in range(Number):
#     if(NumList[j] % 2 == 0):
#         Even_count = Even_count + 1
#     else:
#         Odd_count = Odd_count + 1

# print("\nTotal Number of Even Numbers in this List =  ", Even_count)
# print("Total Number of Odd Numbers in this List = ", Odd_count)

