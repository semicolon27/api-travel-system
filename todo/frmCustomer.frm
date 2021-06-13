VERSION 5.00
Object = "{86CF1D34-0C5F-11D2-A9FC-0000F8754DA1}#2.0#0"; "mscomct2.ocx"
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Begin VB.Form frmCustomer 
   BackColor       =   &H00C0E0FF&
   Caption         =   "Data Customer"
   ClientHeight    =   10125
   ClientLeft      =   165
   ClientTop       =   555
   ClientWidth     =   11400
   LinkTopic       =   "Form1"
   ScaleHeight     =   10125
   ScaleWidth      =   11400
   StartUpPosition =   2  'CenterScreen
   WindowState     =   2  'Maximized
   Begin MSDataGridLib.DataGrid grdlist 
      Bindings        =   "frmCustomer.frx":0000
      Height          =   1215
      Left            =   4920
      TabIndex        =   2
      Top             =   4320
      Visible         =   0   'False
      Width           =   4335
      _ExtentX        =   7646
      _ExtentY        =   2143
      _Version        =   393216
      BackColor       =   -2147483624
      ForeColor       =   0
      HeadLines       =   1
      RowHeight       =   15
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   2
      BeginProperty Column00 
         DataField       =   ""
         Caption         =   ""
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   ""
         Caption         =   ""
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      SplitCount      =   1
      BeginProperty Split0 
         BeginProperty Column00 
         EndProperty
         BeginProperty Column01 
         EndProperty
      EndProperty
   End
   Begin MSDataGridLib.DataGrid grdListFind 
      Bindings        =   "frmCustomer.frx":0016
      Height          =   1215
      Left            =   5880
      TabIndex        =   5
      Top             =   5280
      Visible         =   0   'False
      Width           =   4935
      _ExtentX        =   8705
      _ExtentY        =   2143
      _Version        =   393216
      AllowUpdate     =   0   'False
      BackColor       =   16697820
      HeadLines       =   1
      RowHeight       =   19
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   2
      BeginProperty Column00 
         DataField       =   ""
         Caption         =   ""
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   ""
         Caption         =   ""
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      SplitCount      =   1
      BeginProperty Split0 
         BeginProperty Column00 
         EndProperty
         BeginProperty Column01 
         EndProperty
      EndProperty
   End
   Begin VB.CommandButton cmdfirst 
      Caption         =   "F&irst"
      Enabled         =   0   'False
      Height          =   750
      Left            =   6480
      Picture         =   "frmCustomer.frx":0031
      Style           =   1  'Graphical
      TabIndex        =   99
      Top             =   1800
      Width           =   855
   End
   Begin VB.CommandButton cmdPrev 
      Caption         =   "Pre&vious"
      Enabled         =   0   'False
      Height          =   750
      Left            =   7320
      Picture         =   "frmCustomer.frx":06E2
      Style           =   1  'Graphical
      TabIndex        =   98
      Top             =   1800
      Width           =   855
   End
   Begin VB.CommandButton cmdNext 
      Caption         =   "&Next"
      Enabled         =   0   'False
      Height          =   750
      Left            =   8160
      Picture         =   "frmCustomer.frx":0DD0
      Style           =   1  'Graphical
      TabIndex        =   97
      Top             =   1800
      Width           =   855
   End
   Begin VB.CommandButton cmdLast 
      Caption         =   "&Last"
      Enabled         =   0   'False
      Height          =   750
      Left            =   9000
      Picture         =   "frmCustomer.frx":14BD
      Style           =   1  'Graphical
      TabIndex        =   96
      Top             =   1800
      Width           =   855
   End
   Begin VB.CommandButton cmdExit 
      Caption         =   "E&xit"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   10560
      Picture         =   "frmCustomer.frx":1B99
      Style           =   1  'Graphical
      TabIndex        =   95
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdDelete 
      Caption         =   "&Delete"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   9720
      Picture         =   "frmCustomer.frx":212A
      Style           =   1  'Graphical
      TabIndex        =   94
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdAdd 
      Caption         =   "&Add"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   5520
      Picture         =   "frmCustomer.frx":279D
      Style           =   1  'Graphical
      TabIndex        =   93
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdEdit 
      Caption         =   "&Edit"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   6360
      Picture         =   "frmCustomer.frx":2E92
      Style           =   1  'Graphical
      TabIndex        =   92
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdCancel 
      Caption         =   "&Cancel"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   7200
      Picture         =   "frmCustomer.frx":34B1
      Style           =   1  'Graphical
      TabIndex        =   91
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdSave 
      Caption         =   "&Save"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   8040
      Picture         =   "frmCustomer.frx":3B91
      Style           =   1  'Graphical
      TabIndex        =   90
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdPrint 
      Caption         =   "&Print"
      BeginProperty Font 
         Name            =   "Arial Narrow"
         Size            =   9.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   8880
      Picture         =   "frmCustomer.frx":4220
      Style           =   1  'Graphical
      TabIndex        =   89
      Top             =   2640
      Width           =   855
   End
   Begin VB.CommandButton cmdFind 
      Appearance      =   0  'Flat
      Caption         =   "&Find"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   750
      Left            =   10560
      MaskColor       =   &H00C00000&
      Picture         =   "frmCustomer.frx":48C8
      Style           =   1  'Graphical
      TabIndex        =   88
      Top             =   1800
      Width           =   855
   End
   Begin VB.TextBox txtIdent 
      Height          =   285
      Left            =   1920
      MaxLength       =   3
      TabIndex        =   84
      Text            =   "nam"
      Top             =   2640
      Width           =   735
   End
   Begin VB.Frame fraCorrespondece 
      Height          =   6615
      Left            =   360
      TabIndex        =   6
      Top             =   3360
      Width           =   5775
      Begin VB.CheckBox chkActive 
         Caption         =   "Active"
         Height          =   195
         Left            =   1440
         TabIndex        =   34
         Top             =   6240
         Width           =   1935
      End
      Begin VB.TextBox txtNote2 
         Height          =   285
         Left            =   1440
         TabIndex        =   33
         Text            =   "txtNote2"
         Top             =   5760
         Width           =   2175
      End
      Begin VB.TextBox txtNote1 
         Height          =   285
         Left            =   1440
         TabIndex        =   32
         Text            =   "txtNote1"
         Top             =   5520
         Width           =   2175
      End
      Begin VB.TextBox txtCorContact2 
         Height          =   285
         Left            =   1440
         TabIndex        =   30
         Text            =   "txtCorContact2"
         Top             =   4560
         Width           =   2175
      End
      Begin VB.TextBox txtCorContact1 
         Height          =   285
         Left            =   1440
         TabIndex        =   29
         Text            =   "txtCorContact1"
         Top             =   4320
         Width           =   2175
      End
      Begin VB.TextBox txtCorPhone2 
         Height          =   285
         Left            =   1440
         TabIndex        =   28
         Text            =   "txtCorPhone2"
         Top             =   3120
         Width           =   2175
      End
      Begin VB.TextBox txtCorPhone1 
         Height          =   285
         Left            =   1440
         TabIndex        =   27
         Text            =   "txtCorPhone1"
         Top             =   2880
         Width           =   2175
      End
      Begin VB.TextBox txtCorFax2 
         Height          =   285
         Left            =   1440
         TabIndex        =   25
         Text            =   "txtCorFax2"
         Top             =   3960
         Width           =   2175
      End
      Begin VB.TextBox txtCorFax1 
         Height          =   285
         Left            =   1440
         TabIndex        =   24
         Text            =   "txtCorFax1"
         Top             =   3600
         Width           =   2175
      End
      Begin VB.TextBox txtCorAdd4 
         Height          =   285
         Left            =   1440
         TabIndex        =   23
         Text            =   "txtCorAdd4"
         Top             =   960
         Width           =   4095
      End
      Begin VB.TextBox txtCorAdd3 
         Height          =   285
         Left            =   1440
         TabIndex        =   22
         Text            =   "txtCorAdd3"
         Top             =   720
         Width           =   4095
      End
      Begin VB.TextBox txtCorAdd2 
         Height          =   285
         Left            =   1440
         TabIndex        =   21
         Text            =   "txtCorAdd2"
         Top             =   480
         Width           =   4095
      End
      Begin VB.TextBox txtCorAdd1 
         Height          =   285
         Left            =   1440
         TabIndex        =   20
         Text            =   "txtCorAdd1"
         Top             =   240
         Width           =   4095
      End
      Begin VB.TextBox txtCorEmail 
         Height          =   285
         Left            =   1440
         TabIndex        =   17
         Text            =   "txtCorEmail"
         Top             =   5040
         Width           =   3375
      End
      Begin VB.TextBox txtCorZipCode 
         Height          =   315
         Left            =   1440
         TabIndex        =   12
         Text            =   "txtCorZipCode"
         Top             =   2400
         Width           =   3015
      End
      Begin VB.TextBox txtCorCountry 
         Height          =   285
         Left            =   1440
         TabIndex        =   8
         Text            =   "txtCorCountry"
         Top             =   1920
         Width           =   2895
      End
      Begin VB.TextBox txtCorCity 
         Height          =   285
         Left            =   1440
         TabIndex        =   7
         Text            =   "txtCorCity"
         Top             =   1440
         Width           =   2895
      End
      Begin VB.Label Label15 
         Caption         =   "Note :"
         Height          =   255
         Left            =   120
         TabIndex        =   31
         Top             =   5535
         Width           =   975
      End
      Begin VB.Label Label17 
         Caption         =   "Phone :"
         Height          =   255
         Left            =   120
         TabIndex        =   26
         Top             =   2895
         Width           =   1095
      End
      Begin VB.Label Label20 
         Caption         =   "Address :"
         Height          =   255
         Left            =   120
         TabIndex        =   19
         Top             =   240
         Width           =   975
      End
      Begin VB.Label Label18 
         Caption         =   "Email :"
         Height          =   255
         Left            =   120
         TabIndex        =   18
         Top             =   5055
         Width           =   975
      End
      Begin VB.Label lblCorCountry 
         Height          =   255
         Left            =   4560
         TabIndex        =   16
         Top             =   1920
         Width           =   855
      End
      Begin VB.Label lblCorCity 
         Height          =   255
         Left            =   4560
         TabIndex        =   15
         Top             =   1440
         Width           =   975
      End
      Begin VB.Label Label16 
         Caption         =   "Contact :"
         Height          =   255
         Left            =   120
         TabIndex        =   14
         Top             =   4335
         Width           =   975
      End
      Begin VB.Label Label14 
         Caption         =   "ZipCode :"
         Height          =   255
         Left            =   120
         TabIndex        =   13
         Top             =   2430
         Width           =   855
      End
      Begin VB.Label Label13 
         Caption         =   "Fax"
         Height          =   255
         Left            =   120
         TabIndex        =   11
         Top             =   3615
         Width           =   1095
      End
      Begin VB.Label Label12 
         Caption         =   "City :"
         Height          =   255
         Left            =   120
         TabIndex        =   10
         Top             =   1470
         Width           =   855
      End
      Begin VB.Label Label11 
         Caption         =   "Country :"
         Height          =   255
         Left            =   120
         TabIndex        =   9
         Top             =   1935
         Width           =   975
      End
   End
   Begin VB.TextBox txtPartnerName 
      Height          =   285
      Left            =   1920
      TabIndex        =   1
      Text            =   "name"
      Top             =   2280
      Width           =   3615
   End
   Begin VB.TextBox txtPartnerID 
      Height          =   285
      Left            =   1920
      TabIndex        =   0
      Text            =   "ID"
      Top             =   1920
      Width           =   1935
   End
   Begin VB.Frame fraComp 
      Height          =   6615
      Left            =   6120
      TabIndex        =   35
      Top             =   3360
      Width           =   6015
      Begin VB.TextBox txtaddress1 
         Height          =   285
         Left            =   1080
         TabIndex        =   57
         Text            =   "Address1"
         Top             =   5520
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtaddress2 
         Height          =   285
         Left            =   1080
         TabIndex        =   56
         Text            =   "Address2"
         Top             =   5760
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtaddress3 
         Height          =   285
         Left            =   1080
         TabIndex        =   55
         Text            =   "Address3"
         Top             =   6000
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtaddress4 
         Height          =   285
         Left            =   1080
         TabIndex        =   54
         Text            =   "Address4"
         Top             =   6240
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtCity 
         Height          =   315
         Left            =   3240
         TabIndex        =   53
         Text            =   "txtCity"
         Top             =   5880
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtZipCode 
         Height          =   315
         Left            =   5160
         TabIndex        =   52
         Text            =   "txtZipCode"
         Top             =   5640
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtEmail 
         Height          =   285
         Left            =   1560
         TabIndex        =   51
         Text            =   "txtEmail"
         Top             =   6360
         Visible         =   0   'False
         Width           =   3375
      End
      Begin VB.TextBox txtFax1 
         Height          =   285
         Left            =   360
         TabIndex        =   50
         Text            =   "txtFax1"
         Top             =   6000
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtFax2 
         Height          =   285
         Left            =   360
         TabIndex        =   49
         Text            =   "txtFax2"
         Top             =   6240
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtPhone1 
         Height          =   285
         Left            =   360
         TabIndex        =   48
         Text            =   "txtPhone1"
         Top             =   5400
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtPhone2 
         Height          =   285
         Left            =   2640
         TabIndex        =   47
         Text            =   "txtPhone2"
         Top             =   6120
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtContact1 
         Height          =   285
         Left            =   5160
         TabIndex        =   46
         Text            =   "txtContact1"
         Top             =   6000
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtContact2 
         Height          =   285
         Left            =   5160
         TabIndex        =   45
         Text            =   "txtContact2"
         Top             =   6240
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtNPWP 
         Height          =   285
         Left            =   2400
         TabIndex        =   43
         Text            =   "txtEmail"
         Top             =   480
         Width           =   3375
      End
      Begin VB.TextBox txtCountry 
         Height          =   285
         Left            =   3240
         TabIndex        =   42
         Text            =   "txtCorCountry"
         Top             =   6240
         Visible         =   0   'False
         Width           =   495
      End
      Begin VB.TextBox txtApitu 
         Height          =   285
         Left            =   1440
         TabIndex        =   41
         Text            =   "txtEmail"
         Top             =   4695
         Width           =   3375
      End
      Begin VB.TextBox txtSpr 
         Height          =   285
         Left            =   1440
         TabIndex        =   40
         Text            =   "txtEmail"
         Top             =   4920
         Width           =   3375
      End
      Begin VB.TextBox txtSiup 
         Height          =   285
         Left            =   1440
         TabIndex        =   39
         Text            =   "txtEmail"
         Top             =   5160
         Width           =   3375
      End
      Begin VB.TextBox txtNPWPKukuh 
         Height          =   285
         Left            =   2400
         TabIndex        =   38
         Text            =   "txtEmail"
         Top             =   1680
         Width           =   3375
      End
      Begin VB.TextBox txtNPWP2 
         Height          =   285
         Left            =   2400
         TabIndex        =   37
         Text            =   "txtEmail"
         Top             =   2760
         Width           =   3375
      End
      Begin VB.TextBox txtNPWPKukuh2 
         Height          =   285
         Left            =   2400
         TabIndex        =   36
         Text            =   "txtEmail"
         Top             =   3960
         Width           =   3375
      End
      Begin MSComCtl2.DTPicker dtpNPWPdate 
         Height          =   375
         Left            =   2400
         TabIndex        =   44
         Top             =   840
         Width           =   2655
         _ExtentX        =   4683
         _ExtentY        =   661
         _Version        =   393216
         CustomFormat    =   "dd MMMM yyyy"
         Format          =   61079555
         CurrentDate     =   38801
      End
      Begin MSComCtl2.DTPicker dtpNPWPkukuh 
         Height          =   375
         Left            =   2400
         TabIndex        =   58
         Top             =   1320
         Width           =   2655
         _ExtentX        =   4683
         _ExtentY        =   661
         _Version        =   393216
         CustomFormat    =   "dd MMMM yyyy"
         Format          =   61079555
         CurrentDate     =   38801
      End
      Begin MSComCtl2.DTPicker dtpNPWPDate2 
         Height          =   375
         Left            =   2400
         TabIndex        =   59
         Top             =   3120
         Width           =   2655
         _ExtentX        =   4683
         _ExtentY        =   661
         _Version        =   393216
         CustomFormat    =   "dd MMMM yyyy"
         Format          =   61079555
         CurrentDate     =   38801
      End
      Begin MSComCtl2.DTPicker dtpNPWPKukuh2 
         Height          =   375
         Left            =   2400
         TabIndex        =   60
         Top             =   3600
         Width           =   2655
         _ExtentX        =   4683
         _ExtentY        =   661
         _Version        =   393216
         CustomFormat    =   "dd MMMM yyyy"
         Format          =   61079555
         CurrentDate     =   38801
      End
      Begin VB.Label Label2 
         Caption         =   "Address :"
         Height          =   255
         Left            =   0
         TabIndex        =   83
         Top             =   6000
         Visible         =   0   'False
         Width           =   975
      End
      Begin VB.Label lblCityID 
         Height          =   255
         Left            =   4440
         TabIndex        =   82
         Top             =   1440
         Width           =   735
      End
      Begin VB.Label Label1 
         Caption         =   "City :"
         Height          =   255
         Left            =   1920
         TabIndex        =   81
         Top             =   5880
         Visible         =   0   'False
         Width           =   855
      End
      Begin VB.Label Label3 
         Caption         =   "Country :"
         Height          =   255
         Left            =   1920
         TabIndex        =   80
         Top             =   6255
         Visible         =   0   'False
         Width           =   975
      End
      Begin VB.Label Label4 
         Caption         =   "Fax"
         Height          =   255
         Left            =   2640
         TabIndex        =   79
         Top             =   1575
         Visible         =   0   'False
         Width           =   1095
      End
      Begin VB.Label Label5 
         Caption         =   "ZipCode :"
         Height          =   255
         Left            =   3720
         TabIndex        =   78
         Top             =   1710
         Visible         =   0   'False
         Width           =   855
      End
      Begin VB.Label Label8 
         Caption         =   "Contact :"
         Height          =   255
         Left            =   3840
         TabIndex        =   77
         Top             =   6120
         Visible         =   0   'False
         Width           =   975
      End
      Begin VB.Label Label9 
         Caption         =   "Email :"
         Height          =   255
         Left            =   240
         TabIndex        =   76
         Top             =   6375
         Visible         =   0   'False
         Width           =   975
      End
      Begin VB.Label Label10 
         Caption         =   "Phone :"
         Height          =   255
         Left            =   2640
         TabIndex        =   75
         Top             =   975
         Visible         =   0   'False
         Width           =   1095
      End
      Begin VB.Label lblCity 
         Height          =   255
         Left            =   4440
         TabIndex        =   74
         Top             =   1470
         Width           =   975
      End
      Begin VB.Label lblCountry 
         Height          =   255
         Left            =   4440
         TabIndex        =   73
         Top             =   1905
         Width           =   855
      End
      Begin VB.Label Label19 
         Caption         =   "NPWP 1 No  :"
         Height          =   255
         Left            =   120
         TabIndex        =   72
         Top             =   495
         Width           =   975
      End
      Begin VB.Label Label21 
         Caption         =   "NPWP 1 Tanggal  :"
         Height          =   255
         Left            =   120
         TabIndex        =   71
         Top             =   840
         Width           =   1335
      End
      Begin VB.Label Label22 
         Caption         =   "Pengukuhan 1  :"
         Height          =   375
         Left            =   120
         TabIndex        =   70
         Top             =   1320
         Width           =   1335
      End
      Begin VB.Label lblCountryID 
         Height          =   255
         Left            =   1920
         TabIndex        =   69
         Top             =   1680
         Width           =   975
      End
      Begin VB.Label Label23 
         Caption         =   "APIT/APIU"
         Height          =   255
         Left            =   120
         TabIndex        =   68
         Top             =   4710
         Width           =   1335
      End
      Begin VB.Label Label24 
         Caption         =   "SPR"
         Height          =   255
         Left            =   120
         TabIndex        =   67
         Top             =   4935
         Width           =   1335
      End
      Begin VB.Label Label25 
         Caption         =   "SIUP"
         Height          =   255
         Left            =   120
         TabIndex        =   66
         Top             =   5175
         Width           =   1335
      End
      Begin VB.Label Label27 
         Caption         =   "No Pengukuhan 1 :"
         Height          =   240
         Left            =   120
         TabIndex        =   65
         Top             =   1695
         Width           =   2175
      End
      Begin VB.Label lblKukuh2tgl 
         Caption         =   "Pengukuhan2  :"
         Height          =   375
         Left            =   120
         TabIndex        =   64
         Top             =   3600
         Width           =   1335
      End
      Begin VB.Label lblNPWP2Tgl 
         Caption         =   "NPWP 2 Tanggal  :"
         Height          =   255
         Left            =   120
         TabIndex        =   63
         Top             =   3120
         Width           =   1335
      End
      Begin VB.Label lblNPWP2 
         Caption         =   "NPWP 2 No  :"
         Height          =   255
         Left            =   120
         TabIndex        =   62
         Top             =   2775
         Width           =   975
      End
      Begin VB.Label lblkukuh2 
         Caption         =   "No Pengukuhan 2  :"
         Height          =   240
         Left            =   120
         TabIndex        =   61
         Top             =   3975
         Width           =   2175
      End
   End
   Begin MSAdodcLib.Adodc adodetail 
      Height          =   330
      Left            =   120
      Top             =   840
      Visible         =   0   'False
      Width           =   1200
      _ExtentX        =   2117
      _ExtentY        =   582
      ConnectMode     =   0
      CursorLocation  =   3
      IsolationLevel  =   -1
      ConnectionTimeout=   15
      CommandTimeout  =   30
      CursorType      =   3
      LockType        =   3
      CommandType     =   8
      CursorOptions   =   0
      CacheSize       =   50
      MaxRecords      =   0
      BOFAction       =   0
      EOFAction       =   0
      ConnectStringType=   1
      Appearance      =   1
      BackColor       =   -2147483643
      ForeColor       =   -2147483640
      Orientation     =   0
      Enabled         =   -1
      Connect         =   ""
      OLEDBString     =   ""
      OLEDBFile       =   ""
      DataSourceName  =   ""
      OtherAttributes =   ""
      UserName        =   ""
      Password        =   ""
      RecordSource    =   ""
      Caption         =   "Adodc1"
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      _Version        =   393216
   End
   Begin MSAdodcLib.Adodc adolist 
      Height          =   330
      Left            =   120
      Top             =   1200
      Visible         =   0   'False
      Width           =   1200
      _ExtentX        =   2117
      _ExtentY        =   582
      ConnectMode     =   0
      CursorLocation  =   3
      IsolationLevel  =   -1
      ConnectionTimeout=   15
      CommandTimeout  =   30
      CursorType      =   3
      LockType        =   3
      CommandType     =   8
      CursorOptions   =   0
      CacheSize       =   50
      MaxRecords      =   0
      BOFAction       =   0
      EOFAction       =   0
      ConnectStringType=   1
      Appearance      =   1
      BackColor       =   -2147483643
      ForeColor       =   -2147483640
      Orientation     =   0
      Enabled         =   -1
      Connect         =   ""
      OLEDBString     =   ""
      OLEDBFile       =   ""
      DataSourceName  =   ""
      OtherAttributes =   ""
      UserName        =   ""
      Password        =   ""
      RecordSource    =   ""
      Caption         =   "Adodc2"
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      _Version        =   393216
   End
   Begin MSAdodcLib.Adodc adoFind 
      Height          =   330
      Left            =   120
      Top             =   1560
      Visible         =   0   'False
      Width           =   1215
      _ExtentX        =   2143
      _ExtentY        =   582
      ConnectMode     =   0
      CursorLocation  =   3
      IsolationLevel  =   -1
      ConnectionTimeout=   15
      CommandTimeout  =   30
      CursorType      =   3
      LockType        =   3
      CommandType     =   8
      CursorOptions   =   0
      CacheSize       =   50
      MaxRecords      =   0
      BOFAction       =   0
      EOFAction       =   0
      ConnectStringType=   1
      Appearance      =   1
      BackColor       =   -2147483643
      ForeColor       =   -2147483640
      Orientation     =   0
      Enabled         =   -1
      Connect         =   ""
      OLEDBString     =   ""
      OLEDBFile       =   ""
      DataSourceName  =   ""
      OtherAttributes =   ""
      UserName        =   ""
      Password        =   ""
      RecordSource    =   ""
      Caption         =   "Adodc2"
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Arial Narrow"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      _Version        =   393216
   End
   Begin VB.Label Label32 
      BackColor       =   &H00D6BD7B&
      BackStyle       =   0  'Transparent
      Caption         =   "# 3 character"
      Height          =   255
      Left            =   2760
      TabIndex        =   87
      Top             =   2640
      Width           =   1455
   End
   Begin VB.Label lblHeader 
      BackColor       =   &H00D6BD7B&
      BackStyle       =   0  'Transparent
      Caption         =   "Customer Detail"
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   30
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H0080FFFF&
      Height          =   735
      Left            =   360
      TabIndex        =   86
      Top             =   120
      Width           =   6015
   End
   Begin VB.Label Label26 
      BackColor       =   &H00D6BD7B&
      BackStyle       =   0  'Transparent
      Caption         =   "Initial :"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   255
      Left            =   360
      TabIndex        =   85
      Top             =   2640
      Width           =   1455
   End
   Begin VB.Label Label7 
      BackColor       =   &H00D6BD7B&
      BackStyle       =   0  'Transparent
      Caption         =   "Customer Name :"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   255
      Left            =   360
      TabIndex        =   4
      Top             =   2280
      Width           =   1455
   End
   Begin VB.Label Label6 
      BackColor       =   &H00D6BD7B&
      BackStyle       =   0  'Transparent
      Caption         =   "Customer ID :"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   255
      Left            =   360
      TabIndex        =   3
      Top             =   1920
      Width           =   1455
   End
   Begin VB.Image Image1 
      Height          =   1815
      Left            =   360
      Picture         =   "frmCustomer.frx":4F4C
      Stretch         =   -1  'True
      Top             =   0
      Width           =   10575
   End
End
Attribute VB_Name = "frmCustomer"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Dim strCustomerOld As String
Dim rsmenu As ADODB.Recordset
Dim rsSave As ADODB.Recordset
Dim rsSaveDate As ADODB.Recordset
Dim rsDetail As ADODB.Recordset
Dim msgpil As Integer
Dim TypeSave As Byte
Dim saveoke As Boolean
Dim VarSelection As Variant
Dim grdListNo As Integer
Dim varlong As Integer
Dim strModul As String
Dim strTableH As String
Dim mainID As String
Dim LenSaveID As Integer
Dim SaveIDCounter As Long


Private Sub cmdAdd_Click()
saveoke = False
 TypeSave = 1
'  addSetUp
  
 textActive Me, True
 dtpValue Me, Now
  chkActive.Enabled = True
  chkActive.Value = 1
'txtPartnerID.Enabled = False
 
 dtpNPWPdate.Enabled = True
dtpNPWPkukuh.Enabled = True
dtpNPWPKukuh2.Enabled = True
dtpNPWPDate2.Enabled = True
 dtpNPWPdate.Value = Date
dtpNPWPkukuh.Value = Date
dtpNPWPKukuh2.Value = Date
dtpNPWPDate2.Value = Date

lblNPWP2.Visible = True
lblNPWP2Tgl.Visible = True
lblkukuh2.Visible = True
lblKukuh2tgl.Visible = True
txtNPWPKukuh2.Visible = True
txtNPWP2.Visible = True
dtpNPWPKukuh2.Visible = True
dtpNPWPDate2.Visible = True

ButtonAdd Me
txtPartnerID.SetFocus
'txtPartnerName.SetFocus
End Sub

Private Sub cmdCancel_Click()
dtpNPWPdate.Enabled = False
dtpNPWPkukuh.Enabled = False
dtpNPWPDate2.Enabled = False
dtpNPWPKukuh2.Enabled = False
textBlank Me
chkActive.Enabled = False
If TypeSave < 2 Then
ButtonCancel1 Me
 txtCorCity.Enabled = True
 txtCity.Enabled = True
 txtCorCountry.Enabled = True
 txtCountry.Enabled = True
 txtPartnerName.Enabled = True

  adoFind.RecordSource = "SELECT * from " & strTableH & " where partnerID='' "
  adoFind.Refresh
End If

If TypeSave = 2 Then
ButtonCancel2 Me
  textActive Me, False
End If
 
 TypeSave = 0
 find_dblclick
 saveoke = True

End Sub


Private Sub cmdDelete_Click()
msgpil = (MsgBox("Are you sure want Delete ?", vbYesNo, "Your Data Will Delete"))
 If msgpil <> 6 Then Exit Sub
 TypeSave = 2
strCustomerOld = Trim(txtPartnerID.Text)
  If rsSave.State = adStateOpen Then rsSave.Close
  rsSave.Source = "select * from " & strTableH & " where partnerID='" & mainID & gOffCode & strCustomerOld & "'"
  rsSave.Open
  rsSave.MoveFirst
'  Urut = Right(rsSave!userGroupID, 4)
  conn.BeginTrans
  rsSave.Delete
  rsSave.UpdateBatch adAffectCurrent

  conn.CommitTrans
  ButtonDelete Me
  textActive Me, False
  textBlank Me
  TypeSave = 0
  adoFind.Refresh
  find_dblclick

End Sub

Private Sub cmdEdit_Click()
saveoke = False
strCustomerOld = txtPartnerID.Text

textActive Me, True
chkActive.Enabled = True


ButtonEdit Me

 TypeSave = 2

'txtPartnerID.Enabled = False
 dtpNPWPdate.Enabled = True
dtpNPWPkukuh.Enabled = True
dtpNPWPDate2.Enabled = True
dtpNPWPKukuh2.Enabled = True

lblNPWP2.Visible = True
lblNPWP2Tgl.Visible = True
lblkukuh2.Visible = True
lblKukuh2tgl.Visible = True
txtNPWPKukuh2.Visible = True
txtNPWP2.Visible = True
dtpNPWPKukuh2.Visible = True
dtpNPWPDate2.Visible = True

' dtpDate.Enabled = True
' dtpDueDate.Enabled = True
End Sub

Private Sub cmdExit_Click()
Unload Me
End Sub

Private Sub cmdFind_Click()
 grdFind
End Sub

Private Sub cmdfirst_Click()
adoFind.Recordset.MoveFirst
find_dblclick
End Sub

Private Sub cmdLast_Click()
adoFind.Recordset.MoveLast
find_dblclick
End Sub

Private Sub cmdNext_Click()
If Abs(adoFind.Recordset.AbsolutePosition) < adoFind.Recordset.RecordCount Then
 adoFind.Recordset.MoveNext
 find_dblclick
End If
End Sub

Private Sub cmdPrev_Click()
If Abs(adoFind.Recordset.AbsolutePosition) > 1 Then
adoFind.Recordset.MovePrevious
find_dblclick
End If
End Sub

Private Sub cmdPrint_Click()
Dim ofrmPrintMaster As New frmPrintMaster
 Dim msgpil As Byte
 If TypeSave > 0 Then
  msgpil = (MsgBox("Save? ", vbYesNo))
  If msgpil = 6 Then
     cmdSave_Click
     If TypeSave > 0 Then GoTo cancelprint
    Else
     GoTo cancelprint
  End If
 End If
If saveoke = False Then GoTo cancelprint

ofrmPrintMaster.Show vbModal
 Dim rslist As ADODB.Recordset
 Dim sData As Boolean
 Dim sAll As Boolean
 Dim report1 As New CRAXDRT.Report
 Dim subreport1 As CRAXDRT.SubreportObject
 Dim rptApp As CRAXDRT.Application
' Dim formula As CRAXDRT.FormulaFieldDefinition
 Dim rptView As New frmRptView
 'Load rptView
 Set rptApp = New CRAXDRT.Application
 Set rslist = New ADODB.Recordset
 rslist.ActiveConnection = conn
 rslist.CursorType = adOpenDynamic
 rslist.LockType = adLockBatchOptimistic
 rslist.CursorLocation = adUseClient
  If rslist.State = adStateOpen Then rslist.Close

 If ofrmPrintMaster.oData = True Then
   rslist.Source = adoFind.Recordset.Source & _
   " and " & strTableH & ".partnerid = '" & adoFind.Recordset!PartnerID & "' "
  Else
   rslist.Source = adoFind.Recordset.Source
'//  rsList.Source = " SELECT " & strTableH & ".*, City.Name AS City, Country.Name AS Country, CorCity.Name AS CorCity, CorCountry.Name AS CorCountry " & _
  " FROM ((" & strTableH & " LEFT OUTER JOIN City ON " & strTableH & ".CityID=City.CityID) LEFT OUTER JOIN Country ON City.countryID=Country.CountryID) LEFT OUTER JOIN (City AS CorCity LEFT OUTER JOIN Country AS CorCountry ON CorCity.countryID=CorCountry.CountryID) ON " & strTableH & ".CorCityID=CorCity.CityID "

 End If
rslist.Open
 Set report1 = rptApp.OpenReport(App.Path & "\report\customerdata.rpt")
 
 report1.Database.SetDataSource rslist
 
 'ConnectReportToDB Report
 'ConnectReportToDB subReport
 'Set formulas = reportView.Report.FormulaFields
 'For Each formula In report1.FormulaFields
             ' If (rptParameter.Name = "{?pMinDate}") Then
                '  rptParameter.AddCurrentValue CDate(frm_OutFlow_SelectPeriod.DTPicker1.Value)
             ' ElseIf (rptParameter.Name = "{?pMaxDate}") Then
               '   rptParameter.AddCurrentValue CDate(frm_OutFlow_SelectPeriod.DTPicker2.Value)
             ' End If

 'Next
 '   Screen.MousePointer = vbHourglass
 '   rptview.CRViewer1.ReportSource = Report
 '   CRViewer1.ViewReport
 '   Screen.MousePointer = vbDefault

rptView.Show
report1.PrinterSetup 0
rptView.CRViewer1.ReportSource = report1
rptView.CRViewer1.ViewReport
rptView.CRViewer1.Zoom (1)
cancelprint:
End Sub

Private Sub cmdSave_Click()
Dim DateSave As Date
Dim MsgID As String
If Trim(txtPartnerName.Text) = "" Then
  MsgBox "Partner Name Still Empty ", vbOKOnly
  GoTo cancelsave
End If
If Len(Trim(txtIdent.Text)) < 3 Then
  MsgBox "Intials Must 3 Character ", vbOKOnly
  txtIdent.SetFocus
  GoTo cancelsave
End If

MsgID = "Partner ID"
msgpil = (MsgBox(gMsgQsavePrompt, vbYesNo, gMsgQsaveTitle))
 If msgpil <> 6 Then GoTo cancelsave

Dim Urut As String
Dim DateTran As Date
On Error GoTo errorExesave
LoopSaveUlang:

 If TypeSave = 2 Then
 Urut = mainID & gOffCode & txtPartnerID.Text
  If mainID & gOffCode & strCustomerOld <> Urut Then
   adoList.RecordSource = " select * from " & strTableH & " where partnerid='" & Urut & "'"
   adoList.Refresh
   If adoList.Recordset.RecordCount <> 0 Then
    MsgBox MsgID + " Available", vbOKOnly, MsgID + " Allready Input"
    GoTo cancelsave
   End If
  End If
 adoList.RecordSource = " select * from " & strTableH & " where right(left(partnerid," & gLenOffCode + Len(mainID) & ")," & gLenOffCode & ")='" & gOffCode & "' and Ident='" & txtIdent.Text & "' and partnerid<>'" & mainID & gOffCode & strCustomerOld & "' and partnerid<>'" & Urut & "'  order by right(partnerid," & LenSaveID & ")"
 adoList.Refresh
 If adoList.Recordset.RecordCount <> 0 Then
    MsgBox MsgID + " Change Initials ", vbOKOnly, MsgID + " Initial Allready Input"
    GoTo cancelsave
 End If
  If rsSave.State = adStateOpen Then rsSave.Close
  rsSave.Source = "select * from " & strTableH & " where partnerID='" & mainID & gOffCode & strCustomerOld & "'"
  rsSave.Open
  rsSave.MoveFirst
'  Urut = Right(rsSave!userGroupID, 4)
  conn.BeginTrans
  
 End If
 If TypeSave = 1 Then
 If txtPartnerID.Text = "" Then
'Otomatis
 adoList.RecordSource = " select * from " & strTableH & " where right(left(partnerid," & gLenOffCode + Len(mainID) & ")," & gLenOffCode & ")='" & gOffCode & "' and Ident='" & txtIdent.Text & "' order by right(partnerid," & gLenOffCode + Len(mainID) & ")"
 adoList.Refresh
 If adoList.Recordset.RecordCount <> 0 Then
    MsgBox MsgID + " Change Initials ", vbOKOnly, MsgID + " Initial Allready Input"
    GoTo cancelsave
 End If
 adoList.RecordSource = " select * from " & strTableH & " where right(left(partnerid," & gLenOffCode + Len(mainID) & ")," & gLenOffCode & ")='" & gOffCode & "' order by right(partnerid," & LenSaveID & ")"
 adoList.Refresh
 If adoList.Recordset.RecordCount <> 0 Then
   adoList.Recordset.MoveLast
   Urut = mainID & Trim(gOffCode) & Right(SaveIDCounter + Abs(Right(adoList.Recordset!PartnerID, 4)), LenSaveID)
  Else
    Urut = mainID & Trim(gOffCode) & Right(SaveIDCounter, LenSaveID)
 End If
 txtPartnerID.Text = Urut
 
 
 Else
 '//Manual
 If Len(Trim(txtPartnerID.Text)) < LenSaveID Then
   MsgBox "ID " & LenSaveID & "Digits ", vbOKOnly
   GoTo cancelsave
 End If
  Urut = mainID & Trim(gOffCode) & txtPartnerID.Text
 adoList.RecordSource = " select * from " & strTableH & " where right(left(partnerid," & gLenOffCode + Len(mainID) & ")," & gLenOffCode & ")='" & gOffCode & "' and Ident='" & txtIdent.Text & "' order by right(partnerid," & gLenOffCode + Len(mainID) & ")"
 adoList.Refresh
 If adoList.Recordset.RecordCount <> 0 Then
    MsgBox MsgID + " Change Initials ", vbOKOnly, MsgID + " Initial Allready Input"
    GoTo cancelsave
 End If
 adoList.RecordSource = " select * from " & strTableH & " where partnerid='" & Urut & "' "
 adoList.Refresh
 If adoList.Recordset.RecordCount <> 0 Then
    MsgBox MsgID + " ID Sudah Ada ", vbOKOnly, MsgID + " ID Allready Input"
    GoTo cancelsave
 End If
 End If
'//
'//Manual
 '  adoList.RecordSource = " select * from Customer where partnerID='" + txtPartnerID.Text + "'"
 '  adoList.Refresh
 '  If adoList.Recordset.RecordCount <> 0 Then
 '   MsgBox MsgID + " Available", vbOKOnly, MsgID + " Allready Input"
 '   GoTo cancelsave
 '  End If
 '//
  If rsSave.State = adStateOpen Then rsSave.Close
  rsSave.Source = " select * from " & strTableH & " where  partnerID=''"
  rsSave.Open
  conn.BeginTrans
  If rsSave.RecordCount <> 0 Then
    rsSave.MoveFirst
   Else
    rsSave.AddNew
  End If
 End If

' adoFind.Recordset!offcode = Left(gKtrAs, 4)
rsSave!PartnerID = Urut
rsSave!PartnerName = Trim(txtPartnerName.Text)
rsSave!Ident = Trim(txtIdent.Text)

'//Correspndence
rsSave!CorAdd1 = Trim(txtCorAdd1.Text)
rsSave!CorAdd2 = txtCorAdd2.Text
rsSave!CorAdd3 = Trim(txtCorAdd3.Text)
rsSave!CorAdd4 = txtCorAdd4.Text
rsSave!Corphone1 = txtCorPhone1.Text
rsSave!Corphone2 = txtCorPhone2.Text
rsSave!Corfax1 = txtCorFax1.Text
rsSave!Corfax2 = txtCorFax2.Text
rsSave!corcityID = lblCorCity.Caption
rsSave!CorcountryID = lblCorCountry.Caption
rsSave!CorZipcode = txtCorZipCode.Text
rsSave!Coremail = txtCorEmail.Text
rsSave!corcontact1 = txtCorContact1.Text
rsSave!corcontact2 = txtCorContact2.Text
rsSave!Note1 = txtNote1.Text
rsSave!Note2 = txtNote2.Text
rsSave!active = chkActive.Value

'//Company
rsSave!Address1 = Trim(txtaddress1.Text)
rsSave!Address2 = txtaddress2.Text
rsSave!Address3 = Trim(txtaddress3.Text)
rsSave!Address4 = txtaddress4.Text
rsSave!Phone1 = txtPhone1.Text
rsSave!phone2 = txtPhone2.Text
rsSave!fax1 = txtFax1.Text
rsSave!fax2 = txtFax2.Text
rsSave!cityID = lblCityID.Caption
rsSave!countryID = lblCountryID.Caption
rsSave!email = txtEmail.Text
rsSave!contact1 = txtContact1.Text
rsSave!contact2 = txtContact2.Text
rsSave!NPWP = txtNPWP.Text
rsSave!NPWPDate = dtpNPWPdate.Value
rsSave!NPWPdatekukuh = dtpNPWPkukuh.Value
rsSave!NPWPkukuh = txtNPWPKukuh.Text

rsSave!NPWP1 = txtNPWP2.Text
rsSave!NPWPDate1 = dtpNPWPDate2.Value
rsSave!NPWPdatekukuh1 = dtpNPWPKukuh2.Value
rsSave!NPWPkukuh1 = txtNPWPKukuh2.Text

rsSave!Apitu = txtApitu.Text
rsSave!spr = txtSpr.Text
rsSave!siup = txtSiup.Text

rsSave.UpdateBatch adAffectCurrent

conn.CommitTrans

On Error GoTo 0
If TypeSave = 2 Then
adoFind.Refresh
adoFind.Recordset.Find "PartnerID='" & Urut & "' "
Else
adoFind.RecordSource = " SELECT " & strTableH & ".*, City.Name AS City, Country.Name AS Country, CorCity.Name AS CorCity, CorCountry.Name AS CorCountry " & _
  " FROM ((" & strTableH & " LEFT OUTER JOIN City ON " & strTableH & ".CityID=City.CityID) LEFT OUTER JOIN Country ON City.countryID=Country.CountryID) LEFT OUTER JOIN (City AS CorCity LEFT OUTER JOIN Country AS CorCountry ON CorCity.countryID=CorCountry.CountryID) ON " & strTableH & ".CorCityID=CorCity.CityID " & _
  " where partnerid <>'' and partnerid ='" & Urut & "'"
adoFind.Refresh
End If

TypeSave = 0
saveoke = True

cmdSave.Enabled = False
 find_dblclick

GoTo cancelsave
errorExesave:
conn.RollbackTrans
GoTo LoopSaveUlang
If Err.Number = -2147467259 Then
MsgBox "" & strTableH & " ID Available", vbOKOnly, Err.Number
Else
MsgBox "Error", vbOKOnly, Err.Number
End If
saveoke = False
cancelsave:
If rsDetail.State = adStateOpen Then rsDetail.Close
If rsSave.State = adStateOpen Then rsSave.Close

On Error GoTo 0
End Sub



Private Sub Form_Load()
BackFormColor Me
strTableH = "Customer"
mainID = "C"
LenSaveID = 6
SaveIDCounter = 1000001
txtPartnerID.MaxLength = LenSaveID
    Set rsmenu = New ADODB.Recordset
    Set rsmenu.ActiveConnection = conn
    rsmenu.CursorType = adOpenStatic
 ButtonSet Me
 grdListNo = 0
 Set rsSave = New ADODB.Recordset
 rsSave.ActiveConnection = conn
 rsSave.CursorType = adOpenDynamic
 rsSave.LockType = adLockBatchOptimistic
 rsSave.CursorLocation = adUseClient
 
 Set rsSaveDate = New ADODB.Recordset
 rsSaveDate.ActiveConnection = conn
 rsSaveDate.CursorType = adOpenKeyset
 rsSaveDate.LockType = adLockPessimistic
 rsSaveDate.CursorLocation = adUseServer
 
 
 Set rsDetail = New ADODB.Recordset
 rsDetail.ActiveConnection = conn
 rsDetail.CursorType = adOpenDynamic
 rsDetail.LockType = adLockBatchOptimistic
 rsDetail.CursorLocation = adUseClient
 
   adoList.CommandType = adCmdUnknown
   adoList.ConnectionString = ConnStr
   adoList.CursorLocation = adUseClient
   adoList.LockType = adLockReadOnly
   adoList.CursorType = adOpenStatic
   
   adoFind.CommandType = adCmdUnknown
   adoFind.ConnectionString = ConnStr
   adoFind.CursorLocation = adUseClient
   adoFind.LockType = adLockReadOnly
   adoFind.CursorType = adOpenStatic
   
   textActive Me, False
   grdListNo = 0
   TypeSave = 0
   dtpNPWPdate.Enabled = False
dtpNPWPkukuh.Enabled = False
saveoke = True
TypeSave = 0
   cmdCancel_Click
adoFind.RecordSource = "select * from " & strTableH & " where partnerID=''"
adoFind.Refresh

'cmdCancel_Click

find_dblclick

End Sub


Private Sub grdListFind_DblClick()
If adoFind.Recordset.RecordCount <> 0 Then find_dblclick
grdListFind_LostFocus

End Sub

Private Sub grdListFind_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then
       If adoFind.Recordset.RecordCount <> 0 Then
         find_dblclick
         grdListFind_LostFocus
       End If
    End If
    If KeyAscii = 27 Then
         GrdList_LostFocus
         cmdCancel.SetFocus
    End If
cancelFind:

End Sub

Private Sub grdListFind_LostFocus()
grdListFind.Enabled = False
grdListFind.Visible = False
End Sub

Private Sub grdlist_DblClick()
If adoList.Recordset.RecordCount <> 0 Then
 If grdListNo = 1 Then City_dblclick
 If grdListNo = 2 Then country_dblclick
 If grdListNo = 3 Then CorCity_dblclick
 If grdListNo = 4 Then Corcountry_dblclick
End If
GrdList_LostFocus
grdlistHide
End Sub

Private Sub grdlist_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then
       grdlist_DblClick
       GoTo cancellist
    End If
        'If rsList.State = adStateOpen Then rsList.Close
    If KeyAscii = 27 Then
         GrdList_LostFocus
         GoTo cancellist
    End If
Exit Sub

cancellist:
grdlistHide
End Sub

Private Sub GrdList_LostFocus()
      GrdList.Enabled = False
      GrdList.Visible = False
      grdlistHide
End Sub
Sub grdlistHide()
 If grdListNo = 1 Then txtCity.SetFocus
 If grdListNo = 2 Then txtCountry.SetFocus
 If grdListNo = 3 Then txtCorCity.SetFocus
 If grdListNo = 4 Then txtCorCountry.SetFocus
 grdListNo = 0
End Sub


Sub grdCountry()
 VarSelection = Replace(Trim(txtCountry.Text), "'", "''") & "%"
 varlong = Len(Trim(VarSelection))
 If txtCountry.Text = "" Then
   adoList.RecordSource = "select * from country"
  Else
   adoList.RecordSource = "select * from country where left(name,'" & varlong & "') like '" & VarSelection & "'"
 End If
 adoList.Refresh
 grdListNo = 2
GrdListShow Me, lblCountryID.Left, txtCountry.Top, 3000, 3000
End Sub
Sub grdCorCountry()
 VarSelection = Replace(Trim(txtCorCountry.Text), "'", "''") & "%"
 varlong = Len(Trim(VarSelection))
 If txtCountry.Text = "" Then
   adoList.RecordSource = "select * from country"
  Else
   adoList.RecordSource = "select * from country where left(name,'" & varlong & "') like '" & VarSelection & "'"
 End If
 adoList.Refresh
 grdListNo = 4
GrdListShow Me, txtCorCountry.Left, txtCorCountry.Top, 3000, 3000
End Sub

Sub grdcity()
 VarSelection = Replace(Trim(txtCity.Text), "'", "''") & "%"
 varlong = Len(Trim(VarSelection))
 If Trim(txtCity.Text) = "" Then
   adoList.RecordSource = "select * from city"
  Else
   adoList.RecordSource = "select * from city where  left(name,'" & varlong & "') like '" & VarSelection & "'"
 End If

 adoList.Refresh
 grdListNo = 1
 GrdList.ClearFields
GrdListShow Me, lblCityID.Left, txtCity.Left, 3000, 3000
 End Sub
 
Sub grdCorcity()
 VarSelection = Replace(Trim(txtCorCity.Text), "'", "''") & "%"
 varlong = Len(Trim(VarSelection))
 If txtCity.Text = "" Then
   adoList.RecordSource = "select * from city"
  Else
   adoList.RecordSource = "select * from city where  left(name,'" & varlong & "') like '" & VarSelection & "'"
 End If

 adoList.Refresh
 grdListNo = 3
GrdListShow Me, txtCorCity.Left, txtCorCity.Top, 3000, 3000
 End Sub
 

Sub find_dblclick()
saveoke = True
' dtpDate.Enabled = False
' dtpDueDate.Enabled = False

' If adoFind.Recordset!offcode <> Left(gKtrAs, 4) Then
'  cmdEdit.Enabled = False
' Else
  cmdEdit.Enabled = True
' End If
dtpNPWPdate.Enabled = False
dtpNPWPkukuh.Enabled = False
dtpNPWPDate2.Enabled = False
dtpNPWPKukuh2.Enabled = False
If adoFind.Recordset.RecordCount <> 0 Then
 textActive Me, False
 chkActive.Enabled = False
 If IsNull(adoFind.Recordset!PartnerID) Then txtPartnerID.Text = "" Else txtPartnerID.Text = Right(adoFind.Recordset!PartnerID, LenSaveID)
 If IsNull(adoFind.Recordset!PartnerName) Then txtPartnerName.Text = "" Else txtPartnerName.Text = adoFind.Recordset!PartnerName
 If IsNull(adoFind.Recordset!Ident) Then txtIdent.Text = "" Else txtIdent.Text = adoFind.Recordset!Ident

'//Correspondence
 If IsNull(adoFind.Recordset!CorAdd1) Then txtCorAdd1.Text = "" Else txtCorAdd1.Text = adoFind.Recordset!CorAdd1
 If IsNull(adoFind.Recordset!CorAdd2) Then txtCorAdd2.Text = "" Else txtCorAdd2.Text = adoFind.Recordset!CorAdd2
 If IsNull(adoFind.Recordset!CorAdd3) Then txtCorAdd3.Text = "" Else txtCorAdd3.Text = adoFind.Recordset!CorAdd3
 If IsNull(adoFind.Recordset!CorAdd4) Then txtCorAdd4.Text = "" Else txtCorAdd4.Text = adoFind.Recordset!CorAdd4
 If IsNull(adoFind.Recordset!Corphone1) Then txtCorPhone1.Text = "" Else txtCorPhone1.Text = adoFind.Recordset!Corphone1
 If IsNull(adoFind.Recordset!Corphone2) Then txtCorPhone2.Text = "" Else txtCorPhone2.Text = adoFind.Recordset!Corphone2
 If IsNull(adoFind.Recordset!CorZipcode) Then txtCorZipCode.Text = "" Else txtCorZipCode.Text = adoFind.Recordset!CorZipcode
 If IsNull(adoFind.Recordset!Corfax1) Then txtCorFax1.Text = "" Else txtCorFax1.Text = adoFind.Recordset!Corfax1
 If IsNull(adoFind.Recordset!Corfax2) Then txtCorFax2.Text = "" Else txtCorFax2.Text = adoFind.Recordset!Corfax2
 If IsNull(adoFind.Recordset!corcityID) Then
   lblCorCity.Caption = ""
   txtCorCity.Text = ""
  Else
   lblCorCity.Caption = adoFind.Recordset!corcityID
   adoList.RecordSource = "select * from City where Cityid like '" & adoFind.Recordset!corcityID & "'"
   adoList.Refresh
   If adoList.Recordset.RecordCount <> 0 Then
     adoList.Recordset.MoveFirst
     txtCorCity.Text = adoList.Recordset!Name
    Else
     lblCorCity.Caption = ""
     txtCorCity.Text = ""
   End If
 End If
 If IsNull(adoFind.Recordset!CorcountryID) Then
   lblCorCountry.Caption = ""
   txtCorCountry.Text = ""
  Else
   lblCorCountry.Caption = adoFind.Recordset!CorcountryID
      adoList.RecordSource = "select * from country where countryid like '" & adoFind.Recordset!CorcountryID & "'"
      adoList.Refresh
   If adoList.Recordset.RecordCount <> 0 Then
     adoList.Recordset.MoveFirst
     txtCorCountry.Text = adoList.Recordset!Name
    Else
     lblCorCountry.Caption = ""
     txtCorCountry.Text = ""
   End If
 End If
 If IsNull(adoFind.Recordset!corcontact1) Then txtCorContact1.Text = "" Else txtCorContact1.Text = adoFind.Recordset!corcontact1
 If IsNull(adoFind.Recordset!corcontact2) Then txtCorContact2.Text = "" Else txtCorContact2.Text = adoFind.Recordset!corcontact2
 If IsNull(adoFind.Recordset!Coremail) Then txtCorEmail.Text = "" Else txtCorEmail.Text = adoFind.Recordset!Coremail
 If IsNull(adoFind.Recordset!Note1) Then txtNote1.Text = "" Else txtNote1.Text = adoFind.Recordset!Note1
 If IsNull(adoFind.Recordset!Note2) Then txtNote2.Text = "" Else txtNote2.Text = adoFind.Recordset!Note2
 If IsNull(adoFind.Recordset!active) Or adoFind.Recordset!active <> "1" Then chkActive.Value = 0 Else chkActive.Value = adoFind.Recordset!active

'//Company
 If IsNull(adoFind.Recordset!Address1) Then txtaddress1.Text = "" Else txtaddress1.Text = adoFind.Recordset!Address1
 If IsNull(adoFind.Recordset!Address2) Then txtaddress2.Text = "" Else txtaddress2.Text = adoFind.Recordset!Address2
 If IsNull(adoFind.Recordset!Address3) Then txtaddress3.Text = "" Else txtaddress3.Text = adoFind.Recordset!Address3
 If IsNull(adoFind.Recordset!Address4) Then txtaddress4.Text = "" Else txtaddress4.Text = adoFind.Recordset!Address4
 If IsNull(adoFind.Recordset!Phone1) Then txtPhone1.Text = "" Else txtPhone1.Text = adoFind.Recordset!Phone1
 If IsNull(adoFind.Recordset!phone2) Then txtPhone2.Text = "" Else txtPhone2.Text = adoFind.Recordset!phone2
 If IsNull(adoFind.Recordset!fax1) Then txtFax1.Text = "" Else txtFax1.Text = adoFind.Recordset!fax1
 If IsNull(adoFind.Recordset!fax2) Then txtFax2.Text = "" Else txtFax2.Text = adoFind.Recordset!fax2
 If IsNull(adoFind.Recordset!cityID) Then
   lblCityID.Caption = ""
   txtCity.Text = ""
  Else
   lblCityID.Caption = adoFind.Recordset!cityID
   adoList.RecordSource = "select * from city where cityid like '" & adoFind.Recordset!cityID & "'"
   adoList.Refresh
   If adoList.Recordset.RecordCount <> 0 Then
     adoList.Recordset.MoveFirst
     txtCity.Text = adoList.Recordset!Name
    Else
     lblCityID.Caption = ""
     txtCity.Text = ""
   End If
 End If
 If IsNull(adoFind.Recordset!countryID) Then
   lblCountryID.Caption = ""
   txtCountry.Text = ""
  Else
   lblCountryID.Caption = adoFind.Recordset!countryID
      adoList.RecordSource = "select * from country where countryid like '" & adoFind.Recordset!countryID & "'"
      adoList.Refresh
   If adoList.Recordset.RecordCount <> 0 Then
     adoList.Recordset.MoveFirst
     txtCountry.Text = adoList.Recordset!Name
    Else
     lblCountryID.Caption = ""
     txtCountry.Text = ""
   End If
 End If
 If IsNull(adoFind.Recordset!contact1) Then txtContact1.Text = "" Else txtContact1.Text = adoFind.Recordset!contact1
 If IsNull(adoFind.Recordset!contact2) Then txtContact2.Text = "" Else txtContact2.Text = adoFind.Recordset!contact2
 If IsNull(adoFind.Recordset!email) Then txtEmail.Text = "" Else txtEmail.Text = adoFind.Recordset!email
 If IsNull(adoFind.Recordset!NPWP) Then txtNPWP.Text = "" Else txtNPWP.Text = adoFind.Recordset!NPWP
 If IsNull(adoFind.Recordset!NPWPDate) Then dtpNPWPdate.Value = Date Else dtpNPWPdate.Value = adoFind.Recordset!NPWPDate
 If IsNull(adoFind.Recordset!NPWPdatekukuh) Then dtpNPWPkukuh.Value = Date Else dtpNPWPkukuh.Value = adoFind.Recordset!NPWPdatekukuh
  If IsNull(adoFind.Recordset!NPWPkukuh) Then txtNPWPKukuh.Text = "" Else txtNPWPKukuh.Text = adoFind.Recordset!NPWPkukuh

 
 If IsNull(adoFind.Recordset!NPWP1) Then txtNPWP2.Text = "" Else txtNPWP2.Text = adoFind.Recordset!NPWP1
 If IsNull(adoFind.Recordset!NPWPDate1) Then dtpNPWPDate2.Value = Date Else dtpNPWPDate2.Value = adoFind.Recordset!NPWPDate1
 If IsNull(adoFind.Recordset!NPWPdatekukuh1) Then dtpNPWPKukuh2.Value = Date Else dtpNPWPKukuh2.Value = adoFind.Recordset!NPWPdatekukuh1
 If IsNull(adoFind.Recordset!NPWPkukuh1) Then txtNPWPKukuh2.Text = "" Else txtNPWPKukuh2.Text = adoFind.Recordset!NPWPkukuh1
 If IsNull(adoFind.Recordset!Apitu) Then txtApitu.Text = "" Else txtApitu.Text = adoFind.Recordset!Apitu
 If IsNull(adoFind.Recordset!spr) Then txtSpr.Text = "" Else txtSpr.Text = adoFind.Recordset!spr
 If IsNull(adoFind.Recordset!siup) Then txtSiup.Text = "" Else txtSiup.Text = adoFind.Recordset!siup

lblNPWP2.Visible = True
lblNPWP2Tgl.Visible = True
lblkukuh2.Visible = True
lblKukuh2tgl.Visible = True
txtNPWPKukuh2.Visible = True
txtNPWP2.Visible = True
dtpNPWPKukuh2.Visible = True
dtpNPWPDate2.Visible = True

If IsNull(adoFind.Recordset!NPWP1) Or Trim(adoFind.Recordset!NPWP1) = "" Then
lblNPWP2.Visible = False
lblNPWP2Tgl.Visible = False
lblkukuh2.Visible = False
lblKukuh2tgl.Visible = False
txtNPWPKukuh2.Visible = False
txtNPWP2.Visible = False
dtpNPWPKukuh2.Visible = False
dtpNPWPDate2.Visible = False
End If

  cmdFind.Enabled = False
  cmdAdd.Enabled = False
  cmdEdit.Enabled = True
  cmdPrint.Enabled = True
  cmdDelete.Enabled = True
'//
 Else
  cmdFind.Enabled = True
  cmdAdd.Enabled = True
  cmdEdit.Enabled = False
  cmdPrint.Enabled = False
  cmdDelete.Enabled = False

End If
' If IsNull(adoFind.Recordset!duedate) Then dtpDueDate.Value = Date Else dtpDueDate.Value = adoFind.Recordset!duedate
 '//invoiceDetail
 
 If Abs(adoFind.Recordset.RecordCount) > 1 Then
   cmdfirst.Enabled = True
   cmdPrev.Enabled = True
   cmdNext.Enabled = True
   cmdLast.Enabled = True
  Else
   cmdfirst.Enabled = False
   cmdPrev.Enabled = False
   cmdNext.Enabled = False
   cmdLast.Enabled = False

 End If
End Sub
Sub grdFind()
  adoFind.RecordSource = " SELECT " & strTableH & ".*, City.Name AS City, Country.Name AS Country, CorCity.Name AS CorCity, CorCountry.Name AS CorCountry " & _
  " FROM ((" & strTableH & " LEFT OUTER JOIN City ON " & strTableH & ".CityID=City.CityID) LEFT OUTER JOIN Country ON City.countryID=Country.CountryID) LEFT OUTER JOIN (City AS CorCity LEFT OUTER JOIN Country AS CorCountry ON CorCity.countryID=CorCountry.CountryID) ON " & strTableH & ".CorCityID=CorCity.CityID " & _
   " where partnerid <>'' and  right(left(partnerid," & gLenOffCode + Len(mainID) & ")," & gLenOffCode & ")='" & gOffCode & "'  "

 If txtPartnerName.Text <> "" Then
  VarSelection = Replace(Trim(txtPartnerName.Text), "'", "''") & "%"
  varlong = Len(Trim(VarSelection))
   adoFind.RecordSource = adoFind.RecordSource & " and left(partnername,'" & varlong & "') like '" & VarSelection & "'"
 End If
 adoFind.Refresh
 Set grdListFind.DataSource = adoFind
 ' grdListNo = 11
GrdListFindShow Me, txtPartnerName.Left, txtPartnerName.Top, 7000, 4000
 End Sub


Private Sub txtCity_DblClick()
grdcity
End Sub

Private Sub txtCity_KeyPress(KeyAscii As Integer)
KeyAscii = Asc(UCase(Chr(KeyAscii)))
    If KeyAscii = 13 Then grdcity

End Sub


Private Sub txtCorCity_dblclick()
grdCorcity
End Sub

Private Sub txtCorCity_KeyPress(KeyAscii As Integer)
KeyAscii = Asc(UCase(Chr(KeyAscii)))
    If KeyAscii = 13 Then grdCorcity
End Sub

Private Sub txtCorCountry_dblclick()
grdCorCountry
End Sub

Private Sub txtCorCountry_KeyPress(KeyAscii As Integer)
KeyAscii = Asc(UCase(Chr(KeyAscii)))
    If KeyAscii = 13 Then grdCorCountry
End Sub

Private Sub txtCountry_DblClick()
grdCountry
End Sub

Private Sub txtCountry_KeyPress(KeyAscii As Integer)
KeyAscii = Asc(UCase(Chr(KeyAscii)))
    If KeyAscii = 13 Then grdCountry

End Sub
Sub City_dblclick()
 If IsNull(adoList.Recordset!cityID) Then lblCityID.Caption = "" Else lblCityID.Caption = adoList.Recordset!cityID
 If IsNull(adoList.Recordset!Name) Then txtCity.Text = "" Else txtCity.Text = adoList.Recordset!Name
End Sub
Sub CorCity_dblclick()
 If IsNull(adoList.Recordset!cityID) Then lblCorCity.Caption = "" Else lblCorCity.Caption = adoList.Recordset!cityID
 If IsNull(adoList.Recordset!Name) Then txtCorCity.Text = "" Else txtCorCity.Text = adoList.Recordset!Name
End Sub

Sub country_dblclick()
 If IsNull(adoList.Recordset!countryID) Then lblCountryID.Caption = "" Else lblCountryID.Caption = adoList.Recordset!countryID
 If IsNull(adoList.Recordset!Name) Then txtCountry.Text = "" Else txtCountry.Text = adoList.Recordset!Name
End Sub
Sub Corcountry_dblclick()
 If IsNull(adoList.Recordset!countryID) Then lblCorCountry.Caption = "" Else lblCorCountry.Caption = adoList.Recordset!countryID
 If IsNull(adoList.Recordset!Name) Then txtCorCountry.Text = "" Else txtCorCountry.Text = adoList.Recordset!Name
End Sub


Private Sub txtIdent_KeyPress(KeyAscii As Integer)
KeyAscii = Asc(UCase(Chr(KeyAscii)))
'    If KeyAscii = 13 Then grdCountry
End Sub


Private Sub txtPartnerID_KeyPress(KeyAscii As Integer)
If KeyAscii = Asc(".") Then
 KeyAscii = 0
 Else
 KeyAscii = keyNumber(KeyAscii)
End If
End Sub
