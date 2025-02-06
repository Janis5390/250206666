import os
from dotenv import load_dotenv


if 'ENV_FILE' in os.environ:
    
    env_file = os.environ['ENV_FILE']
    load_dotenv(env_file)

else:
    load_dotenv()