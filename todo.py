print ("Welcome to our ToDo task managment program.")
todo_dict = {}

while True:
  task = input("Please enter your ToDo task: ")
  status = input("Is your task completed? (y/n) ")
  print ("Your task is " + task)

  if status == "yes" or status == "y":
    todo_dict[task] = True
  else:
    todo_dict[task] = False

  new = input("Would you like another task? (y/n) ")
  if new == "no" or new == "n":
    break

todo_file = open("todo.txt", "w+")

print ("Completed tasks: ")
todo_file.write("Completed tasks:\n")
for items in todo_dict:
  if todo_dict[items] is True:
    print ("- " + items)
    todo_file.write("- " + items + "\n")

todo_file.write("\n")

print ("Incompleted tasks: ")
todo_file.write("Incompleted tasks:\n")
for items in todo_dict:
  if todo_dict[items] is False:
    print ("- " + items)
    todo_file.write("- " + items + "\n")

todo_file.close()

print ("END")