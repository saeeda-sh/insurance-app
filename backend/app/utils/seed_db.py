import uuid
from datetime import date
from sqlalchemy.orm import Session
from ..models import Customer, InsurancePolicy, PolicyStatus
from ..database import SessionLocal


def create_sample_data(db: Session):
    customer = Customer(customer_id=uuid.uuid4(), first_name="John", last_name="Doe")
    db.add(customer)
    db.commit()
    db.refresh(customer)

    policy1 = InsurancePolicy(
        policy_id=uuid.uuid4(),
        policy_type="Health Insurance",
        premium_amount=500,
        policy_start_date=date(2023, 1, 1),
        policy_end_date=date(2024, 1, 1),
        policy_status=PolicyStatus.active,
        customer_id=customer.customer_id,
    )
    policy2 = InsurancePolicy(
        policy_id=uuid.uuid4(),
        policy_type="Life Insurance",
        premium_amount=1000,
        policy_start_date=date(2023, 6, 1),
        policy_end_date=date(2025, 6, 1),
        policy_status=PolicyStatus.pending,
        customer_id=customer.customer_id,
    )

    db.add(policy1)
    db.add(policy2)
    db.commit()


def seed_db():
    db = SessionLocal()
    try:
        create_sample_data(db)
    finally:
        db.close()


if __name__ == "__main__":
    seed_db()
