from config import load_config
from birthday import BirthdayService
from logger import get_logger

logger = get_logger()


def main():
    config = load_config()

    logger.info("Birthday Automation Started")

    service = BirthdayService(config)
    service.run()

    logger.info("Birthday Automation Completed")


if __name__ == "__main__":
    main()