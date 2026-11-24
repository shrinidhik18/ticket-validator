
import csv
import logging

from pydantic import ValidationError
from tickets.models import Ticket

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


def load_tickets(file_path: str):
    valid_tickets = []
    invalid_tickets = []

    try:
        # utf-8-sig handles the BOM in Windows-generated CSV files
        with open(file_path, "r", newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)

            if not reader.fieldnames:
                logger.warning("CSV file is empty or has no header.")
                return valid_tickets, invalid_tickets

            for row_number, row in enumerate(reader, start=2):
                try:
                    ticket = Ticket.model_validate(row)
                    valid_tickets.append(ticket)

                    logger.info("Row %s: Valid ticket", row_number)

                except ValidationError as error:
                    invalid_tickets.append({
                        "row": row_number,
                        "errors": error.errors()
                    })

                    logger.error("Row %s: Invalid ticket", row_number)

    except FileNotFoundError:
        logger.error("CSV file not found: %s", file_path)

    return valid_tickets, invalid_tickets
