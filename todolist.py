# python learning day 1
"""
print("python learning todolist.py")

name = input("Enter your name:")
task1 = input("Enter that you want to do:")
task2 = input("Enter that you want to do next:")
tastk3 = input("Enter that you want to do last:")

print("------------------todo list------------------")
print("Name:", name)
print("Task:",task)
print(name+"have a good day finishing up "+ task1+","+task2+" and  "+task3)
print("---------------------------------------------")

print("what is the most important task?")
priority = input("tell me:")
print("Do it fast as you can !"+priority)
"""

#day 2
print("python learning day 2")

tasks = []

print("Enter the tasks you have to do today: (press enter to stop)\n")

while True:
    task = input("Task: ")
    
    if task == "":
        break 
    tasks.append(task)

print ("\n Your To-Do list for today is:\n")

for i,t in enumerate(tasks):
    print(f"{i+1}. {t}")
print ("---------------------------------------------")
print ("\n The number of tasks you have today is:" + str(len(tasks)))
