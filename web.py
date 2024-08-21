import streamlit as st
import modules.functions as functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo+"\n")
    functions.set_todos(todos)


def remove_todo(todo):
    todos.remove(todo)
    functions.set_todos(todos)
    st.rerun()


st.title("My Todo app")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivibty.")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=f"checkbok_{index}")
    if checkbox:
        remove_todo(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")                    






































































































































































