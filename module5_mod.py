class FindNumber():
    def __init__(self, total_number):
        self.total_number = total_number
        self.get_number(total_number)
        self.data_search()

    def get_number(self, total_number):
        self.input_list = {}
        for i in range(total_number):
            get_input = input("Please input a number: ")
            self.input_list[get_input] = i+1
        return self.input_list
    
    
    def data_search(self):
        self.test_input = input("Please input the number you want to test: ")
        if self.test_input in self.input_list:
            print("I found your number! It's " + str(self.input_list[self.test_input]))
        else:
            print("This is a new number!")
            return -1
