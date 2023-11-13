import random
def generate_username(name_of_user):
    # Constraints
    minimum_capital_letter = 1
    minimum_specia_char = 2
    minimum_digits = 1
    min_len_of_username = 6
    special_chars = ['@', '#', '$', '&']

    username = ""

    name_of_user = "".join(name_of_user.split())
    name_of_user = name_of_user.lower()
    minimum_char_from_name = min_len_of_username - minimum_digits - minimum_specia_char

    temp = 0
    for i in range(random.randint(minimum_char_from_name, len(name_of_user))):
        if temp < minimum_capital_letter:
            username += name_of_user[i].upper()
            temp += 1
        else:
            username += name_of_user[i]

    temp_list = []
    for i in range(minimum_digits):
        temp_list.append(str(random.randint(0, 9)))

    for i in range(minimum_specia_char):
        temp_list.append(special_chars[random.randint(0, len(special_chars) - 1)])

    random.shuffle(temp_list)
    username += "".join(temp_list)
    print(username)

if __name__ == "__main__":
    name_of_user = "Akshay Singh"
    for i in range(8):
        generate_username(name_of_user)