# Welcome to Mind Mesh
Mind Mesh is an app that promotes mental wellness through journaling, mood tracking, and local support resources.

## Installation
1. Create a python virtual environment
'''bash Terminal
mkdir mind-mesh
cd mind-mesh
python3 -m venv .venv
source .venv/bin/activate
'''

2. Clone the repository
'''bash Terminal
git clone https://github.com/Justcosa/Mind-Mesh.git
'''

3. Install dependencies with pip
'''bash Terminal
pip install fastapi uvicorn
pip install SQLAlchemy
pip install pydantic
pip install flet[all]
pip install requests
'''

## Operation
1. Start the fastAPI server
'''bash Terminal
python fastAPI/journalAPI.py
'''

2. Run the main.py file
'''bash Terminal
flet run main.py
'''

## Contributors
- Beloy, John Ernest M.
- Vicente, Joaquin
- Villanueva, Reema
