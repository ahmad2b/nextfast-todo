import streamlit as st
import requests

# Set the API URL
API_URL = "http://localhost:8000/todos"

# Create a form for creating todos in the sidebar
with st.sidebar.form(key="create_form"):
    st.subheader("Create Todo")
    title = st.text_input("Title")
    description = st.text_input("Description")
    submit_button = st.form_submit_button(label="Create")
    if submit_button:
        response = requests.post(
            API_URL, json={"title": title, "description": description}
        )
        if response.status_code == 201:
            st.success("Todo created successfully")
            st.balloons()
        else:
            st.error("Error: Could not create todo")


# List all todos in the main space
st.subheader("List of Todos")
response = requests.get(API_URL)
if response.status_code == 200:
    todos = response.json()
    todos.sort(key=lambda x: x["id"], reverse=True)

    for todo in todos:
        with st.form(key=f"{todo['id']}"):
            st.write(f"ID: {todo['id']}")
            title = st.text_input("Title", value=todo["title"])
            description = st.text_input("Description", value=todo["description"])
            completed = st.checkbox("Completed", value=todo["completed"])
            update_button = st.form_submit_button(label="Update")

            if update_button:
                response = requests.put(
                    f"{API_URL}/{todo['id']}",
                    json={
                        "title": title,
                        "description": description,
                        "completed": completed,
                    },
                )
                if response.status_code == 200:
                    st.success("Todo updated successfully")
                else:
                    st.error("Error: Could not update todo")

        delete_button = st.button("Delete", key=f"delete_{todo['id']}")
        if delete_button:
            response = requests.delete(f"{API_URL}/{todo['id']}")
            if response.status_code == 204:
                st.info("Todo deleted successfully")
            else:
                st.error("Error: Could not delete todo")
        st.write("---")
else:
    st.write("Error: Could not fetch todos")
