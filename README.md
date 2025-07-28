# Welcome to Mind Mesh
Mind Mesh is an app that promotes mental wellness through journaling, mood tracking, and local support resources.

## Installation
First, make sure you have **pip** and **git** installed to make installation easier.
Feel free to skip this step if you already have pip and git installed.
```bash
sudo apt install python3-pip
sudo apt install git
```

1. Clone the repository
```bash
git clone https://github.com/Justcosa/Mind-Mesh.git
```

2. Create a python virtual environment inside the folder
```bash Terminal
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies with pip
```bash
pip install fastapi uvicorn
pip install SQLAlchemy
pip install pydantic
pip install flet[all]
pip install requests
```

## Operation
1. Start the fastAPI server
```bash
python fastAPI/journalAPI.py
```

2. Run the main.py file
You will need to open a new terminal window to run the file.
```bash
flet run main.py
```

## Closing the app
### In both terminals press **ctrl+c** to close the FastAPI server and the app

## Contributors
- Beloy, John Ernest M.
- Vicente, Joaquin
- Villanueva, Reema
