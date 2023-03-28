import streamlit as st
import functions_todo

todos = functions_todo.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    # session_state is similar to dictionary contains
    # - widget values which has keys
    # it is specific for streamlit.
    # We can call it by the key of the text_input
    todos.append(todo_local)
    functions_todo.write_todos(todos)


st.title("My Todo app")
st.subheader("This is my To-do app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_todo.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="new_todo", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

