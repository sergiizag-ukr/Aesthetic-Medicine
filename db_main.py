from service_manager import run
from database import init_db

init_db()


if __name__ == "__main__":
    run()