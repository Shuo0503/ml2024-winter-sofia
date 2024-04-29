def input_number_test ():
    input_list = {}
    get_number = int(input("Please input the amount of numbers you will provide later: "))
    
    for i in range(get_number):
        get_input = input("Please input a number: ")
        input_list[get_input] = i+1

    test_input = input("Please input the number you want to test: ")

    if test_input in input_list:
        print("I found your number! It's " + str(input_list[test_input]))
    else:
        print("This is a new number!")
        return -1

input_number_test()
