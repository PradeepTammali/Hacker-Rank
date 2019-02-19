# import math

# def is_prime(n): 
#     if n <= 1: 
#         return False
#     if n == 2: 
#         return True
#     if n > 2 and n % 2 == 0: 
#         return False
  
#     max_div = math.floor(math.sqrt(n))
#     for i in range(3, 1 + max_div, 2): 
#         if n % i == 0: 
#             return False
#     return True

# def LargestPrimeFactor(n):
#     maxPrimeFactor = 2
#     print(is_prime(6857))
#     for i in range(int(n/2)+1, 1, -1):
#         if n%i == 0 and is_prime(i):
#             print(i)
#             maxPrimeFactor = i
#             break
#     return maxPrimeFactor

num = 600851475143
i = 2
while i * i < num:
     while num % i == 0:
         num = num / i
     i = i + 1
print(num)