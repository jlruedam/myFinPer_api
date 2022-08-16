# Python
from datetime import datetime
from typing import Optional
# Pydantic
from pydantic import BaseModel

class AccountingEvent(BaseModel):
    event_id: int
    date_transaction = datetime
    subaccount_id: int
    description: str
    user_id: int

