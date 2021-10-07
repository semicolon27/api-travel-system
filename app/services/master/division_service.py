
"""
Helo
"""
from sqlalchemy.sql.elements import or_
from app.schema.master.division_schema import Division, RequestDivisionByCode
from app.models.db_models import T_Division
from sqlalchemy.orm import Session
from sqlalchemy import and_, asc
from sqlalchemy.sql.expression import func


def get_division_by_id(db: Session, division_id):
    division_by_id = db.query(T_Division).filter(
        T_Division.OffCode == division_id).first()
    return division_by_id


""" TODO: 
###
frmmPrincipal, frmmJobKind, frmCMImJobKind
"select DivID, DivName from Division where offcode='" & gOffCode & "' and  left(Divname,'" & varlong & "') like '" & VarSelection & "' order by DivName" 
"""


def get_division_by_code(db: Session, req: RequestDivisionByCode):
    division_by_code = db.query(T_Division).with_entities(T_Division.DivID, T_Division.DivName).filter(
        and_(T_Division.OffCode == req.OffCode, func.left(T_Division.DivName, req.varlong).like(req.varselection))).order_by(asc(T_Division.DivName))
    return division_by_code


"""
"select account.*,curency.name as Curname from (account left outer join curency on account.cur=curency.cur)  where offcode='" & gOffCode & "' and Account.grouptran<>'C' and Account.grouptran<>'B' order by account"
"""

"""
###
frmmInvDesc

grdAccount()
If txtAccountName.Text = "" Then
   adoList.RecordSource = "select account.*,curency.name as Curname from (account left outer join curency on account.cur=curency.cur)  where offcode='" & gOffCode & "' and Account.grouptran<>'C' and Account.grouptran<>'B' order by account"
  Else
   adoList.RecordSource = "select account.*,curency.name as Curname from (account left outer join curency on account.cur=curency.cur) where offcode='" & gOffCode & "' and Account.grouptran<>'C' and Account.grouptran<>'B' and left(account.name,'" & varlong & "') like '" & VarSelection & "' order by account"
 End If

grdJobKind()
If txtJobName.Text = "" Then
   adoList.RecordSource = "select Jobkind.JobKind, Jobkind.jobName,Division.DivName from Jobkind Left Outer join Division on Jobkind.offcode=Division.offcode and Jobkind.DivID=Division.DivID where Jobkind.offcode='" & gOffCode & "'"
  Else
   adoList.RecordSource = "select Jobkind.JobKind, Jobkind.jobName,Division.DivName from Jobkind Left Outer join Division on Jobkind.offcode=Division.offcode and Jobkind.DivID=Division.DivID where Jobkind.offcode='" & gOffCode & "' and  left(jobname,'" & varlong & "') like '" & VarSelection & "' order by JobName"
 End If
"""
