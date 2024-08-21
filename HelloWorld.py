from modules.functions import get_todos, set_todos
import time


user_prompt = "enter a todo"
todos = []

# text = "\n \
# salam be hamegi \n\
# ppyton yek zaban barname nevisi sathe bala hast \n \
# ke baraye web,application, game, ai va sakht robat \n \
# hamchnin amniat karbord dard\n \"
#
# print(text)
  
now = time.strftime("%a, %d %b %Y %H:%M:%S")
print("It is ", now)
while True:

    user_action = input("type add, show, edit, or exit: ").strip()

    if user_action.startswith("add"):
        todo =user_action[4:] + "\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        set_todos(todos, filename="todos.txt")
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for todo in todos:
            todo=todo.strip("\n")

            todos = [todo.strip("\n")for todo in todos]

        for index,todo in enumerate(todos):
            print(f"{index+1}. {todo}")
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            todos = get_todos("todos.txt")
            todos[number-1]=input("new todo: ")+"\n"

            set_todos(todos, filename="todos.txt")
        except ValueError:
            print("Please enter a integer index ")
    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])-1
            todos = get_todos("todos.txt")
            todo_to_remove=todos[number].strip("\n")
            todos.pop(number)
            set_todos(todos, filename="todos.txt")

            message = f"todo{todo_to_remove} has been removed"
            print(message)
        except IndexError:
            print("todos not found (number out of range)")
    elif user_action.startswith("exit"):
        break
    else:
        print("invalid input")

    print("done!")