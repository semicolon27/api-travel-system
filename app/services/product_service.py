from app.models import db_models as models
from app.utils import database as db
from sqlalchemy import text

async def get_categories():
    query = models.t_Category.select()
    all_get = await db.database.fetch_all(query)
    return all_get