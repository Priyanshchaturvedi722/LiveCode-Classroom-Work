# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 2 (Create a Classs)
# Score: 1/1 (4/4 Test Cases Passed)
# Synced: Thursday, November 26, 2026 at 9:47 AM

class car:
    def __init__(self,name,model,price):
        self.name =name
        self.model =model
        self.price=price
    def details(self):
        print(f"the name of car is: {self.name}")
        print(f"the model of car is: {self.model}")
        print(f"the price of car is: {self.price}")

obj1=car("thar",2022,400000)
obj1.details()

