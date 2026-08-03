# Commands I've Used — W3 A2

## Environment
source venv/bin/activate       # activate the virtual environment
                                 # (look for "(venv)" at the start of your prompt to confirm)

## Running the server
uvicorn main:app --reload       # start FastAPI server, auto-reloads on file changes

## File management
rm task.db                      # delete a file (permanent, no undo)
mv task.db task.db.bak          # rename/move a file (safer alternative to rm)
touch NOTES.md                  # create an empty file

## Checking the database (sqlite3 CLI)
sqlite3 tasks.db ".tables"              # list tables in the database
sqlite3 tasks.db ".schema tasks"        # show the CREATE TABLE structure of a table
sqlite3 tasks.db "SELECT * FROM tasks"  # show all rows in the tasks table
sqlite3 tasks.db "SELECT COUNT(*) FROM tasks"  # count rows in the table

## Installing tools
sudo apt install sqlite3        # install sqlite3 CLI if not already present

## Git
git status                              # check what's staged/unstaged/clean
git ls-files | grep -E "venv|tasks.db"  # check if a file/folder is tracked by git
git rm --cached tasks.db                # stop tracking a file, but keep it on disk
git add .gitignore
git add .
git commit -m "message here"
git push
git pull origin main --rebase           # pull remote changes, replay local commits on top
                                          # (use when push is rejected due to remote history)
