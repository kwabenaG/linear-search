# linear search algorithm

""" the program does a simple linear search and returns its index  [position].. It gives two chances thanks"""


class Search:
    list_arr = [100, 200, 300, 400, 500, 600,  700, 900, 1000, 1900, 9000]  # example of list values

    def __init__(self):
        self.numbers = Search.list_arr  # initializes the list_arr declared above

    def search_index(self):
        length = len(self.numbers)  # gets the length of the list

        print('The available List to pick from '.format(0), self.numbers) # prints out the instructions to the user

        user = int(input("Input Any Value: ")) # gets user input and cast value to an integer

        for i in range(0, length):  # runs the for loop to determine the number index
            if self.numbers[i] == user:
                return i
        return -1

    def results(self): # method responsible for calling search_index method
        results = self.search_index()  # assigns results to the above (search_index) method
        if results == -1:
            print('Out of context, Number not found')  # print value based on eval
            second_chance = input('Do you want to try again? [yes], [y], [YES]')  # second chance for indexing
            if second_chance == 'yes' or 'y' or 'YES':
                second_value = self.search_index()
                if second_value == -1:
                    print('Out of context, Number not found, Thanks')
                else:
                    print('Number typed has an index of'.format(0), results,
                          'Great Search...', )  # print value based on eval
            else:
                exit()
        else:
            print('Number typed has an index of'.format(0), results, 'Great Search...',)  # print value based on eval


callsearch = Search()  # object instance created
callsearch.results()   # called the results method..

# thanks.. this algorithm work for linear search.



