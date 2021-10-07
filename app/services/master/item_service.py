from app.models.db_models import T_InvDesc, T_Item, T_JobKind
from sqlalchemy.orm import Session
from sqlalchemy import desc


"""
frmmitem
"SELECT  JobKind.JobName,InvDesc.InvDesc,Item.*,jobkind.jobkind " & _
   " FROM (Item left outer JOIN InvDesc ON Item.InvID = InvDesc.InvID) left outer JOIN JobKind ON InvDesc.JobKind = JobKind.JobKind " & _
   "where Item.offcode='" & gOffCode & "' "
"""


def get_item_jobkind_invdesc(db: Session, gOffCode: str):
    item_list = db.query(T_Item).join(T_InvDesc, T_Item.itemID == T_InvDesc.InvID).join(
        T_JobKind, T_InvDesc.JobKind == T_JobKind.JobKind).filter(T_Item.OffCode == gOffCode).all()
    return item_list


def get_jobkinds(db: Session):
    all_get = db.query(T_JobKind).order_by(desc(T_JobKind.JobName)).all()
    return all_get
