def validate_input(input_user):
    if not input_user.isdigit():
        print("Enter a number!")
        return False

    input_user = int(input_user)
    if input_user > 100 or input_user < 0:
        print("Enter a number between 0 and 100 ")
        return False
    
    return True

if __name__ == "__main__":
    print(validate_input('5'))