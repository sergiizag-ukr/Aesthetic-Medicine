from service_manager import run
from database import init_db
import logging
 
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(
            "service_manager.log",
            encoding="utf-8"
            ),
            logging.StreamHandler()
            ]
)


init_db()

if __name__ == "__main__":
    run()
