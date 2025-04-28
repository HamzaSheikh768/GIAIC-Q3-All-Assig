import streamlit as st
import json

# ========================== Load Library from File =============================
def load_library():
    """
    This function loads the library data from the 'library.json' file.
    If the file does not exist, it returns an empty list.
    """
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# ========================== Save Library to File =============================
def save_library():
    """
    This function saves the current state of the library to 'library.json'.
    """
    with open("library.json", "w") as file:
        json.dump(library, file)

# ========================== Initialize Library =============================
library = load_library()

# ========================== Streamlit App UI =============================
st.title("📚 Personal Library Manager By Muhammad Faizna...📖")
st.write("Manage your personal book collection easily! 📔")

#................................... Sidebar menu options
menu = st.sidebar.selectbox("📌 Select an Option", [
    "Add a Book 🆕", 
    "Remove a Book ❌", 
    "Search a Book 🔍", 
    "Display All Books 📖", 
    "View Library 📊", 
    "Save & Exit 💾"
])

# ========================== Add a Book =============================
if menu == "Add a Book 🆕":
    st.header("📚 Add a New Book")
    
    #................................. Input fields for book details
    title = st.text_input("📖 Enter Book Title")
    author = st.text_input("✍️ Enter Author Name")
    year = st.number_input("📅 Enter Publication Year", min_value=2020, max_value=2050, step=1)
    genre = st.text_input("📂 Enter Genre")
    read_status = st.checkbox("✅ Mark as Read")
    
    if st.button("➕ Add Book"):
        #............................. Adding book details to the library
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
        save_library()  # Save updated library
        st.success("✅ Book Added Successfully!")

# ========================== Remove a Book =============================
elif menu == "Remove a Book ❌":
    st.header("🗑️ Remove a Book")
    
    book_titles = [book["title"] for book in library]  # Get list of book titles
    
    if book_titles:
        selected_book = st.selectbox("📖 Select a book to remove", book_titles, key="remove_book")
        
        if st.button("❌ Remove Book"):
            #......................Removing selected book from the library
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("🚀 Book Removed Successfully! 📖")
            st.rerun()
    else:
        st.warning("📭 No books available to remove!")

# ========================== Search for a Book =============================
elif menu == "Search a Book 🔍":
    st.header("🔍 Search for a Book")
    search_term = st.text_input("🔎 Enter title or author name to search")
    
    if st.button("🔍 Search"):
        #..........................Searching for books by title or author
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        
        if results:
            st.write("🎯 Matching Books:")
            st.table(results)
        else:
            st.warning("❌ No books found with this search term!")

# ========================== Display All Books =============================
elif menu == "Display All Books 📖":
    st.header("📖 Your Library")
    
    #.............................Display library as a table
    if library:
        st.table(library)  
    else:
        st.warning("📭 Your library is empty! Start adding books! 📚")

# ========================== View Library Statistics =============================
elif menu == "View Library 📊":
    st.header("📊 Library Statistics")
    
    #.............................Total number of books
    total_books = len(library)  
    books_read = sum(1 for book in library if book["read"])  # Count of read books
    percentage_read = (books_read / total_books * 100) if total_books > 0 else 0  # Read percentage
    
    # ............................Display statistics
    st.write(f"📚 Total Books: {total_books}")
    st.write(f"✅ Books Read: {books_read}")
    st.write(f"📊 Percentage Read: {percentage_read:.2f}%")

# ========================== Save & Exit =============================
elif menu == "Save & Exit 💾":
    st.success("💾 Library Saved! Exiting... 👋")
