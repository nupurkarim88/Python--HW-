#START
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [n**2 for n in nums]
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]

print("Squares:", squares)
print("Evens:", evens)
print("Odds:", odds)
#END