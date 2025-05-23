import logging
import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

from ..database import get_db
from .. import models, schemas


router = APIRouter()

logger = logging.getLogger("insurance-policy-api")
logger.setLevel(logging.INFO)


def handle_db_error(error: Exception, db: Session):
    logger.error(f"Database error: {str(error)}")
    db.rollback()
    raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/", response_model=list[schemas.InsurancePolicy])
def read_policies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        policies = db.query(models.InsurancePolicy).offset(skip).limit(limit).all()
        if not policies:
            logger.warning(f"No insurance policies in database.")
        return policies
    except Exception as e:
        handle_db_error(e, db)
