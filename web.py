import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todoo = st.session_state["new_todo"] + "\n"
    todos.append(todoo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')