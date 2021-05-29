import requests as request
from random import randint
import os
from pickle import dump, load

class RandomQuote:
    def __init__(self):
        self.quote = ""
        self.author = ""
        self.apiUrl = "https://type.fit/api/quotes"
        self.data = []

        self.saveResponse()

    def saveResponse(self):
        file_name = "data"
        if not os.path.isfile(file_name):
            get_data = request.get(url = self.apiUrl)
            get_data = get_data.json()

            self.data = get_data
            final_data = (get_data)

            with open(file_name, "ab") as data_file:
                dump(final_data, data_file)
        
        else:
            with (open(file_name, "rb")) as data_file:
                while True:
                    try:
                        self.data = (load(data_file))
                        print(load(data_file))
                    except EOFError:
                        break

    def setQuote(self):
        get_random_quote = randint(0, len(self.data) - 1)
        self.author = self.data[get_random_quote]["author"]
        self.quote = self.data[get_random_quote]["text"]
    
    def start(self):
        self.setQuote()
        print('{} \n-- {}'.format(self.quote, self.author))
        
        
if __name__ == "__main__":
    app = RandomQuote()
    app.start()

