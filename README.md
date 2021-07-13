# library-api

The goal is to build a small API to manage a library, with users borrowing books.

You can choose to code it with Python or PHP.

## Excercise

Take a look to the `data.json` file. You'll see two kinds of entities.

**User**

- id
- name

**Book**

- id
- title
- author

Create endpoints to list books and users.  
All endpoints input and output must be in JSON.

- List users
  - Sort by name
- List books
  - Sort by author or title
  - Search by author or title

Update the model to allow users to borrow a book.

- Create the loan model
- Add some loans in the `data.json` file
- Create an endpoint to list loans
  - Get all books borrowed by a user
  - Get all users who are currently borrowing a book
- Add endpoint to add and remove loans, and persist those changes in the `data.json` file.

## Bonus

Here are some improvements if you have remaining time. **They are not mandatory** but will be appreciated.

- Feel free to do anything you want...
- Use git and commit your progress.
- Replace JSON storage by SQLite storage.
- Add authentication on your endpoints.
- Write tests.

## Project setup

For each language, a branch with a small boilerplate is provided to quickly start the project.
Check `README.md` on the branch to see how to install and run it.
