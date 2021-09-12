# coding: utf-8
from sqlalchemy import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Boolean
from app.database import Base

metadata = MetaData()


class T_APPO_D(Base):
    __tablename__ = 'APPO_D'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType = Column(String)
    Account = Column(String)
    DivID = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    RefVou = Column(String)
    RefNO = Column(Integer)
    RefMainDoc = Column(String)
    RefPreDoc = Column(String)
    RefDetailDoc = Column(String)
    RefOthDoc = Column(String)
    TranDocD = Column(String)
    RefD1 = Column(String)
    RefD2 = Column(String)
    MerkID = Column(String)
    ThingType = Column(String)
    ThingID = Column(String)
    SerialID = Column(String)
    Descript = Column(String)
    Qty = Column(Integer)
    UnitID = Column(String)
    UnitPrice = Column(Integer)
    DiscAmount = Column(Integer)
    RefCur = Column(String)
    RefAmount = Column(Integer)
    Rate = Column(Integer)
    AmountD = Column(Integer)
    BalanceD = Column(Integer)
    TaxAmount = Column(Integer)
    TaxAmount1 = Column(Integer)
    OthCost = Column(Integer)


class T_APPO_H(Base):
    __tablename__ = 'APPO_H'
    VoucherID = Column(String, primary_key=True)
    Account = Column(String)
    Cur = Column(String)
    DateDay = Column(DateTime)
    DateDue = Column(DateTime)
    TType = Column(String)
    PartnerName = Column(String)
    PartnerID = Column(String)
    Receiver = Column(String)
    MainDoc = Column(String)
    PreDoc = Column(String)
    DetailDoc = Column(String)
    OthDoc = Column(String)
    TranDoc = Column(String)
    Ref1 = Column(String)
    Ref2 = Column(String)
    TotalDiscount = Column(Integer)
    TotalTax = Column(Integer)
    TotalTax1 = Column(Integer)
    SubTotal = Column(Integer)
    GrandTotal = Column(Integer)
    BalanceH = Column(Integer)
    TotalAdj = Column(Integer)
    TotalCost = Column(Integer)
    Journal = Column(String)
    RateJou = Column(Integer)
    Paid = Column(String)
    HeadJou = Column(String)
    UserID = Column(String)
    DateEntry = Column(DateTime)
    DateUpdate = Column(DateTime)
    UserLock = Column(String)
    AddDesc = Column(String)


class T_APProduct(Base):
    __tablename__ = 'APProduct'
    Item_ID_NV = Column(String, primary_key=True)
    Item_Desc_NV = Column(String)
    Item_Acc_NV = Column(String)


class T_APVou_D(Base):
    __tablename__ = 'APVou_D'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType = Column(String)
    Account = Column(String)
    DivID = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    RefVou = Column(String)
    RefNO = Column(Integer)
    RefMainDoc = Column(String)
    RefPreDoc = Column(String)
    RefDetailDoc = Column(String)
    RefOthDoc = Column(String)
    TranDocD = Column(String)
    RefD1 = Column(String)
    RefD2 = Column(String)
    MerkID = Column(String)
    ThingType = Column(String)
    ThingID = Column(String)
    SerialID = Column(String)
    Descript = Column(String)
    Qty = Column(Integer)
    UnitID = Column(String)
    UnitPrice = Column(Integer)
    DiscAmount = Column(Integer)
    RefCur = Column(String)
    RefAmount = Column(Integer)
    Rate = Column(Integer)
    AmountD = Column(Integer)
    BalanceD = Column(Integer)
    TaxAmount = Column(Integer)
    TaxAmount1 = Column(Integer)
    OthCost = Column(Integer)


class T_APVou_D1(Base):
    __tablename__ = 'APVou_D1'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType1 = Column(String)
    Account1 = Column(String)
    RefVou1 = Column(String)
    RefNO1 = Column(Integer)
    RefMainDoc1 = Column(String)
    RefPreDoc1 = Column(String)
    RefDetailDoc1 = Column(String)
    RefOthDoc1 = Column(String)
    TranDocD1 = Column(String)
    RefD11 = Column(String)
    RefD21 = Column(String)
    MerkID1 = Column(String)
    ThingType1 = Column(String)
    ThingID1 = Column(String)
    SerialID1 = Column(String)
    Descript1 = Column(String)
    Qty1 = Column(Integer)
    UnitID1 = Column(String)
    UnitPrice1 = Column(Integer)
    DiscAmount1 = Column(Integer)
    RefCur1 = Column(String)
    RefAmount1 = Column(Integer)
    Rate1 = Column(Integer)
    AmountD1 = Column(Integer)
    BalanceD1 = Column(Integer)
    TaxAmount1 = Column(Integer)
    TaxAmount11 = Column(Integer)
    OthCost1 = Column(Integer)


class T_APVou_H(Base):
    __tablename__ = 'APVou_H'
    VoucherID = Column(String, primary_key=True)
    Account = Column(String)
    Cur = Column(String)
    DateDay = Column(DateTime)
    DateDue = Column(DateTime)
    TType = Column(String)
    PartnerName = Column(String)
    PartnerID = Column(String)
    Receiver = Column(String)
    MainDoc = Column(String)
    PreDoc = Column(String)
    DetailDoc = Column(String)
    OthDoc = Column(String)
    TranDoc = Column(String)
    Ref1 = Column(String)
    Ref2 = Column(String)
    TotalDiscount = Column(Integer)
    TotalTax = Column(Integer)
    TotalTax1 = Column(Integer)
    SubTotal = Column(Integer)
    GrandTotal = Column(Integer)
    BalanceH = Column(Integer)
    TotalAdj = Column(Integer)
    TotalCost = Column(Integer)
    Journal = Column(String)
    RateJou = Column(Integer)
    Paid = Column(String)
    HeadJou = Column(String)
    UserID = Column(String)
    DateEntry = Column(DateTime)
    DateUpdate = Column(DateTime)
    UserLock = Column(String)
    AddDesc = Column(String)


class T_APVou_H1(Base):
    __tablename__ = 'APVou_H1'
    VoucherID = Column(String, primary_key=True)
    POno = Column(String)
    PODate = Column(String)
    MainDoc1 = Column(String)
    PreDoc1 = Column(String)
    DetailDoc1 = Column(String)
    OthDoc1 = Column(String)
    Ref11 = Column(String)
    Ref21 = Column(String)
    TotalTax1 = Column(Integer)
    TotalTax11 = Column(Integer)
    GrandTotal1 = Column(Integer)
    BalanceH1 = Column(Integer)
    Paid1 = Column(String)


class T_ARVou_D(Base):
    __tablename__ = 'ARVou_D'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType = Column(String)
    Account = Column(String)
    DivID = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    RefVou = Column(String)
    RefNO = Column(Integer)
    RefMainDoc = Column(String)
    RefPreDoc = Column(String)
    RefDetailDoc = Column(String)
    RefOthDoc = Column(String)
    TranDocD = Column(String)
    RefD1 = Column(String)
    RefD2 = Column(String)
    MerkID = Column(String)
    ThingType = Column(String)
    ThingID = Column(String)
    SerialID = Column(String)
    Descript = Column(String)
    Qty = Column(Integer)
    UnitID = Column(String)
    UnitPrice = Column(Integer)
    DiscAmount = Column(Integer)
    RefCur = Column(String)
    RefAmount = Column(Integer)
    Rate = Column(Integer)
    AmountD = Column(Integer)
    BalanceD = Column(Integer)
    TaxAmount = Column(Integer)
    TaxAmount1 = Column(Integer)
    OthCost = Column(Integer)


class T_ARVou_D1(Base):
    __tablename__ = 'ARVou_D1'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType1 = Column(String)
    Account1 = Column(String)
    RefVou1 = Column(String)
    RefNO1 = Column(Integer)
    RefMainDoc1 = Column(String)
    RefPreDoc1 = Column(String)
    RefDetailDoc1 = Column(String)
    RefOthDoc1 = Column(String)
    TranDocD1 = Column(String)
    RefD11 = Column(String)
    RefD21 = Column(String)
    MerkID1 = Column(String)
    ThingType1 = Column(String)
    ThingID1 = Column(String)
    SerialID1 = Column(String)
    Descript1 = Column(String)
    Qty1 = Column(Integer)
    UnitID1 = Column(String)
    UnitPrice1 = Column(Integer)
    DiscAmount1 = Column(Integer)
    RefCur1 = Column(String)
    RefAmount1 = Column(Integer)
    Rate1 = Column(Integer)
    AmountD1 = Column(Integer)
    BalanceD1 = Column(Integer)
    TaxAmount1 = Column(Integer)
    TaxAmount11 = Column(Integer)
    OthCost1 = Column(Integer)


class T_ARVou_H(Base):
    __tablename__ = 'ARVou_H'
    VoucherID = Column(String, primary_key=True)
    Account = Column(String)
    Cur = Column(String)
    DateDay = Column(DateTime)
    DateDue = Column(DateTime)
    TType = Column(String)
    PartnerName = Column(String)
    PartnerID = Column(String)
    Receiver = Column(String)
    MainDoc = Column(String)
    PreDoc = Column(String)
    DetailDoc = Column(String)
    OthDoc = Column(String)
    TranDoc = Column(String)
    Ref1 = Column(String)
    Ref2 = Column(String)
    TotalDiscount = Column(Integer)
    TotalTax = Column(Integer)
    TotalTax1 = Column(Integer)
    SubTotal = Column(Integer)
    GrandTotal = Column(Integer)
    BalanceH = Column(Integer)
    TotalAdj = Column(Integer)
    TotalCost = Column(Integer)
    Journal = Column(String)
    RateJou = Column(Integer)
    Paid = Column(String)
    HeadJou = Column(String)
    UserID = Column(String)
    DateEntry = Column(DateTime)
    DateUpdate = Column(DateTime)
    UserLock = Column(String)
    AddDesc = Column(String)


class T_ARVou_H1(Base):
    __tablename__ = 'ARVou_H1'
    VoucherID = Column(String, primary_key=True)
    POno = Column(String)
    PODate = Column(String)
    MainDoc1 = Column(String)
    PreDoc1 = Column(String)
    DetailDoc1 = Column(String)
    OthDoc1 = Column(String)
    Ref11 = Column(String)
    Ref21 = Column(String)
    TotalTax1 = Column(Integer)
    TotalTax11 = Column(Integer)
    GrandTotal1 = Column(Integer)
    BalanceH1 = Column(Integer)
    Paid1 = Column(String)


class T_Asset(Base):
    __tablename__ = 'Asset'
    OffCode = Column(String, primary_key=True)
    AssetID = Column(String)
    Name = Column(String)
    AssetKindID = Column(String)


class T_AssetKind(Base):
    __tablename__ = 'AssetKind'
    AssetKindID = Column(String, primary_key=True)
    Name = Column(String)


class T_Bhs(Base):
    __tablename__ = 'Bhs'
    captText = Column(String, primary_key=True)
    bhsID = Column(String)
    ShowText = Column(String)


class T_BranchOffice(Base):
    __tablename__ = 'BranchOffice'
    OffCode = Column(String, primary_key=True)
    CompanyID = Column(String)
    CityID = Column(String)
    name = Column(String)


class T_CBAdv_D(Base):
    __tablename__ = 'CBAdv_D'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType = Column(String)
    Account = Column(String)
    DivID = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    RefVou = Column(String)
    RefNO = Column(Integer)
    RefMainDoc = Column(String)
    RefPreDoc = Column(String)
    RefDetailDoc = Column(String)
    RefOthDoc = Column(String)
    TranDocD = Column(String)
    RefD1 = Column(String)
    RefD2 = Column(String)
    MerkID = Column(String)
    ThingType = Column(String)
    ThingID = Column(String)
    SerialID = Column(String)
    Descript = Column(String)
    Qty = Column(Integer)
    UnitID = Column(String)
    UnitPrice = Column(Integer)
    DiscAmount = Column(Integer)
    RefCur = Column(String)
    RefAmount = Column(Integer)
    Rate = Column(Integer)
    AmountD = Column(Integer)
    BalanceD = Column(Integer)
    TaxAmount = Column(Integer)
    TaxAmount1 = Column(Integer)
    OthCost = Column(Integer)


class T_CBAdv_D1(Base):
    __tablename__ = 'CBAdv_D1'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType1 = Column(String)
    Account1 = Column(String)
    RefVou1 = Column(String)
    RefNO1 = Column(Integer)
    RefMainDoc1 = Column(String)
    RefPreDoc1 = Column(String)
    RefDetailDoc1 = Column(String)
    RefOthDoc1 = Column(String)
    TranDocD1 = Column(String)
    RefD11 = Column(String)
    RefD21 = Column(String)
    MerkID1 = Column(String)
    ThingType1 = Column(String)
    ThingID1 = Column(String)
    SerialID1 = Column(String)
    Descript1 = Column(String)
    Qty1 = Column(Integer)
    UnitID1 = Column(String)
    UnitPrice1 = Column(Integer)
    DiscAmount1 = Column(Integer)
    RefCur1 = Column(String)
    RefAmount1 = Column(Integer)
    Rate1 = Column(Integer)
    AmountD1 = Column(Integer)
    BalanceD1 = Column(Integer)
    TaxAmount1 = Column(Integer)
    TaxAmount11 = Column(Integer)
    OthCost1 = Column(Integer)


class T_CBAdv_H(Base):
    __tablename__ = 'CBAdv_H'
    VoucherID = Column(String, primary_key=True)
    Account = Column(String)
    Cur = Column(String)
    DateDay = Column(DateTime)
    DateDue = Column(DateTime)
    TType = Column(String)
    PartnerName = Column(String)
    PartnerID = Column(String)
    Receiver = Column(String)
    MainDoc = Column(String)
    PreDoc = Column(String)
    DetailDoc = Column(String)
    OthDoc = Column(String)
    TranDoc = Column(String)
    Ref1 = Column(String)
    Ref2 = Column(String)
    TotalDiscount = Column(Integer)
    TotalTax = Column(Integer)
    TotalTax1 = Column(Integer)
    SubTotal = Column(Integer)
    GrandTotal = Column(Integer)
    BalanceH = Column(Integer)
    TotalAdj = Column(Integer)
    TotalCost = Column(Integer)
    Journal = Column(String)
    RateJou = Column(Integer)
    Paid = Column(String)
    HeadJou = Column(String)
    UserID = Column(String)
    DateEntry = Column(DateTime)
    DateUpdate = Column(DateTime)
    UserLock = Column(String)
    AddDesc = Column(String)


class T_CBBalance(Base):
    __tablename__ = 'CBBalance'
    ThingId = Column(String, primary_key=True)
    PeriodID = Column(String)
    Out = Column(Integer)
    In = Column(Integer)
    BegBalance = Column(Integer)
    EndBalance = Column(Integer)


class T_CBVou_D(Base):
    __tablename__ = 'CBVou_D'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType = Column(String)
    Account = Column(String)
    DivID = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    RefVou = Column(String)
    RefNO = Column(Integer)
    RefMainDoc = Column(String)
    RefPreDoc = Column(String)
    RefDetailDoc = Column(String)
    RefOthDoc = Column(String)
    TranDocD = Column(String)
    RefD1 = Column(String)
    RefD2 = Column(String)
    MerkID = Column(String)
    ThingType = Column(String)
    ThingID = Column(String)
    SerialID = Column(String)
    Descript = Column(String)
    Qty = Column(Integer)
    UnitID = Column(String)
    UnitPrice = Column(Integer)
    DiscAmount = Column(Integer)
    RefCur = Column(String)
    RefAmount = Column(Integer)
    Rate = Column(Integer)
    AmountD = Column(Integer)
    BalanceD = Column(Integer)
    TaxAmount = Column(Integer)
    TaxAmount1 = Column(Integer)
    OthCost = Column(Integer)


class T_CBVou_D1(Base):
    __tablename__ = 'CBVou_D1'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType1 = Column(String)
    Account1 = Column(String)
    RefVou1 = Column(String)
    RefNO1 = Column(Integer)
    RefMainDoc1 = Column(String)
    RefPreDoc1 = Column(String)
    RefDetailDoc1 = Column(String)
    RefOthDoc1 = Column(String)
    TranDocD1 = Column(String)
    RefD11 = Column(String)
    RefD21 = Column(String)
    MerkID1 = Column(String)
    ThingType1 = Column(String)
    ThingID1 = Column(String)
    SerialID1 = Column(String)
    Descript1 = Column(String)
    Qty1 = Column(Integer)
    UnitID1 = Column(String)
    UnitPrice1 = Column(Integer)
    DiscAmount1 = Column(Integer)
    RefCur1 = Column(String)
    RefAmount1 = Column(Integer)
    Rate1 = Column(Integer)
    AmountD1 = Column(Integer)
    BalanceD1 = Column(Integer)
    TaxAmount1 = Column(Integer)
    TaxAmount11 = Column(Integer)
    OthCost1 = Column(Integer)


class T_CBVou_H(Base):
    __tablename__ = 'CBVou_H'
    VoucherID = Column(String, primary_key=True)
    Account = Column(String)
    Cur = Column(String)
    DateDay = Column(DateTime)
    DateDue = Column(DateTime)
    TType = Column(String)
    PartnerName = Column(String)
    PartnerID = Column(String)
    Receiver = Column(String)
    MainDoc = Column(String)
    PreDoc = Column(String)
    DetailDoc = Column(String)
    OthDoc = Column(String)
    TranDoc = Column(String)
    Ref1 = Column(String)
    Ref2 = Column(String)
    TotalDiscount = Column(Integer)
    TotalTax = Column(Integer)
    TotalTax1 = Column(Integer)
    SubTotal = Column(Integer)
    GrandTotal = Column(Integer)
    BalanceH = Column(Integer)
    TotalAdj = Column(Integer)
    TotalCost = Column(Integer)
    Journal = Column(String)
    RateJou = Column(Integer)
    Paid = Column(String)
    HeadJou = Column(String)
    UserID = Column(String)
    DateEntry = Column(DateTime)
    DateUpdate = Column(DateTime)
    UserLock = Column(String)
    AddDesc = Column(String)


class T_Category(Base):
    __tablename__ = 'Category'
    CategoryID = Column(String, primary_key=True)
    CategoryDesc = Column(String)


class T_City(Base):
    __tablename__ = 'City'
    CityID = Column(String, primary_key=True)
    Name = Column(String)
    countryID = Column(String)
    locKind = Column(String)


class T_Company(Base):
    __tablename__ = 'Company'
    CompanyID = Column(String, primary_key=True)
    CompanyName = Column(String)
    CompanyName1 = Column(String)
    CompanyHead = Column(String)
    CompanyAddress = Column(String)
    CompanyPhone = Column(String)


class T_Country(Base):
    __tablename__ = 'Country'
    CountryID = Column(String, primary_key=True)
    Name = Column(String)


# ! di rename cari Curency ke Currency agar sesuai bahasa inggris
class T_Currency(Base):
    __tablename__ = 'Currency'
    Cur = Column(String, primary_key=True)
    Name = Column(String)
    CountryID = Column(String)
    Rate = Column(Integer)
    Mark = Column(String)


class T_Customer(Base):
    __tablename__ = 'Customer'
    PartnerID = Column(String, primary_key=True)
    PartnerName = Column(String)
    Ident = Column(String)
    OrgType = Column(String)
    Address1 = Column(String)
    Address2 = Column(String)
    Address3 = Column(String)
    Address4 = Column(String)
    CityID = Column(String)
    CountryID = Column(String)
    ZipCode = Column(String)
    Phone1 = Column(String)
    Phone2 = Column(String)
    Fax1 = Column(String)
    Fax2 = Column(String)
    Email = Column(String)
    Contact1 = Column(String)
    Contact2 = Column(String)
    NPWP = Column(String)
    NPWPdate = Column(DateTime)
    NPWPKukuh = Column(String)
    NPWPdateKukuh = Column(DateTime)
    NPWP1 = Column(String)
    NPWPdate1 = Column(DateTime)
    NPWPKukuh1 = Column(String)
    NPWPdateKukuh1 = Column(DateTime)
    APITU = Column(String)
    SPR = Column(String)
    SIUP = Column(String)
    Note1 = Column(String)
    Note2 = Column(String)
    CorAdd1 = Column(String)
    CorAdd2 = Column(String)
    CorAdd3 = Column(String)
    CorAdd4 = Column(String)
    CorCityID = Column(String)
    CorCountryID = Column(String)
    CorZipCode = Column(String)
    CorPhone1 = Column(String)
    CorPhone2 = Column(String)
    CorFax1 = Column(String)
    CorFax2 = Column(String)
    CorEmail = Column(String)
    CorContact1 = Column(String)
    CorContact2 = Column(String)
    Active = Column(String)
    UserID = Column(String)

# TODO: cari, ngga ada di db access


class T_DType(Base):
    __tablename__ = 'DType'
    DType = Column(String, primary_key=True)
    Name = Column(String)
    CorVoucherType = Column(String)
    Modul = Column(String)
    HeadDC = Column(String)
    FoGroup = Column(String)


class T_DailyTranJob(Base):
    __tablename__ = 'DailyTranJob'
    ProductID = Column(String, primary_key=True)
    name = Column(String)
    account = Column(String)
    GroupProdID = Column(String)
    AssetKind = Column(String)
    inv = Column(Boolean)
    Emod = Column(Boolean)
    Mmod = Column(Boolean)
    Amod = Column(Boolean)


class T_Department(Base):
    __tablename__ = 'Department'
    DepartmentID = Column(String, primary_key=True)
    DepartmentName = Column(String)
    DepartmentHead = Column(String)
    OffCode = Column(String)


class T_DetDemPeriod(Base):
    __tablename__ = 'DetDemPeriod'
    DD_Period_ID_VC = Column(String, primary_key=True)
    DD_Start_Day_SI = Column(Integer)
    DD_End_Day_SI = Column(Integer)
    DD_Desc_VC = Column(String)


class T_Division(Base):
    __tablename__ = 'Division'
    OffCode = Column(String, primary_key=True)
    DivID = Column(String)
    DivName = Column(String)


class T_Forex(Base):
    __tablename__ = 'Forex'
    ForexID = Column(String, primary_key=True)
    ForexCode = Column(String)
    ForexDesc = Column(String)
    ForexCountryID = Column(String)


class T_GetDatetime(Base):
    __tablename__ = 'GetDatetime'
    OffCode = Column(String, primary_key=True)
    UserID = Column(String)
    datedaytime = Column(DateTime)


class T_gLen(Base):
    __tablename__ = 'gLen'
    gNumber = Column(String, primary_key=True)
    gLenThing = Column(Integer)
    gLenVoucher = Column(Integer)
    gLenOffCode = Column(Integer)
    gLenCounter = Column(Integer)
    gLenTranID = Column(Integer)
    gMCounter = Column(Integer)
    gLenAccount = Column(Integer)


class T_InvDesc(Base):
    __tablename__ = 'InvDesc'
    OffCode = Column(String, primary_key=True)
    InvID = Column(String)
    JobKind = Column(String)
    InvType = Column(String)
    Account = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    InvDesc = Column(String)


class T_Item(Base):
    __tablename__ = 'Item'
    OffCode = Column(String, primary_key=True)
    itemID = Column(String)
    InvID = Column(String)
    ItemDesc = Column(String)
    GroupItem = Column(String)
    Account = Column(String)
    Cur = Column(String)
    HrgStd = Column(Integer)


class T_JobKind(Base):
    __tablename__ = 'JobKind'
    OffCode = Column(String, primary_key=True)
    JobKind = Column(String)
    JobName = Column(String)
    DivID = Column(String)


class T_JobOrder(Base):
    __tablename__ = 'JobOrder'
    OffCode = Column(String, primary_key=True)
    JobID = Column(String)
    JobKind = Column(String)
    DateDay = Column(DateTime)
    Ident = Column(String)
    PartnerID = Column(String)
    PartnerName = Column(String)
    Descript = Column(String)
    CustomerName = Column(String)
    Weight = Column(String)
    Measurement = Column(String)
    Utility = Column(String)
    Dishpack = Column(String)
    Clothing = Column(String)
    Glass = Column(String)
    Furniture = Column(String)
    Comment = Column(String)
    AllPacker = Column(String)
    Packer = Column(String)
    Freelance = Column(String)
    ElfBox = Column(String)
    ElfBak = Column(String)
    LooseBak = Column(String)
    L300Box = Column(String)
    PickUp = Column(String)
    Panther = Column(String)
    LCLshipment = Column(String)
    WoodenLiftvan = Column(String)
    CartonLiftvan = Column(String)
    FCLshipment = Column(String)
    FCL20 = Column(String)
    FCL40 = Column(String)
    LoosePack = Column(String)
    Liftvan = Column(String)
    Departure = Column(String)
    PaymentType = Column(String)
    AddPay = Column(String)
    OrderByName = Column(String)
    OrderByDate = Column(String)
    CargoDivName = Column(String)
    CargoDivDate = Column(String)
    MPdivName = Column(String)
    MPdivDate = Column(String)
    Remark = Column(String)
    DateUpdate = Column(DateTime)
    active = Column(String)


class T_JobOrderX(Base):
    __tablename__ = 'JobOrderX'
    OffCode = Column(String, primary_key=True)
    JobID = Column(String)
    JobKind = Column(String)
    DateDay = Column(DateTime)
    Ident = Column(String)
    PartnerID = Column(String)
    PartnerName = Column(String)
    KindOfWork = Column(String)
    ShipConsignee = Column(String)
    NameOfGood = Column(String)
    CustomerRef = Column(String)
    LoadPort = Column(String)
    DischargePort = Column(String)
    VesselFlight = Column(String)
    ETA = Column(DateTime)
    ETD = Column(DateTime)
    ClearanceDate = Column(DateTime)
    DeliveryDate = Column(DateTime)
    BlAwbM = Column(String)
    BlAwbH = Column(String)
    Service = Column(String)
    ContSize = Column(String)
    ContainerNo = Column(String)
    QofGood = Column(Integer)
    Weight = Column(Integer)
    Measurement = Column(String)
    ShippingName = Column(String)
    WarehouseName = Column(String)
    TypeOfService = Column(String)
    EPTEBc23Peb30Date = Column(DateTime)
    PTBc23Peb30 = Column(String)
    PTPE = Column(String)
    PTInvoice = Column(String)
    PTPacking = Column(String)
    PTBlAwbAsli = Column(String)
    PTAsuransi = Column(String)
    PTSK = Column(String)
    PTKonlak = Column(String)
    PTSSBP = Column(String)
    GCPib20Peb30 = Column(String)
    GCPE = Column(String)
    GCInvoice = Column(String)
    GCPacking = Column(String)
    GCBlAwbAsli = Column(String)
    GCSK = Column(String)
    GCSTTJ = Column(String)
    GCIzinDep = Column(String)
    GCCIS = Column(String)
    GCIP = Column(String)
    GCMaster = Column(String)
    GCNPIK = Column(String)
    GCSKBPPN = Column(String)
    GCAsuransi = Column(String)
    GCSSPCP = Column(String)
    Driver = Column(String)
    Truck = Column(String)
    Condition = Column(String)
    Remark = Column(String)
    active = Column(String)


class T_MaterialType(Base):
    __tablename__ = 'MaterialType'
    MateID = Column(String, primary_key=True)
    MateDesc = Column(String)


class T_Menu(Base):
    __tablename__ = 'Menu'
    OffCode = Column(String, primary_key=True)
    MenuId = Column(String)
    Name = Column(String)
    FrmName = Column(String)
    Remark = Column(String)
    UserUse = Column(Boolean)


class T_Merk(Base):
    __tablename__ = 'Merk'
    MerkID = Column(String, primary_key=True)
    Name = Column(String)
    Descript = Column(String)
    GroupMerk = Column(String)


class T_Paste_Errors(Base):
    __tablename__ = 'Paste Errors'
    # TODO: DI DB TIPENYA LONG TEX, primary_key=TrueT
    Field0 = Column(String, primary_key=True)


class T_PaySalesTran(Base):
    __tablename__ = 'PaySalesTran'
    PayID = Column(String, primary_key=True)
    PayKindID = Column(String)
    PayDesc = Column(String)
    Account = Column(String)
    CostType = Column(String)
    Cost = Column(Integer)
    CostAccount = Column(String)
    Mark = Column(String)
    Active = Column(String)


class T_PaymentVoucher(Base):
    __tablename__ = 'PaymentVoucher'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    PayID = Column(String)
    IdentityNo = Column(String)
    IdentityName = Column(String)
    Amount = Column(Integer)
    OtherAmount = Column(Integer)
    Cost = Column(Integer)
    TotalPay = Column(Integer)
    BalanceD = Column(Integer)


class T_PeriodACC(Base):
    __tablename__ = 'PeriodACC'
    PeriodID = Column(String, primary_key=True)
    PeriodName = Column(String)
    StartDate = Column(DateTime)
    EndDate = Column(DateTime)
    YearPeriod = Column(String)
    CloseStat = Column(String)
    CloseDate = Column(DateTime)
    UserID = Column(String)
    UserIDClose = Column(String)


class T_PeriodFO(Base):
    __tablename__ = 'PeriodFO'
    OffCode = Column(String, primary_key=True)
    PeriodID = Column(String)
    PeriodDate = Column(DateTime)


class T_Port(Base):
    __tablename__ = 'Port'
    PortCode_CH = Column(String, primary_key=True)
    PortName_CH = Column(String)
    PortType_CH = Column(String)
    PortTrade_CH = Column(String)
    PortRate_NU = Column(Integer)
    PortCountry_CH = Column(String)
    CityID_CH = Column(String)
    LocKind = Column(String)


class T_PrincipalMain(Base):
    __tablename__ = 'PrincipalMain'
    Prin_Code_CH = Column(String, primary_key=True)
    Prin_Name_CH = Column(String)
    Prin_Name1_CH = Column(String)
    Prin_Address1_CH = Column(String)
    Prin_Address2_CH = Column(String)
    Prin_Address3_CH = Column(String)
    Prin_Address4_CH = Column(String)
    Prin_Address5_CH = Column(String)
    Prin_City_CH = Column(String)
    Prin_Country_CH = Column(String)
    Prin_Zip_CH = Column(String)
    Prin_Phone_CH = Column(String)
    Prin_Fax_CH = Column(String)
    Prin_Email_CH = Column(String)
    Prin_Type_CH = Column(String)
    Prin_Inactive_BT = Column(Boolean)
    Prin_UserID_CH = Column(String)
    Prin_BL_Code_CH = Column(String)
    Prin_KtrAs_CH = Column(String)


class T_ProductBuy(Base):
    __tablename__ = 'ProductBuy'
    ProductID = Column(String, primary_key=True)
    name = Column(String)
    account = Column(String)
    UnitPrice = Column(Integer)
    GroupProdID = Column(String)
    AssetKind = Column(String)
    inv = Column(String)
    Emod = Column(String)
    Mmod = Column(String)
    Amod = Column(String)


class T_ProductSale(Base):
    __tablename__ = 'ProductSale'
    ProductID = Column(String, primary_key=True)
    name = Column(String)
    account = Column(String)
    Cur = Column(String)
    UnitPrice = Column(Integer)
    GroupProdID = Column(String)
    AssetKind = Column(String)
    inv = Column(String)
    Emod = Column(String)
    Mmod = Column(String)
    Amod = Column(String)


class T_Rate(Base):
    __tablename__ = 'Rate'
    Cur1 = Column(String, primary_key=True)
    Cur2 = Column(String)
    RateAmount = Column(Integer)


class T_SaleVou_D(Base):
    __tablename__ = 'SaleVou_D'
    VoucherID = Column(String, primary_key=True)
    NoDet = Column(Integer)
    DType = Column(String)
    Account = Column(String)
    DivID = Column(String)
    Tax = Column(String)
    Tax1 = Column(String)
    RefVou = Column(String)
    RefNO = Column(Integer)
    RefMainDoc = Column(String)
    RefPreDoc = Column(String)
    RefDetailDoc = Column(String)
    RefOthDoc = Column(String)
    TranDocD = Column(String)
    RefD1 = Column(String)
    RefD2 = Column(String)
    ThingType = Column(String)
    ThingID = Column(String)
    SerialID = Column(String)
    Descript = Column(String)
    Qty = Column(Integer)
    UnitID = Column(String)
    UnitPrice = Column(Integer)
    DiscAmount = Column(Integer)
    RefCur = Column(String)
    RefAmount = Column(Integer)
    Rate = Column(Integer)
    AmountD = Column(Integer)
    BalanceD = Column(Integer)
    TaxAmount = Column(Integer)
    TaxAmount1 = Column(Integer)
    OthCost = Column(Integer)


class T_SaleVou_H(Base):
    __tablename__ = 'SaleVou_H'
    VoucherID = Column(String, primary_key=True)
    Account = Column(String)
    Cur = Column(String)
    DateDay = Column(DateTime)
    DateDue = Column(DateTime)
    TType = Column(String)
    PartnerName = Column(String)
    PartnerID = Column(String)
    Receiver = Column(String)
    MainDoc = Column(String)
    PreDoc = Column(String)
    DetailDoc = Column(String)
    OthDoc = Column(String)
    TranDoc = Column(String)
    Ref1 = Column(String)
    Ref2 = Column(String)
    TotalDiscount = Column(Integer)
    TotalTax = Column(Integer)
    TotalTax1 = Column(Integer)
    SubTotal = Column(Integer)
    GrandTotal = Column(Integer)
    BalanceH = Column(Integer)
    TotalAdj = Column(Integer)
    TotalCost = Column(Integer)
    Journal = Column(String)
    RateJou = Column(Integer)
    Paid = Column(String)
    HeadJou = Column(String)
    UserID = Column(String)
    DateEntry = Column(DateTime)
    DateUpdate = Column(DateTime)
    UserLock = Column(String)
    AddDesc = Column(String)


class T_Sales(Base):
    __tablename__ = 'Sales'
    OffCode = Column(String, primary_key=True)
    SalesId = Column(String)
    Name = Column(String)
    Comm = Column(Integer)
    Active = Column(String)


class T_SetupSystem(Base):
    __tablename__ = 'SetupSystem'
    OffCode = Column(String, primary_key=True)
    Address1 = Column(String)
    Address2 = Column(String)
    Address3 = Column(String)
    NPWP = Column(String)
    NPWPDate = Column(String)
    NPWPKukuh = Column(String)
    NPWPDateKukuh = Column(String)
    AccSubgroupPL = Column(String)
    AccountPLDitahan = Column(String)
    AccountPLBerJalan = Column(String)
    InvoiceName = Column(String)
    Tax1Name = Column(String)
    Tax1Title = Column(String)
    Name1 = Column(String)
    Name2 = Column(String)
    Name3 = Column(String)
    TaxStd = Column(String)
    TaxSdn = Column(String)
    ARTaxAccount = Column(String)
    ARTax1Account = Column(String)
    SelisihAcckurs = Column(String)
    DiscountAcc = Column(String)
    userlock = Column(String)


class T_Supplier(Base):
    __tablename__ = 'Supplier'
    PartnerID = Column(String, primary_key=True)
    PartnerName = Column(String)
    Address1 = Column(String)
    Address2 = Column(String)
    Address3 = Column(String)
    Address4 = Column(String)
    CityID = Column(String)
    CountryID = Column(String)
    ZipCode = Column(String)
    Phone1 = Column(String)
    Phone2 = Column(String)
    Fax1 = Column(String)
    Fax2 = Column(String)
    Email = Column(String)
    Contact1 = Column(String)
    Contact2 = Column(String)
    NPWP = Column(String)
    NPWPdate = Column(DateTime)
    NPWPdateKukuh = Column(DateTime)
    Note1 = Column(String)
    Note2 = Column(String)
    CorAdd1 = Column(String)
    CorAdd2 = Column(String)
    CorAdd3 = Column(String)
    CorAdd4 = Column(String)
    CorCityID = Column(String)
    CorCountryID = Column(String)
    CorZipCode = Column(String)
    CorPhone1 = Column(String)
    CorPhone2 = Column(String)
    CorFax1 = Column(String)
    CorFax2 = Column(String)
    CorEmail = Column(String)
    CorContact1 = Column(String)
    CorContact2 = Column(String)
    Inactive = Column(Boolean)
    UserID = Column(String)


class T_Tax(Base):
    __tablename__ = 'Tax'
    TaxID = Column(String, primary_key=True)
    Name = Column(String)
    Amount = Column(Integer)


class T_TranMain(Base):
    __tablename__ = 'TranMain'
    TranMain = Column(String, primary_key=True)
    CompanyID = Column(String)
    BranchID = Column(String)
    DepartmentID = Column(String)


class T_TranType(Base):
    __tablename__ = 'TranType'
    TType = Column(String, primary_key=True)
    Name = Column(String)
    CorVoucherType = Column(String)
    Modul = Column(String)
    HeadDC = Column(String)
    FoGroup = Column(Boolean)


class T_Unit(Base):
    __tablename__ = 'Unit'
    UnitID = Column(String, primary_key=True)
    Name = Column(String)


class T_UserGroupMain(Base):
    __tablename__ = 'UserGroupMain'
    OffCode = Column(String, primary_key=True)
    UserGroupId = Column(String)
    UserGroupName = Column(String)
    Modul = Column(String)


class T_UserGroupMenuButton(Base):
    __tablename__ = 'UserGroupMenuButton'
    OffCode = Column(String, primary_key=True)
    UserGroupId = Column(String)
    MenuId = Column(String)
    UserGroupName = Column(String)
    bOpen = Column(String)
    bAdd = Column(String)
    bEdit = Column(String)
    bDelete = Column(String)
    bPrint = Column(String)


class T_UserMain(Base):
    __tablename__ = 'UserMain'
    OffCode = Column(String, primary_key=True)
    UserId = Column(String)
    UserGroupId = Column(String)
    UserName = Column(String)
    UserRank = Column(Integer)
    UserLogon = Column(Boolean)
    UserLastLogon = Column(DateTime)
    UserSpecial = Column(Boolean)
    UserPassword = Column(String)
    DeptID = Column(String)
    UserDateInp = Column(DateTime)
    UserIDInp = Column(String)
    Active = Column(String)


class T_Vendor(Base):
    __tablename__ = 'Vendor'
    PartnerID = Column(String, primary_key=True)
    PartnerName = Column(String)
    Ident = Column(String)
    OrgType = Column(String)
    Customer = Column(String)
    Vendor = Column(String)
    Principal = Column(String)
    Address1 = Column(String)
    Address2 = Column(String)
    Address3 = Column(String)
    Address4 = Column(String)
    CityID = Column(String)
    CountryID = Column(String)
    ZipCode = Column(String)
    Phone1 = Column(String)
    Phone2 = Column(String)
    Fax1 = Column(String)
    Fax2 = Column(String)
    Email = Column(String)
    Contact1 = Column(String)
    Contact2 = Column(String)
    NPWP = Column(String)
    NPWPdate = Column(DateTime)
    NPWPKukuh = Column(String)
    NPWPdateKukuh = Column(DateTime)
    NPWP1 = Column(String)
    NPWPdate1 = Column(DateTime)
    NPWPKukuh1 = Column(String)
    NPWPdateKukuh1 = Column(DateTime)
    APITU = Column(String)
    SPR = Column(String)
    SIUP = Column(String)
    Note1 = Column(String)
    Note2 = Column(String)
    CorAdd1 = Column(String)
    CorAdd2 = Column(String)
    CorAdd3 = Column(String)
    CorAdd4 = Column(String)
    CorCityID = Column(String)
    CorCountryID = Column(String)
    CorZipCode = Column(String)
    CorPhone1 = Column(String)
    CorPhone2 = Column(String)
    CorFax1 = Column(String)
    CorFax2 = Column(String)
    CorEmail = Column(String)
    CorContact1 = Column(String)
    CorContact2 = Column(String)
    Active = Column(String)
    UserID = Column(String)
