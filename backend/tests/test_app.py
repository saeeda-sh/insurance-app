import pytest
import uuid
from datetime import datetime
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app import models
from app.database import SessionLocal, engine
from app.utils.seed_db import seed_db
from app.utils.config import settings

# Override the database URL with local db for testing
engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)
client = TestClient(app)


@pytest.fixture(scope="module")
def db():
    # Test Database Session
    db_session = SessionLocal()

    # Clean up the database before running tests
    db_session.query(models.InsurancePolicy).delete()
    db_session.query(models.Customer).delete()
    db_session.commit()

    seed_db()
    yield db_session
    db_session.close()


@pytest.fixture(scope="module")
def create_customer_and_policy(db):
    # Create a sample customer
    customer_data = {
        "customer_id": uuid.uuid4(),
        "first_name": "John",
        "last_name": "Doe",
        "created_at": datetime.now(),
    }
    customer = models.Customer(**customer_data)
    db.add(customer)
    db.commit()
    db.refresh(customer)

    # Create a sample policy
    policy_data = {
        "policy_id": uuid.uuid4(),
        "policy_type": "Health",
        "premium_amount": 2000,
        "policy_start_date": "2023-01-01",
        "policy_end_date": "2023-12-31",
        "policy_status": "active",
        "customer_id": customer.customer_id,
    }
    policy = models.InsurancePolicy(**policy_data)
    db.add(policy)
    db.commit()
    db.refresh(policy)
    return customer, policy


def test_read_policies(db, create_customer_and_policy):
    response = client.get("/api/policies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
