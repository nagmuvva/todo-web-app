import streamlit as st
import modules.functions as functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.save_todos(todos)


st.set_page_config(layout="wide")

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is to increase your <b>productivity</b>.", unsafe_allow_html=True)
st.write("Select to delete")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo", )
