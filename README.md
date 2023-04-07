# FileManagementUtility
This is a command-line utility that allows users to manage documents in a file-like system stored in memory. The utility supports the following features:
<ol>
<li>Adding a document at a particular path</li>
<li>Searching for a document with a full path or path prefix</li>
<li>Deleting a document at a particular path</li>
<li>Autocomplete for paths</li>
<li>Tab-completion for paths</li>
  </ol>
  
## Requirements
<ul>
<li>Python 3.x</li>
  </ul>
  
## Installation
1. Clone the repository: `git clone https://github.com/(username)/(repository).git`
2. Navigate to the project directory: `cd (repository)`
3. Install the required dependencies: `pip install -r requirements.txt`
  
## Usage
To run the utility, use the following command:
`python file_management.py`

The utility will ask for input according to the supported features. The following are examples of usage:
- Adding a document:
  ```bash
  Enter command: add /path/to/document.txt
  Document added successfully
  ```
- Searching for a document:
  ```bash 
  Enter command: search /path/to
  Matching documents:
  /path/to/document.txt
  ```
- Deleting a document:
   ```bash
   Enter command: delete /path/to/document.txt
   Document deleted successfully
   ```
- Autocomplete:
  ```bash
  Enter command: /m
  Suggested paths:
  /my_documents
  /my_files
  ```
- Tab-completion:
  ```bash
  Enter command: /my_d<tab>
  ```
  
  ### That's All from this project.
  ## THANK YOU
