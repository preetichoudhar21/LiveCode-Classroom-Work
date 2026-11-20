# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 2 (Solve the error)
# Score: Submitted (Evaluation Completed)
# Synced: Friday, November 20, 2026 at 10:02 AM

# Write your Python solution below
class student:
    def __init__(self,name):
        self.name=name
    def greet(self):
          print(f"Hello {self.name} how are you!!")
obj1 = student("shyam")
obj2= student("ram")
obj1.greet()