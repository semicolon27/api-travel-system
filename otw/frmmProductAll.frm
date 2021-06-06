' Get Cateogry dropdown

Sub grdCategory()
Dim varlong As Integer
VarSelection = Replace(Trim(txtCategory.Text), "'", "''") & "%"
varlong = Len(Trim(VarSelection))
 
 If txtCategory.Text = "" Then
   adoList.RecordSource = "select * from Category order by CategoryDesc"
  Else
   adoList.RecordSource = "select * from Category WHERE left(CategoryDesc,'" & varlong & "') like '" & VarSelection & "' order by CategorydESC"
 End If
 adoList.Refresh
 grdListNo = 2
 GrdList.ClearFields
GrdListShow Me, txtCategory.Left, txtCategory.Top, 3000, 3000
End Sub
Sub grdCategory_dblclick()
 If IsNull(adoList.Recordset!CategoryDesc) Then txtCategory.Text = "" Else txtCategory.Text = adoList.Recordset!CategoryDesc
 If IsNull(adoList.Recordset!CategoryID) Then lblCateID.Caption = "" Else lblCateID.Caption = adoList.Recordset!CategoryID
End Sub