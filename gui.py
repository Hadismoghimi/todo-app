import modules.functions as functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip=' Enter a to-do', key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")
sg.theme('Black')
window = sg.Window('My To-Do App',
                   layout = [
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button],
                   ],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values["todo"]+"\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window['todos'].Update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]+"\n"
            print(todo_to_edit, new_todo)
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.set_todos(todos)
            window['todos'].Update(values=todos)
        case "todos":
            window['todo'].Update(value=values["todos"][0])
        case 'Complete':
             todo_to_complete = values["todos"]
             functions.get_todos()
             todos.remove(todo_to_complete)
             functions.set_todos(todos)
             window['todos'].Update(values=todos)
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            exit()


window.close()