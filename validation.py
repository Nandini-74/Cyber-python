import re

def validate_phone_number(phone):
    pattern = r'^[0-9]{10}$'
    return bool(re.match(pattern, phone))

def validate_emali(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def main():
    phone_number = input()
    email = input()

    is_phone_vaild = validate_phone_number(phone_number)
    is_email_valid = validate_email(email)

    if is_phone_valid and is_email_valid:
        print("Both are valid")
    elif is_phone_valid and not is_email_valid:
        print("Phone number is valid, but the email is not valid")
    elif not is_phone_valid and is_email_valid:
        print("Email is valid, but the phone number is not valid")
    else:
        print("Both are invalid")

if __name__ == "__main__":
    main()
