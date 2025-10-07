class Person:
    name = "John"
    occupation = "Developer"
    network = "LinkedIn"
    location = "New York"
    def info(self):
        print(f"{self.name} is a {self.occupation} on {self.network} located in {self.location}")


a = Person()
# print(a.name)
# print(a.occupation)
# print(a.network)

a.name = "Alice"
a.occupation = "Designer"
a.network = "Twitter"
# print(a.name)
# print(a.occupation) 
# print(a.network)
a.info()