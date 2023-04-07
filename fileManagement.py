import os
import readline

# Create a dictionary to hold the documents
documents = {}

# Function to add a document at a particular path
def add_document(path, content):
    documents[path] = content
    print(f"Added document at path {path}")

# Function to search for a document with the full path or for documents with a path prefix
def search_document(path):
    matching_documents = {}
    for document_path, content in documents.items():
        if document_path == path:
            matching_documents[document_path] = content
        elif document_path.startswith(path + "/"):
            matching_documents[document_path] = content
    if matching_documents:
        print("Matching documents found:")
        for document_path, content in matching_documents.items():
            print(f"{document_path}: {content}")
    else:
        print("No matching documents found.")

# Function to delete a document at a particular path
def delete_document(path):
    if path in documents:
        del documents[path]
        print(f"Deleted document at path {path}")
    else:
        print("No document found at that path.")

# Command line interface
def main():
    while True:
        # Use readline to enable tab completion
        readline.set_completer_delims("\t")
        readline.parse_and_bind("tab: complete")
        readline.set_completer(lambda text, state: autocomplete(text, state, documents))

        # Ask for user input
        command = input("Enter command (add, search, delete, exit): ")
        if command == "add":
            path = input("Enter path: ")
            content = input("Enter content: ")
            add_document(path, content)
        elif command == "search":
            path = input("Enter path: ")
            search_document(path)
        elif command == "delete":
            path = input("Enter path: ")
            delete_document(path)
        elif command == "exit":
            break
        else:
            print("Invalid command.")

# Function for tab completion
def autocomplete(text, state, documents):
    options = [path for path in documents.keys() if path.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

if __name__ == "__main__":
    main()
