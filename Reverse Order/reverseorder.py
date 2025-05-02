#START
num = int(input("Enter a number: "))
num = abs(num)
count = 0
while num > 0:
    count += 1
    num //= 10 
if count == 0:
    count = 1
print("Total digits in the number:", count)
#END