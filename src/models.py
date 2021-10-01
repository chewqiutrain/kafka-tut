from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime 
import uuid
from uuid import UUID

@dataclass_json
@dataclass
class TestFees:
    amount: float 
    currency: str 


@dataclass_json
@dataclass
class TestData:
    id: UUID
    first_name: str 
    last_name: str
    created_tstamp: datetime
    fees: TestFees

    def __str__(self) -> str:
        return f"TestData(id = {self.id.__str__()} | first_name = {self.first_name} | " + \
            f"last_name = {self.last_name} | " + \
            f"created_tstamp = {self.created_tstamp.strftime('%Y-%m-%d %H:%M:%S')} | " + \
            f"fees = {self.fees}"
