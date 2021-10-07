"""
frmmitem
"select account.*,curency.name as Curname from (account left outer join curency on account.cur=curency.cur) left outer join accsubGroup on account.accsubgroup = accsubgroup.subgroup where offcode='" & gOffCode & "' and accsubgroup.grouptran<>'C' and accsubgroup.grouptran<>'B' order by account"
"select account.*,curency.name as Curname from (account left outer join curency on account.cur=curency.cur)left outer join accsubGroup on account.accsubgroup = accsubgroup.subgroup where offcode='" & gOffCode & "' and accsubgroup.grouptran<>'C' and accsubgroup.grouptran<>'B' and left(account.name,'" & varlong & "') like '" & VarSelection & "' order by account"
"""
