import streamlit as st
import functions

# session state capthers the value from the input box
# session state is kind of dictionary
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("this app is to *increase* your productivity")

todos = functions.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # down below wasnt explained well
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

#place holder has same function as tool tip
st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")


st.session_state
#try this and seey our browser to understan how session state and key, value works