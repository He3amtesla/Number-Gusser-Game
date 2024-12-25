
def give_user_hint(random_number, input_user):
    if random_number < input_user:
        print("The number you considered is higher than that number")
        return True    
        
    elif random_number > input_user:
        print("The number you considered is less than this number")
        return True


if __name__ == '__main__':
    give_user_hint(50, 40)