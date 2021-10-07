"""
Helo
"""
from app.schema.master.jobkind_schema import JobKind
from app.models.db_models import T_JobKind
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_jobkinds(db: Session):
    all_get = db.query(T_JobKind).order_by(desc(T_JobKind.JobName)).all()
    return all_get


def search_jobkinds(db: Session, keyword: str):
    result = db.query(T_JobKind).filter(
        T_JobKind.JobName.like(f"%{keyword}%")).all()
    print(result)
    return result


def get_jobkind_by_id(db: Session, jobkind_id):
    jobkind_by_id = db.query(T_JobKind).filter(
        T_JobKind.OffCode == jobkind_id).first()
    return jobkind_by_id


def add_jobkind(db: Session, jobkind: JobKind):
    db_jobkind = T_JobKind(**jobkind.dict())
    db.add(db_jobkind)
    db.commit()
    db.refresh(db_jobkind)
    return db_jobkind


def edit_jobkind(db: Session, jobkind: JobKind) -> JobKind:
    edited_jobkind = get_jobkind_by_id(db, jobkind.OffCode)
    jobkind_new = T_JobKind(**jobkind.dict())

    edited_jobkind.JobName = jobkind_new.JobName
    edited_jobkind.JobKind = jobkind_new.JobKind
    edited_jobkind.DivID = jobkind_new.DivID

    db.commit()
    db.refresh(edited_jobkind)

    return jobkind


def delete_jobkind(db: Session, jobkind: JobKind):
    deleted_jobkind = get_jobkind_by_id(db, jobkind.JobKindID)
    db.delete(deleted_jobkind)
    db.commit()
    return deleted_jobkind

"""
frmmitem
"select JobKind, jobName from Jobkind where offcode='" & gOffCode & "' and  left(jobname,'" & varlong & "') like '" & VarSelection & "' order by JobName"


"""
