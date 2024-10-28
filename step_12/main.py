from datetime import datetime, date, time, timedelta
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel
from typing import Set, FrozenSet, Optional

# Pydantic Model using different data types
class SampleModel(BaseModel):
    user_id: UUID  
    created_at: datetime  
    birth_date: date  
    login_time: time  
    session_duration: timedelta  
    tags: Set[str]  
    permissions: FrozenSet[str]  
    data: bytes  
    balance: Decimal  
    is_active: Optional[bool] = None  

# Example usage
example_data = {
    "user_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "created_at": "2024-10-27T14:23:00+05:00",
    "birth_date": "1990-05-15",
    "login_time": "08:45:00",
    "session_duration": 3600.5,  # 3600.5 seconds (1 hour + 0.5 second)
    "tags": ["python", "fastapi", "backend", "python"],  # Duplicates will be removed
    "permissions": ["read", "write", "read"],  # Duplicates will be removed
    "data": "SGVsbG8gV29ybGQh",  # "Hello World!" in Base64
    "balance": "12345.67",
    "is_active": True,
}

# Parse the data using Pydantic
sample_model = SampleModel(**example_data)

# Output the parsed data
print(sample_model.json(indent=4))
