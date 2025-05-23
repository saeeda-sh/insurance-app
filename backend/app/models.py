import enum
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import TIMESTAMP, Column, Date, Enum, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from .database import Base


class PolicyStatus(enum.Enum):
    active = "active"
    expired = "expired"
    canceled = "canceled"
    pending = "pending"


class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"

    policy_id = Column(
        UUID,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )
    policy_type = Column(String, nullable=False)
    premium_amount = Column(Integer, nullable=False)
    policy_start_date = Column(Date, nullable=False)
    policy_end_date = Column(Date, nullable=False)
    policy_status = Column(
        Enum(PolicyStatus), default=PolicyStatus.pending, nullable=False
    )

    customer_id = Column(UUID, ForeignKey("customers.customer_id"), nullable=False)
    customer = relationship("Customer", back_populates="policies")

    def __repr__(self):
        return f"<InsurancePolicy(policy_id={self.policy_id}, policy_type={self.policy_type})>"


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(
        UUID,
        primary_key=True,
        nullable=False,
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    policies = relationship("InsurancePolicy", back_populates="customer")

    def __repr__(self):
        return f"<Customer(customer_id={self.customer_id}, name={self.first_name} {self.last_name})>"
