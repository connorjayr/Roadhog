import os
from dotenv import load_dotenv
import roadhog

if __name__ == '__main__':
    load_dotenv()

    roadhog = roadhog.Roadhog()
    roadhog.run(os.getenv('TOKEN'))
