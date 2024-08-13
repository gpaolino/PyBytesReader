# PyBytesReader
Simple file reader in Python3

## pybytesreader-project setup!

### Windows OS
Prerequisites: Windows 10 (or higher) with Python v3.12 properly installed, don't forget to add Python to the PATH variable. <br/>
You can check the Python version installed running this command: <br/>

    $> py --version

Depending on how the environment variable is set it could be: "py", "python" or "python3" <br/>

Once you have done that, you can clone this repository in your local environment: <br/>

    $> git clone https://github.com/gpaolino/pybytesreader.git

In order to run this project, you need to create a virtual environment and populate it with the dependencies listed in requirements.txt <br/>
Run these commands to get started quickly: <br/>

    $> cd .\pybytesreader\
    $> py -m venv .venv
    $> .\\.venv\Scripts\activate

Optionally upgrade pip package manager: 

    $> python.exe -m pip install --upgrade pip

Install all the dependencies:

    $> python -m pip install -r requirements.txt

### Install PyBytesReader as a Local Package
Navigate to the src directory and install your local package: <br/>

    (.venv)$> cd .\src\
    (.venv)$> python -m pip install .

Run the program: <br/>

    (.venv)$> python pybytesreader

### Build PyBytesReader in an executable file
Usinng pyinstaller you can create a .exe file for the application. <br/>
Navigate to the project directory and build your executable file: <br/>

    (.venv)$> cd ..
    (.venv)$> pyinstaller .\src\pybytesreader\__main__.py --onefile --name "PyBytesReader"
