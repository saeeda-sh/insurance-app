from pydantic import BaseModel
from datetime import date
from enum import Enum
import uuid


class CustomerBase(BaseModel):
    first_name: str
    last_name: str


class Customer(CustomerBase):
    customer_id: uuid.UUID
    policies: list["InsurancePolicy"] = []

    class Config:
        from_attributes = True
        exclude = {"policies"}


class PolicyStatus(str, Enum):
    active = "active"
    expired = "expired"
    canceled = "canceled"
    pending = "pending"


class InsurancePolicyBase(BaseModel):
    policy_type: str
    premium_amount: int
    policy_start_date: date
    policy_end_date: date
    policy_status: PolicyStatus
    customer_id: uuid.UUID


class InsurancePolicy(InsurancePolicyBase):
    policy_id: uuid.UUID

    class Config:
        from_attributes = True
        exclude = {"customer"}
