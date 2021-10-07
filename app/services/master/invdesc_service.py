"""
frmmmitem
"select JobKind.jobName,invDesc.InvDesc,invDesc.InvID,JobKind.Jobkind from invdesc inner join Jobkind on invdesc.offcode=jobkind.offcode and invdesc.jobkind=jobkind.jobkind where invdesc.offcode='" & gOffCode & "'"
"""
