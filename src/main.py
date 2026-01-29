import logging
import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import settings
from src.services.auth_service import GoogleAuthManager
from src.services.gmail_service import GmailService
from src.services.calendar_service import CalendarService
from src.services.notion_service import NotionService

logging.basicConfig(level=settings.LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Personal Task Automation Agent...")
    
    logger.info("Initializing Services...")
    
    # Test Gmail
    try:
        gmail_service = GmailService()
        logger.info("Gmail Service initialized.")
    except Exception as e:
        logger.error(f"Failed to initialize Gmail Service: {e}")

    # Test Calendar
    try:
        calendar_service = CalendarService()
        logger.info("Calendar Service initialized.")
    except Exception as e:
        logger.error(f"Failed to initialize Calendar Service: {e}")

    # Test Notion
    try:
        notion_service = NotionService()
        logger.info("Notion Service initialized.")
    except Exception as e:
        logger.error(f"Failed to initialize Notion Service: {e}")

    logger.info("Service initialization complete. Please ensure valid credentials are in .env and credentials/.")


if __name__ == "__main__":
    main()
