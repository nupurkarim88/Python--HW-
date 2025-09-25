#START
import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits

all_characters = lower_case + upper_case + digits

password_length = 12

password = "".join(random.choice(all_characters) for i in range(password_length))

shuffled_password = "".join(random.sample(password, len(password)))

print(f"Generated Password: {shuffled_password}")
#END