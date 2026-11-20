# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 1 (Create a class name Calculator)
# Score: Submitted (Evaluation Completed)
# Synced: Friday, November 20, 2026 at 9:32 AM

class calculator:
    def add(self,a,b):
        print(f"the additon of {a} & {b} is",{a+b})
    def sub(self,a,b):
        print(f"the subtractiton of {a} & {b} is",{a+b})
    def multi(self,a,b):
        print(f"the multiplication of {a} & {b} is",{a+b})
    def divide(self,a,b):
        print(f"the division of {a} & {b} is",{a+b})
obj =calculator()
obj.add(4,5)
obj.sub(0,5)
obj.multi(90,5)
obj.divide(50,5)