class User: 
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def welcome(self): 
        print(f"Welcome {self.name}, you were born during the {self.century()} century")

    def century(self):
        if self.year_of_birth < 2000:
            return "20th"
        else:
            return "21st"

dolly = User("Dolly", 2001)
martha = User("Martha", 1956)
print(dolly.welcome())
print(martha.welcome())
