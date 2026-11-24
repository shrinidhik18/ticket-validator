
import logging

from tickets.loader import load_tickets

logger = logging.getLogger(__name__)


def validate_csv(file_path: str):
    valid_tickets, invalid_tickets = load_tickets(file_path)

    print("\n========== TICKET VALIDATION REPORT ==========")

    print(f"\nTotal valid tickets: {len(valid_tickets)}")
    print(f"Total invalid tickets: {len(invalid_tickets)}")

    print("\n--- VALID TICKETS ---")
    for ticket in valid_tickets:
        print(f"{ticket.ticket_id}: {ticket.customer_name} - Valid")

    print("\n--- INVALID TICKETS ---")
    for ticket in invalid_tickets:
        print(f"Row {ticket['row']}: Invalid")
        for error in ticket["errors"]:
            print(f"  {error['loc'][0]}: {error['msg']}")

    logger.info("CSV validation completed.")

    return valid_tickets, invalid_tickets


if __name__ == "__main__":
    validate_csv("data/tickets.csv")
