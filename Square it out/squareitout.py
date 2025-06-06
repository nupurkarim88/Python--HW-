#START
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
# Create a list for squares
squares = []
for num in range(start, end + 1):
    squares.append(num * num)
print("Squares list:", squares)
even_squares = []
odd_squares = []
for sq in squares:
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Showing the final result
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
#END
