# Crumb-Packer
This Python script provides a command-line interface (CLI) using curses to manage system packages and Python modules conveniently. It allows you to update package lists, upgrade packages, install programming languages, and install a comprehensive list of Python modules.


## Features

- Update Package List: Updates the system's package list using sudo apt update.
  
- Upgrade Packages: Upgrades all installed packages using sudo apt upgrade -y.
  
- Upgrade Pip: Upgrades pip to the latest version using pip install --upgrade pip.
  
- Install Languages: Installs a variety of programming languages like Python, Java, C/C++, Ruby, and more.
  
- Install Pip Modules: Installs numerous Python modules, including data science libraries (NumPy, Pandas), web frameworks (Django, Flask), machine learning frameworks (TensorFlow, PyTorch), and many others.
  
- Exit: Quits the script.

## Requirements

```
> Python 3
> pip (Python's package installer)
> curses library (usually included in Python standard library)
> pyfiglet library for ASCII art text rendering
```

## Installation

1. Clone the repository

```
git clone https://github.com/Cr0mb/Crumb-Packer.git
cd Crumb-Packer
```
2. Run the script
```
python install.py
```

### Usage

Use the arrow keys to navigate through the menu.

Press Enter to select an action.

Follow the prompts to update package lists, upgrade packages, install languages, or install Python modules.

### Notes

> Ensure you have appropriate permissions to execute system-level commands (sudo).

> Some actions may require administrative privileges (sudo).

> Logs for any errors encountered during command execution are stored in logs.txt.
