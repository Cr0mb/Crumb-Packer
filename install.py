import curses
import subprocess
import shutil  # For terminal size detection

try:
    import pyfiglet
except ImportError:
    print("pyfiglet not found. Installing...")
    subprocess.run(['pip', 'install', 'pyfiglet'], check=True)
    print("pyfiglet has been installed.")
    import pyfiglet


def run_command(command):
    try:
        subprocess.run(command, shell=True, stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError as e:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error executing command '{command}': {e}\n")


def install_languages():
    languages = [
        'sudo apt install -y python3',
        'sudo apt install -y python3-pip',
        'sudo apt install -y default-jdk',
        'sudo apt install -y gcc',
        'sudo apt install -y g++',
        'sudo apt install -y ruby',
        'sudo apt install -y nodejs',
        'sudo apt install -y rustc',
        'sudo apt install -y golang-go',
        'sudo apt install -y php',
        'sudo apt install -y perl',
        'sudo apt install -y lua5.3',
        'sudo apt install -y openjdk-11-jre',
        'sudo apt install -y swift',
        'sudo apt install -y haskell-platform',
        'sudo apt install -y scala',
        'sudo apt install -y erlang',
        'sudo apt install -y elixir',
        'sudo apt install -y julia',
        'sudo apt install -y racket',
        'sudo apt install -y perl6',
        'sudo apt install -y tcl',
        'sudo apt install -y ocaml',
        'sudo apt install -y nim',
        'sudo apt install -y groovy',
        'sudo apt install -y coffeescript',
        'sudo apt install -y clojure',
        'sudo apt install -y verilog'
    ]

    for lang in languages:
        run_command(lang)


def install_pip_modules():
    modules = [
        'numpy',
        'matplotlib',
        'requests',
        'beautifulsoup4',
        'flask',
        'django',
        'tensorflow',
        'pytorch',
        'pandas',
        'scikit-learn',
        'pytest',
        'virtualenv',
        'seaborn',
        'sqlalchemy',
        'pyyaml',
        'jupyter',
        'black',
        'selenium',
        'click',
        'pylint',
        'faker',
        'networkx',
        'plotly',
        'pyqt5',
        'kivy',
        'pyinstaller',
        'wxpython',
        'pygame',
        'pillow',
        'requests-html',
        'tqdm',
        'joblib',
        'scrapy',
        'pyarrow',
        'arrow',
        'google-api-python-client',
        'opencv-python',
        'bokeh',
        'streamlit',
        'fastapi',
        'uvicorn',
        'pandas-profiling',
        'nbconvert',
        'pyodbc',
        'dash',
        'dash-bootstrap-components',
        'redis',
        'cryptography',
        'docker',
        'pytest-cov',
        'flake8',
        'mypy',
        'grpcio',
        'pymongo',
        'aioredis',
        'asyncpg',
        'kafka-python',
        'pykafka',
        'sqlparse',
        'django-rest-framework',
        'flask-restful',
        'celery',
        'uvloop',
        'marshmallow',
        'alembic',
        'pyjwt',
        'pytest-html',
        'fastapi-pagination',
        'fastapi-jwt-auth',
        'gunicorn',
        'python-dotenv',
        'httpx',
        'uvicorn',
        'websockets',
        'orjson',
        'pydantic',
        'regex',
        'pandasql',
        'dash-daq',
        'pandas-datareader',
        'xlrd',
        'openpyxl',
        'pytz',
        'redis-py',
        'h5py',
        'pyarrow',
        'gorilla',
        'pydantic',
        'pymongo',
        'paramiko',
        'jinja2',
        'sqlalchemy-utils',
        'graphene',
        'pandas-datareader',
        'yfinance',
        'gspread',
        'openai',
        'oauthlib',
        'spotipy',
        'tweepy',
        'pywebview',
        'pyjwt',
        'pyshorteners',
        'yagmail',
        'pyautogui',
        'pygame',
        'pyttsx3',
        'sounddevice',
        'pytesseract',
        'pyqrcode',
        'pywhatkit',
        'pycaw',
        'moviepy',
        'youtube-dl',
        'tkinter',
        'wxpython',
        'pyinstaller',
        'pycryptodome',
        'crypto',
        'cryptography',
        'pycryptodome',
        'pycryptodome',
        'pycryptodome',
        'psycopg2',
        'mysql-connector-python',
        'pymssql',
        'cx_Oracle',
        'sqlalchemy-redshift',
        'pyhive',
        'thrift',
        'grpcio-tools',
        'python-consul',
        'etcd3',
        'pika',
        'pymqi',
        'pydbus',
        'pyzmq',
        'pyserial',
        'pyusb',
        'pybluez',
        'pymodbus',
        'pyopc',
        'opcua',
        'pymodbus-tk',
        'paho-mqtt',
        'pymqtt',
        'scapy',
        'pyshark',
        'pylibpcap',
        'pyyaml',
        'ruamel.yaml',
        'pyglet',
        'pyopengl',
        'pycuda',
        'pyopencl',
        'pytesseract',
        'python-docx',
        'python-pptx',
        'openpyxl',
        'xlwt',
        'xlutils',
        'pywin32',
        'pygtk',
        'pyqtgraph',
        'pyopengl-accelerate',
        'pywebview',
        'pyinstaller',
        'pycryptodome',
    ]

    for module in modules:
        run_command(f'pip install --upgrade {module}')


def draw_menu(stdscr, menu, current_row):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    # Print the title at the top
    title = pyfiglet.figlet_format("Crumb Packer", font="slant")
    title_lines = title.split("\n")
    
    # Print title lines
    for i, line in enumerate(title_lines):
        if i < h // 2:  # Only print title lines that fit within the top quarter of the screen
            line = line[:w-1]  # Ensure line length doesn't exceed terminal width
            x = w // 2 - len(line) // 2
            y = i
            stdscr.addstr(y, x, line, curses.color_pair(1))
    
    # Print menu items closer to the title
    menu_start_y = h // 4 + len(title_lines) - 8  # Start menu just below the title with a bit of padding
    for i, item in enumerate(menu):
        if i < h - menu_start_y - 1:  # Ensure menu items fit within available height
            item = item[:w-1]  # Ensure item length doesn't exceed terminal width
            x = w // 2 - len(item) // 2
            y = menu_start_y + i
            
            if i == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, item, curses.A_REVERSE)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, item)

    stdscr.refresh()






def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Define color pair for title

    menu = ['Update Package List', 'Upgrade Packages', 'Upgrade Pip', 'Install Languages',
            'Install Pip Modules', 'Exit']
    current_row = 0

    while True:
        draw_menu(stdscr, menu, current_row)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            if current_row == 0:
                run_command('sudo apt update')
            elif current_row == 1:
                run_command('sudo apt upgrade -y')
            elif current_row == 2:
                run_command('pip install --upgrade pip')
            elif current_row == 3:
                install_languages()
            elif current_row == 4:
                install_pip_modules()
            elif current_row == 5:
                break

if __name__ == '__main__':
    curses.wrapper(main)

