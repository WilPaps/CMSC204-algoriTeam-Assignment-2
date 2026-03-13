def get_student_number():
    while True:
        student_number = input("Enter student number: ").strip()
        cleaned = student_number.replace(" ","").replace("-","")

        if not cleaned.isdigit():
            print("Invalid input. Student number must contain digits only.")
            continue

        if len(cleaned) != 9:
            print("Invalid input. Student number must contain exactly 9 digits.")
            continue

        return cleaned
    
def get_surname():
    while True:
        surname = input("Enter surname: ").strip()

        if not surname.isalpha():
            print("Invalid input. Surname must contain letters only.")

        return surname
        
def generate_keys(student_number, surname):
    last_seven_digits = student_number[-7:]
    keys = [int(digit) for digit in last_seven_digits]

    truncated_surname = surname[:9]
    surname_length = len(truncated_surname)

    keys.append(surname_length)
        
    return keys
    
def get_student_keys():
    student_number = get_student_number()
    surname = get_surname()

    keys = generate_keys(student_number, surname)

    print("\nGenerated key set: ", keys)
    print("-" * 50)

    return keys 