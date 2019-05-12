from dotenv import load_dotenv
from pathlib import Path
import os
from lib import calc

# Read .env file 
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# does it work?
print("Hallo lieber ",os.getenv('USERNAME'))

# awesome calculation!
print("3 plus 5 ist {}!" .format(calc.sum(3,5)))

