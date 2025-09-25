#START
test_dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Here's the test dictionary:", test_dictionary)
value_to_check = int(input("Enter the value you want to check the frequency of: "))
frequency = list(test_dictionary.values()).count(value_to_check)
print(f"The frequency of value '{value_to_check}' is: {frequency}")
#END