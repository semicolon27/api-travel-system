from app.models import db_models as models
from sqlalchemy.orm import Session


def get_categories(db: Session):
    # db.query ngga bisa pkai await
    all_get = db.query(models.t_Category).all()
    return all_get
