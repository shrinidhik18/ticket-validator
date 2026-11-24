
from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class Ticket(BaseModel):
    ticket_id: str = Field(min_length=1)
    customer_name: str = Field(min_length=1)
    service_type: str = Field(min_length=1)
    status: TicketStatus
    created_date: date
    description: str = Field(min_length=1)
