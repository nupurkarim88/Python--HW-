#START
def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
my_tuple = (2, 3, 4)
result = tuple_product(my_tuple)
print(f"The product of {my_tuple} is {result}")
#END