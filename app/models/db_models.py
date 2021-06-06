# coding: utf-8
from sqlalchemy import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import String, String, Integer, DateTime, Boolean

metadata = MetaData()


t_APPO_D = Table(
    'APPO_D', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType', String),
    Column('Account', String),
    Column('DivID', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('RefVou', String),
    Column('RefNO', Integer),
    Column('RefMainDoc', String),
    Column('RefPreDoc', String),
    Column('RefDetailDoc', String),
    Column('RefOthDoc', String),
    Column('TranDocD', String),
    Column('RefD1', String),
    Column('RefD2', String),
    Column('MerkID', String),
    Column('ThingType', String),
    Column('ThingID', String),
    Column('SerialID', String),
    Column('Descript', String),
    Column('Qty', Integer),
    Column('UnitID', String),
    Column('UnitPrice', Integer),
    Column('DiscAmount', Integer),
    Column('RefCur', String),
    Column('RefAmount', Integer),
    Column('Rate', Integer),
    Column('AmountD', Integer),
    Column('BalanceD', Integer),
    Column('TaxAmount', Integer),
    Column('TaxAmount1', Integer),
    Column('OthCost', Integer)
)


t_APPO_H = Table(
    'APPO_H', metadata,
    Column('VoucherID', String),
    Column('Account', String),
    Column('Cur', String),
    Column('DateDay', DateTime),
    Column('DateDue', DateTime),
    Column('TType', String),
    Column('PartnerName', String),
    Column('PartnerID', String),
    Column('Receiver', String),
    Column('MainDoc', String),
    Column('PreDoc', String),
    Column('DetailDoc', String),
    Column('OthDoc', String),
    Column('TranDoc', String),
    Column('Ref1', String),
    Column('Ref2', String),
    Column('TotalDiscount', Integer),
    Column('TotalTax', Integer),
    Column('TotalTax1', Integer),
    Column('SubTotal', Integer),
    Column('GrandTotal', Integer),
    Column('BalanceH', Integer),
    Column('TotalAdj', Integer),
    Column('TotalCost', Integer),
    Column('Journal', String),
    Column('RateJou', Integer),
    Column('Paid', String),
    Column('HeadJou', String),
    Column('UserID', String),
    Column('DateEntry', DateTime),
    Column('DateUpdate', DateTime),
    Column('UserLock', String),
    Column('AddDesc', String)
)


t_APProduct = Table(
    'APProduct', metadata,
    Column('Item_ID_NV', String),
    Column('Item_Desc_NV', String),
    Column('Item_Acc_NV', String)
)


t_APVou_D = Table(
    'APVou_D', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType', String),
    Column('Account', String),
    Column('DivID', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('RefVou', String),
    Column('RefNO', Integer),
    Column('RefMainDoc', String),
    Column('RefPreDoc', String),
    Column('RefDetailDoc', String),
    Column('RefOthDoc', String),
    Column('TranDocD', String),
    Column('RefD1', String),
    Column('RefD2', String),
    Column('MerkID', String),
    Column('ThingType', String),
    Column('ThingID', String),
    Column('SerialID', String),
    Column('Descript', String),
    Column('Qty', Integer),
    Column('UnitID', String),
    Column('UnitPrice', Integer),
    Column('DiscAmount', Integer),
    Column('RefCur', String),
    Column('RefAmount', Integer),
    Column('Rate', Integer),
    Column('AmountD', Integer),
    Column('BalanceD', Integer),
    Column('TaxAmount', Integer),
    Column('TaxAmount1', Integer),
    Column('OthCost', Integer)
)


t_APVou_D1 = Table(
    'APVou_D1', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType1', String),
    Column('Account1', String),
    Column('RefVou1', String),
    Column('RefNO1', Integer),
    Column('RefMainDoc1', String),
    Column('RefPreDoc1', String),
    Column('RefDetailDoc1', String),
    Column('RefOthDoc1', String),
    Column('TranDocD1', String),
    Column('RefD11', String),
    Column('RefD21', String),
    Column('MerkID1', String),
    Column('ThingType1', String),
    Column('ThingID1', String),
    Column('SerialID1', String),
    Column('Descript1', String),
    Column('Qty1', Integer),
    Column('UnitID1', String),
    Column('UnitPrice1', Integer),
    Column('DiscAmount1', Integer),
    Column('RefCur1', String),
    Column('RefAmount1', Integer),
    Column('Rate1', Integer),
    Column('AmountD1', Integer),
    Column('BalanceD1', Integer),
    Column('TaxAmount1', Integer),
    Column('TaxAmount11', Integer),
    Column('OthCost1', Integer)
)


t_APVou_H = Table(
    'APVou_H', metadata,
    Column('VoucherID', String),
    Column('Account', String),
    Column('Cur', String),
    Column('DateDay', DateTime),
    Column('DateDue', DateTime),
    Column('TType', String),
    Column('PartnerName', String),
    Column('PartnerID', String),
    Column('Receiver', String),
    Column('MainDoc', String),
    Column('PreDoc', String),
    Column('DetailDoc', String),
    Column('OthDoc', String),
    Column('TranDoc', String),
    Column('Ref1', String),
    Column('Ref2', String),
    Column('TotalDiscount', Integer),
    Column('TotalTax', Integer),
    Column('TotalTax1', Integer),
    Column('SubTotal', Integer),
    Column('GrandTotal', Integer),
    Column('BalanceH', Integer),
    Column('TotalAdj', Integer),
    Column('TotalCost', Integer),
    Column('Journal', String),
    Column('RateJou', Integer),
    Column('Paid', String),
    Column('HeadJou', String),
    Column('UserID', String),
    Column('DateEntry', DateTime),
    Column('DateUpdate', DateTime),
    Column('UserLock', String),
    Column('AddDesc', String)
)


t_APVou_H1 = Table(
    'APVou_H1', metadata,
    Column('VoucherID', String),
    Column('POno', String),
    Column('PODate', String),
    Column('MainDoc1', String),
    Column('PreDoc1', String),
    Column('DetailDoc1', String),
    Column('OthDoc1', String),
    Column('Ref11', String),
    Column('Ref21', String),
    Column('TotalTax1', Integer),
    Column('TotalTax11', Integer),
    Column('GrandTotal1', Integer),
    Column('BalanceH1', Integer),
    Column('Paid1', String)
)


t_ARVou_D = Table(
    'ARVou_D', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType', String),
    Column('Account', String),
    Column('DivID', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('RefVou', String),
    Column('RefNO', Integer),
    Column('RefMainDoc', String),
    Column('RefPreDoc', String),
    Column('RefDetailDoc', String),
    Column('RefOthDoc', String),
    Column('TranDocD', String),
    Column('RefD1', String),
    Column('RefD2', String),
    Column('MerkID', String),
    Column('ThingType', String),
    Column('ThingID', String),
    Column('SerialID', String),
    Column('Descript', String),
    Column('Qty', Integer),
    Column('UnitID', String),
    Column('UnitPrice', Integer),
    Column('DiscAmount', Integer),
    Column('RefCur', String),
    Column('RefAmount', Integer),
    Column('Rate', Integer),
    Column('AmountD', Integer),
    Column('BalanceD', Integer),
    Column('TaxAmount', Integer),
    Column('TaxAmount1', Integer),
    Column('OthCost', Integer)
)


t_ARVou_D1 = Table(
    'ARVou_D1', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType1', String),
    Column('Account1', String),
    Column('RefVou1', String),
    Column('RefNO1', Integer),
    Column('RefMainDoc1', String),
    Column('RefPreDoc1', String),
    Column('RefDetailDoc1', String),
    Column('RefOthDoc1', String),
    Column('TranDocD1', String),
    Column('RefD11', String),
    Column('RefD21', String),
    Column('MerkID1', String),
    Column('ThingType1', String),
    Column('ThingID1', String),
    Column('SerialID1', String),
    Column('Descript1', String),
    Column('Qty1', Integer),
    Column('UnitID1', String),
    Column('UnitPrice1', Integer),
    Column('DiscAmount1', Integer),
    Column('RefCur1', String),
    Column('RefAmount1', Integer),
    Column('Rate1', Integer),
    Column('AmountD1', Integer),
    Column('BalanceD1', Integer),
    Column('TaxAmount1', Integer),
    Column('TaxAmount11', Integer),
    Column('OthCost1', Integer)
)


t_ARVou_H = Table(
    'ARVou_H', metadata,
    Column('VoucherID', String),
    Column('Account', String),
    Column('Cur', String),
    Column('DateDay', DateTime),
    Column('DateDue', DateTime),
    Column('TType', String),
    Column('PartnerName', String),
    Column('PartnerID', String),
    Column('Receiver', String),
    Column('MainDoc', String),
    Column('PreDoc', String),
    Column('DetailDoc', String),
    Column('OthDoc', String),
    Column('TranDoc', String),
    Column('Ref1', String),
    Column('Ref2', String),
    Column('TotalDiscount', Integer),
    Column('TotalTax', Integer),
    Column('TotalTax1', Integer),
    Column('SubTotal', Integer),
    Column('GrandTotal', Integer),
    Column('BalanceH', Integer),
    Column('TotalAdj', Integer),
    Column('TotalCost', Integer),
    Column('Journal', String),
    Column('RateJou', Integer),
    Column('Paid', String),
    Column('HeadJou', String),
    Column('UserID', String),
    Column('DateEntry', DateTime),
    Column('DateUpdate', DateTime),
    Column('UserLock', String),
    Column('AddDesc', String)
)


t_ARVou_H1 = Table(
    'ARVou_H1', metadata,
    Column('VoucherID', String),
    Column('POno', String),
    Column('PODate', String),
    Column('MainDoc1', String),
    Column('PreDoc1', String),
    Column('DetailDoc1', String),
    Column('OthDoc1', String),
    Column('Ref11', String),
    Column('Ref21', String),
    Column('TotalTax1', Integer),
    Column('TotalTax11', Integer),
    Column('GrandTotal1', Integer),
    Column('BalanceH1', Integer),
    Column('Paid1', String)
)


t_Asset = Table(
    'Asset', metadata,
    Column('OffCode', String),
    Column('AssetID', String),
    Column('Name', String),
    Column('AssetKindID', String)
)


t_AssetKind = Table(
    'AssetKind', metadata,
    Column('AssetKindID', String),
    Column('Name', String)
)


t_Bhs = Table(
    'Bhs', metadata,
    Column('captText', String),
    Column('bhsID', String),
    Column('ShowText', String)
)


t_BranchOffice = Table(
    'BranchOffice', metadata,
    Column('OffCode', String),
    Column('CompanyID', String),
    Column('CityID', String),
    Column('name', String)
)


t_CBAdv_D = Table(
    'CBAdv_D', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType', String),
    Column('Account', String),
    Column('DivID', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('RefVou', String),
    Column('RefNO', Integer),
    Column('RefMainDoc', String),
    Column('RefPreDoc', String),
    Column('RefDetailDoc', String),
    Column('RefOthDoc', String),
    Column('TranDocD', String),
    Column('RefD1', String),
    Column('RefD2', String),
    Column('MerkID', String),
    Column('ThingType', String),
    Column('ThingID', String),
    Column('SerialID', String),
    Column('Descript', String),
    Column('Qty', Integer),
    Column('UnitID', String),
    Column('UnitPrice', Integer),
    Column('DiscAmount', Integer),
    Column('RefCur', String),
    Column('RefAmount', Integer),
    Column('Rate', Integer),
    Column('AmountD', Integer),
    Column('BalanceD', Integer),
    Column('TaxAmount', Integer),
    Column('TaxAmount1', Integer),
    Column('OthCost', Integer)
)


t_CBAdv_D1 = Table(
    'CBAdv_D1', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType1', String),
    Column('Account1', String),
    Column('RefVou1', String),
    Column('RefNO1', Integer),
    Column('RefMainDoc1', String),
    Column('RefPreDoc1', String),
    Column('RefDetailDoc1', String),
    Column('RefOthDoc1', String),
    Column('TranDocD1', String),
    Column('RefD11', String),
    Column('RefD21', String),
    Column('MerkID1', String),
    Column('ThingType1', String),
    Column('ThingID1', String),
    Column('SerialID1', String),
    Column('Descript1', String),
    Column('Qty1', Integer),
    Column('UnitID1', String),
    Column('UnitPrice1', Integer),
    Column('DiscAmount1', Integer),
    Column('RefCur1', String),
    Column('RefAmount1', Integer),
    Column('Rate1', Integer),
    Column('AmountD1', Integer),
    Column('BalanceD1', Integer),
    Column('TaxAmount1', Integer),
    Column('TaxAmount11', Integer),
    Column('OthCost1', Integer)
)


t_CBAdv_H = Table(
    'CBAdv_H', metadata,
    Column('VoucherID', String),
    Column('Account', String),
    Column('Cur', String),
    Column('DateDay', DateTime),
    Column('DateDue', DateTime),
    Column('TType', String),
    Column('PartnerName', String),
    Column('PartnerID', String),
    Column('Receiver', String),
    Column('MainDoc', String),
    Column('PreDoc', String),
    Column('DetailDoc', String),
    Column('OthDoc', String),
    Column('TranDoc', String),
    Column('Ref1', String),
    Column('Ref2', String),
    Column('TotalDiscount', Integer),
    Column('TotalTax', Integer),
    Column('TotalTax1', Integer),
    Column('SubTotal', Integer),
    Column('GrandTotal', Integer),
    Column('BalanceH', Integer),
    Column('TotalAdj', Integer),
    Column('TotalCost', Integer),
    Column('Journal', String),
    Column('RateJou', Integer),
    Column('Paid', String),
    Column('HeadJou', String),
    Column('UserID', String),
    Column('DateEntry', DateTime),
    Column('DateUpdate', DateTime),
    Column('UserLock', String),
    Column('AddDesc', String)
)


t_CBBalance = Table(
    'CBBalance', metadata,
    Column('ThingId', String),
    Column('PeriodID', String),
    Column('Out', Integer),
    Column('In', Integer),
    Column('BegBalance', Integer),
    Column('EndBalance', Integer)
)


t_CBVou_D = Table(
    'CBVou_D', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType', String),
    Column('Account', String),
    Column('DivID', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('RefVou', String),
    Column('RefNO', Integer),
    Column('RefMainDoc', String),
    Column('RefPreDoc', String),
    Column('RefDetailDoc', String),
    Column('RefOthDoc', String),
    Column('TranDocD', String),
    Column('RefD1', String),
    Column('RefD2', String),
    Column('MerkID', String),
    Column('ThingType', String),
    Column('ThingID', String),
    Column('SerialID', String),
    Column('Descript', String),
    Column('Qty', Integer),
    Column('UnitID', String),
    Column('UnitPrice', Integer),
    Column('DiscAmount', Integer),
    Column('RefCur', String),
    Column('RefAmount', Integer),
    Column('Rate', Integer),
    Column('AmountD', Integer),
    Column('BalanceD', Integer),
    Column('TaxAmount', Integer),
    Column('TaxAmount1', Integer),
    Column('OthCost', Integer)
)


t_CBVou_D1 = Table(
    'CBVou_D1', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType1', String),
    Column('Account1', String),
    Column('RefVou1', String),
    Column('RefNO1', Integer),
    Column('RefMainDoc1', String),
    Column('RefPreDoc1', String),
    Column('RefDetailDoc1', String),
    Column('RefOthDoc1', String),
    Column('TranDocD1', String),
    Column('RefD11', String),
    Column('RefD21', String),
    Column('MerkID1', String),
    Column('ThingType1', String),
    Column('ThingID1', String),
    Column('SerialID1', String),
    Column('Descript1', String),
    Column('Qty1', Integer),
    Column('UnitID1', String),
    Column('UnitPrice1', Integer),
    Column('DiscAmount1', Integer),
    Column('RefCur1', String),
    Column('RefAmount1', Integer),
    Column('Rate1', Integer),
    Column('AmountD1', Integer),
    Column('BalanceD1', Integer),
    Column('TaxAmount1', Integer),
    Column('TaxAmount11', Integer),
    Column('OthCost1', Integer)
)


t_CBVou_H = Table(
    'CBVou_H', metadata,
    Column('VoucherID', String),
    Column('Account', String),
    Column('Cur', String),
    Column('DateDay', DateTime),
    Column('DateDue', DateTime),
    Column('TType', String),
    Column('PartnerName', String),
    Column('PartnerID', String),
    Column('Receiver', String),
    Column('MainDoc', String),
    Column('PreDoc', String),
    Column('DetailDoc', String),
    Column('OthDoc', String),
    Column('TranDoc', String),
    Column('Ref1', String),
    Column('Ref2', String),
    Column('TotalDiscount', Integer),
    Column('TotalTax', Integer),
    Column('TotalTax1', Integer),
    Column('SubTotal', Integer),
    Column('GrandTotal', Integer),
    Column('BalanceH', Integer),
    Column('TotalAdj', Integer),
    Column('TotalCost', Integer),
    Column('Journal', String),
    Column('RateJou', Integer),
    Column('Paid', String),
    Column('HeadJou', String),
    Column('UserID', String),
    Column('DateEntry', DateTime),
    Column('DateUpdate', DateTime),
    Column('UserLock', String),
    Column('AddDesc', String)
)


t_Category = Table(
    'Category', metadata,
    Column('CategoryID', String),
    Column('CategoryDesc', String)
)


t_City = Table(
    'City', metadata,
    Column('CityID', String),
    Column('Name', String),
    Column('countryID', String),
    Column('locKind', String)
)


t_Company = Table(
    'Company', metadata,
    Column('CompanyID', String),
    Column('CompanyName', String),
    Column('CompanyName1', String),
    Column('CompanyHead', String),
    Column('CompanyAddress', String),
    Column('CompanyPhone', String)
)


t_Country = Table(
    'Country', metadata,
    Column('CountryID', String),
    Column('Name', String)
)


t_Curency = Table(
    'Curency', metadata,
    Column('Cur', String),
    Column('Name', String),
    Column('CountryID', String),
    Column('Rate', Integer),
    Column('Mark', String)
)


t_Customer = Table(
    'Customer', metadata,
    Column('PartnerID', String),
    Column('PartnerName', String),
    Column('Ident', String),
    Column('OrgType', String),
    Column('Address1', String),
    Column('Address2', String),
    Column('Address3', String),
    Column('Address4', String),
    Column('CityID', String),
    Column('CountryID', String),
    Column('ZipCode', String),
    Column('Phone1', String),
    Column('Phone2', String),
    Column('Fax1', String),
    Column('Fax2', String),
    Column('Email', String),
    Column('Contact1', String),
    Column('Contact2', String),
    Column('NPWP', String),
    Column('NPWPdate', DateTime),
    Column('NPWPKukuh', String),
    Column('NPWPdateKukuh', DateTime),
    Column('NPWP1', String),
    Column('NPWPdate1', DateTime),
    Column('NPWPKukuh1', String),
    Column('NPWPdateKukuh1', DateTime),
    Column('APITU', String),
    Column('SPR', String),
    Column('SIUP', String),
    Column('Note1', String),
    Column('Note2', String),
    Column('CorAdd1', String),
    Column('CorAdd2', String),
    Column('CorAdd3', String),
    Column('CorAdd4', String),
    Column('CorCityID', String),
    Column('CorCountryID', String),
    Column('CorZipCode', String),
    Column('CorPhone1', String),
    Column('CorPhone2', String),
    Column('CorFax1', String),
    Column('CorFax2', String),
    Column('CorEmail', String),
    Column('CorContact1', String),
    Column('CorContact2', String),
    Column('Active', String),
    Column('UserID', String)
)

# TODO: cari, ngga ada di db access
t_DType = Table(
    'DType', metadata,
    Column('DType', String),
    Column('Name', String),
    Column('CorVoucherType', String),
    Column('Modul', String),
    Column('HeadDC', String),
    Column('FoGroup', String)
)


t_DailyTranJob = Table(
    'DailyTranJob', metadata,
    Column('ProductID', String),
    Column('name', String),
    Column('account', String),
    Column('GroupProdID', String),
    Column('AssetKind', String),
    Column('inv', Boolean),
    Column('Emod', Boolean),
    Column('Mmod', Boolean),
    Column('Amod', Boolean)
)


t_Department = Table(
    'Department', metadata,
    Column('DepartmentID', String),
    Column('DepartmentName', String),
    Column('DepartmentHead', String),
    Column('OffCode', String)
)


t_DetDemPeriod = Table(
    'DetDemPeriod', metadata,
    Column('DD_Period_ID_VC', String),
    Column('DD_Start_Day_SI', Integer),
    Column('DD_End_Day_SI', Integer),
    Column('DD_Desc_VC', String)
)


t_Division = Table(
    'Division', metadata,
    Column('OffCode', String),
    Column('DivID', String),
    Column('DivName', String)
)


t_Forex = Table(
    'Forex', metadata,
    Column('ForexID', String),
    Column('ForexCode', String),
    Column('ForexDesc', String),
    Column('ForexCountryID', String)
)


t_GetDatetime = Table(
    'GetDatetime', metadata,
    Column('OffCode', String),
    Column('UserID', String),
    Column('datedaytime', DateTime)
)

t_gLen = Table(
    'gLen', metadata,
    Column('gNumber', String),
    Column('gLenThing', Integer),
    Column('gLenVoucher', Integer),
    Column('gLenOffCode', Integer),
    Column('gLenCounter', Integer),
    Column('gLenTranID', Integer),
    Column('gMCounter', Integer),
    Column('gLenAccount', Integer)
)


t_InvDesc = Table(
    'InvDesc', metadata,
    Column('OffCode', String),
    Column('InvID', String),
    Column('JobKind', String),
    Column('InvType', String),
    Column('Account', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('InvDesc', String)
)


t_Item = Table(
    'Item', metadata,
    Column('OffCode', String),
    Column('itemID', String),
    Column('InvID', String),
    Column('ItemDesc', String),
    Column('GroupItem', String),
    Column('Account', String),
    Column('Cur', String),
    Column('HrgStd', Integer)
)


t_JobKind = Table(
    'JobKind', metadata,
    Column('OffCode', String),
    Column('JobKind', String),
    Column('JobName', String),
    Column('DivID', String)
)


t_JobOrder = Table(
    'JobOrder', metadata,
    Column('OffCode', String),
    Column('JobID', String),
    Column('JobKind', String),
    Column('DateDay', DateTime),
    Column('Ident', String),
    Column('PartnerID', String),
    Column('PartnerName', String),
    Column('Descript', String),
    Column('CustomerName', String),
    Column('Weight', String),
    Column('Measurement', String),
    Column('Utility', String),
    Column('Dishpack', String),
    Column('Clothing', String),
    Column('Glass', String),
    Column('Furniture', String),
    Column('Comment', String),
    Column('AllPacker', String),
    Column('Packer', String),
    Column('Freelance', String),
    Column('ElfBox', String),
    Column('ElfBak', String),
    Column('LooseBak', String),
    Column('L300Box', String),
    Column('PickUp', String),
    Column('Panther', String),
    Column('LCLshipment', String),
    Column('WoodenLiftvan', String),
    Column('CartonLiftvan', String),
    Column('FCLshipment', String),
    Column('FCL20', String),
    Column('FCL40', String),
    Column('LoosePack', String),
    Column('Liftvan', String),
    Column('Departure', String),
    Column('PaymentType', String),
    Column('AddPay', String),
    Column('OrderByName', String),
    Column('OrderByDate', String),
    Column('CargoDivName', String),
    Column('CargoDivDate', String),
    Column('MPdivName', String),
    Column('MPdivDate', String),
    Column('Remark', String),
    Column('DateUpdate', DateTime),
    Column('active', String)
)


t_JobOrderX = Table(
    'JobOrderX', metadata,
    Column('OffCode', String),
    Column('JobID', String),
    Column('JobKind', String),
    Column('DateDay', DateTime),
    Column('Ident', String),
    Column('PartnerID', String),
    Column('PartnerName', String),
    Column('KindOfWork', String),
    Column('ShipConsignee', String),
    Column('NameOfGood', String),
    Column('CustomerRef', String),
    Column('LoadPort', String),
    Column('DischargePort', String),
    Column('VesselFlight', String),
    Column('ETA', DateTime),
    Column('ETD', DateTime),
    Column('ClearanceDate', DateTime),
    Column('DeliveryDate', DateTime),
    Column('BlAwbM', String),
    Column('BlAwbH', String),
    Column('Service', String),
    Column('ContSize', String),
    Column('ContainerNo', String),
    Column('QofGood', Integer),
    Column('Weight', Integer),
    Column('Measurement', String),
    Column('ShippingName', String),
    Column('WarehouseName', String),
    Column('TypeOfService', String),
    Column('EPTEBc23Peb30Date', DateTime),
    Column('PTBc23Peb30', String),
    Column('PTPE', String),
    Column('PTInvoice', String),
    Column('PTPacking', String),
    Column('PTBlAwbAsli', String),
    Column('PTAsuransi', String),
    Column('PTSK', String),
    Column('PTKonlak', String),
    Column('PTSSBP', String),
    Column('GCPib20Peb30', String),
    Column('GCPE', String),
    Column('GCInvoice', String),
    Column('GCPacking', String),
    Column('GCBlAwbAsli', String),
    Column('GCSK', String),
    Column('GCSTTJ', String),
    Column('GCIzinDep', String),
    Column('GCCIS', String),
    Column('GCIP', String),
    Column('GCMaster', String),
    Column('GCNPIK', String),
    Column('GCSKBPPN', String),
    Column('GCAsuransi', String),
    Column('GCSSPCP', String),
    Column('Driver', String),
    Column('Truck', String),
    Column('Condition', String),
    Column('Remark', String),
    Column('active', String)
)


t_MaterialType = Table(
    'MaterialType', metadata,
    Column('MateID', String),
    Column('MateDesc', String)
)


t_Menu = Table(
    'Menu', metadata,
    Column('OffCode', String),
    Column('MenuId', String),
    Column('Name', String),
    Column('FrmName', String),
    Column('Remark', String),
    Column('UserUse', Boolean)
)


t_Merk = Table(
    'Merk', metadata,
    Column('MerkID', String),
    Column('Name', String),
    Column('Descript', String),
    Column('GroupMerk', String)
)


t_Paste_Errors = Table(
    'Paste Errors', metadata,
    Column('Field0', String) #TODO: DI DB TIPENYA LONG TEXT
)


t_PaySalesTran = Table(
    'PaySalesTran', metadata,
    Column('PayID', String),
    Column('PayKindID', String),
    Column('PayDesc', String),
    Column('Account', String),
    Column('CostType', String),
    Column('Cost', Integer),
    Column('CostAccount', String),
    Column('Mark', String),
    Column('Active', String)
)


t_PaymentVoucher = Table(
    'PaymentVoucher', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('PayID', String),
    Column('IdentityNo', String),
    Column('IdentityName', String),
    Column('Amount', Integer),
    Column('OtherAmount', Integer),
    Column('Cost', Integer),
    Column('TotalPay', Integer),
    Column('BalanceD', Integer)
)


t_PeriodACC = Table(
    'PeriodACC', metadata,
    Column('PeriodID', String),
    Column('PeriodName', String),
    Column('StartDate', DateTime),
    Column('EndDate', DateTime),
    Column('YearPeriod', String),
    Column('CloseStat', String),
    Column('CloseDate', DateTime),
    Column('UserID', String),
    Column('UserIDClose', String)
)


t_PeriodFO = Table(
    'PeriodFO', metadata,
    Column('OffCode', String),
    Column('PeriodID', String),
    Column('PeriodDate', DateTime)
)


t_Port = Table(
    'Port', metadata,
    Column('PortCode_CH', String),
    Column('PortName_CH', String),
    Column('PortType_CH', String),
    Column('PortTrade_CH', String),
    Column('PortRate_NU', Integer),
    Column('PortCountry_CH', String),
    Column('CityID_CH', String),
    Column('LocKind', String)
)


t_PrincipalMain = Table(
    'PrincipalMain', metadata,
    Column('Prin_Code_CH', String),
    Column('Prin_Name_CH', String),
    Column('Prin_Name1_CH', String),
    Column('Prin_Address1_CH', String),
    Column('Prin_Address2_CH', String),
    Column('Prin_Address3_CH', String),
    Column('Prin_Address4_CH', String),
    Column('Prin_Address5_CH', String),
    Column('Prin_City_CH', String),
    Column('Prin_Country_CH', String),
    Column('Prin_Zip_CH', String),
    Column('Prin_Phone_CH', String),
    Column('Prin_Fax_CH', String),
    Column('Prin_Email_CH', String),
    Column('Prin_Type_CH', String),
    Column('Prin_Inactive_BT', Boolean),
    Column('Prin_UserID_CH', String),
    Column('Prin_BL_Code_CH', String),
    Column('Prin_KtrAs_CH', String)
)


t_ProductBuy = Table(
    'ProductBuy', metadata,
    Column('ProductID', String),
    Column('name', String),
    Column('account', String),
    Column('UnitPrice', Integer),
    Column('GroupProdID', String),
    Column('AssetKind', String),
    Column('inv', String),
    Column('Emod', String),
    Column('Mmod', String),
    Column('Amod', String)
)


t_ProductSale = Table(
    'ProductSale', metadata,
    Column('ProductID', String),
    Column('name', String),
    Column('account', String),
    Column('Cur', String),
    Column('UnitPrice', Integer),
    Column('GroupProdID', String),
    Column('AssetKind', String),
    Column('inv', String),
    Column('Emod', String),
    Column('Mmod', String),
    Column('Amod', String)
)


t_Rate = Table(
    'Rate', metadata,
    Column('Cur1', String),
    Column('Cur2', String),
    Column('RateAmount', Integer)
)


t_SaleVou_D = Table(
    'SaleVou_D', metadata,
    Column('VoucherID', String),
    Column('NoDet', Integer),
    Column('DType', String),
    Column('Account', String),
    Column('DivID', String),
    Column('Tax', String),
    Column('Tax1', String),
    Column('RefVou', String),
    Column('RefNO', Integer),
    Column('RefMainDoc', String),
    Column('RefPreDoc', String),
    Column('RefDetailDoc', String),
    Column('RefOthDoc', String),
    Column('TranDocD', String),
    Column('RefD1', String),
    Column('RefD2', String),
    Column('ThingType', String),
    Column('ThingID', String),
    Column('SerialID', String),
    Column('Descript', String),
    Column('Qty', Integer),
    Column('UnitID', String),
    Column('UnitPrice', Integer),
    Column('DiscAmount', Integer),
    Column('RefCur', String),
    Column('RefAmount', Integer),
    Column('Rate', Integer),
    Column('AmountD', Integer),
    Column('BalanceD', Integer),
    Column('TaxAmount', Integer),
    Column('TaxAmount1', Integer),
    Column('OthCost', Integer)
)


t_SaleVou_H = Table(
    'SaleVou_H', metadata,
    Column('VoucherID', String),
    Column('Account', String),
    Column('Cur', String),
    Column('DateDay', DateTime),
    Column('DateDue', DateTime),
    Column('TType', String),
    Column('PartnerName', String),
    Column('PartnerID', String),
    Column('Receiver', String),
    Column('MainDoc', String),
    Column('PreDoc', String),
    Column('DetailDoc', String),
    Column('OthDoc', String),
    Column('TranDoc', String),
    Column('Ref1', String),
    Column('Ref2', String),
    Column('TotalDiscount', Integer),
    Column('TotalTax', Integer),
    Column('TotalTax1', Integer),
    Column('SubTotal', Integer),
    Column('GrandTotal', Integer),
    Column('BalanceH', Integer),
    Column('TotalAdj', Integer),
    Column('TotalCost', Integer),
    Column('Journal', String),
    Column('RateJou', Integer),
    Column('Paid', String),
    Column('HeadJou', String),
    Column('UserID', String),
    Column('DateEntry', DateTime),
    Column('DateUpdate', DateTime),
    Column('UserLock', String),
    Column('AddDesc', String)
)


t_Sales = Table(
    'Sales', metadata,
    Column('OffCode', String),
    Column('SalesId', String),
    Column('Name', String),
    Column('Comm', Integer),
    Column('Active', String)
)


t_SetupSystem = Table(
    'SetupSystem', metadata,
    Column('OffCode', String),
    Column('Address1', String),
    Column('Address2', String),
    Column('Address3', String),
    Column('NPWP', String),
    Column('NPWPDate', String),
    Column('NPWPKukuh', String),
    Column('NPWPDateKukuh', String),
    Column('AccSubgroupPL', String),
    Column('AccountPLDitahan', String),
    Column('AccountPLBerJalan', String),
    Column('InvoiceName', String),
    Column('Tax1Name', String),
    Column('Tax1Title', String),
    Column('Name1', String),
    Column('Name2', String),
    Column('Name3', String),
    Column('TaxStd', String),
    Column('TaxSdn', String),
    Column('ARTaxAccount', String),
    Column('ARTax1Account', String),
    Column('SelisihAcckurs', String),
    Column('DiscountAcc', String),
    Column('userlock', String)
)


t_Supplier = Table(
    'Supplier', metadata,
    Column('PartnerID', String),
    Column('PartnerName', String),
    Column('Address1', String),
    Column('Address2', String),
    Column('Address3', String),
    Column('Address4', String),
    Column('CityID', String),
    Column('CountryID', String),
    Column('ZipCode', String),
    Column('Phone1', String),
    Column('Phone2', String),
    Column('Fax1', String),
    Column('Fax2', String),
    Column('Email', String),
    Column('Contact1', String),
    Column('Contact2', String),
    Column('NPWP', String),
    Column('NPWPdate', DateTime),
    Column('NPWPdateKukuh', DateTime),
    Column('Note1', String),
    Column('Note2', String),
    Column('CorAdd1', String),
    Column('CorAdd2', String),
    Column('CorAdd3', String),
    Column('CorAdd4', String),
    Column('CorCityID', String),
    Column('CorCountryID', String),
    Column('CorZipCode', String),
    Column('CorPhone1', String),
    Column('CorPhone2', String),
    Column('CorFax1', String),
    Column('CorFax2', String),
    Column('CorEmail', String),
    Column('CorContact1', String),
    Column('CorContact2', String),
    Column('Inactive', Boolean),
    Column('UserID', String)
)


t_Tax = Table(
    'Tax', metadata,
    Column('TaxID', String),
    Column('Name', String),
    Column('Amount', Integer)
)


t_TranMain = Table(
    'TranMain', metadata,
    Column('TranMain', String),
    Column('CompanyID', String),
    Column('BranchID', String),
    Column('DepartmentID', String)
)


t_TranType = Table(
    'TranType', metadata,
    Column('TType', String),
    Column('Name', String),
    Column('CorVoucherType', String),
    Column('Modul', String),
    Column('HeadDC', String),
    Column('FoGroup', Boolean)
)


t_Unit = Table(
    'Unit', metadata,
    Column('UnitID', String),
    Column('Name', String)
)


t_UserGroupMain = Table(
    'UserGroupMain', metadata,
    Column('OffCode', String),
    Column('UserGroupId', String),
    Column('UserGroupName', String),
    Column('Modul', String)
)


t_UserGroupMenuButton = Table(
    'UserGroupMenuButton', metadata,
    Column('OffCode', String),
    Column('UserGroupId', String),
    Column('MenuId', String),
    Column('UserGroupName', String),
    Column('bOpen', String),
    Column('bAdd', String),
    Column('bEdit', String),
    Column('bDelete', String),
    Column('bPrint', String)
)


t_UserMain = Table(
    'UserMain', metadata,
    Column('OffCode', String),
    Column('UserId', String),
    Column('UserGroupId', String),
    Column('UserName', String),
    Column('UserRank', Integer),
    Column('UserLogon', Boolean),
    Column('UserLastLogon', DateTime),
    Column('UserSpecial', Boolean),
    Column('UserPassword', String),
    Column('DeptID', String),
    Column('UserDateInp', DateTime),
    Column('UserIDInp', String),
    Column('Active', String)
)


t_Vendor = Table(
    'Vendor', metadata,
    Column('PartnerID', String),
    Column('PartnerName', String),
    Column('Ident', String),
    Column('OrgType', String),
    Column('Customer', String),
    Column('Vendor', String),
    Column('Principal', String),
    Column('Address1', String),
    Column('Address2', String),
    Column('Address3', String),
    Column('Address4', String),
    Column('CityID', String),
    Column('CountryID', String),
    Column('ZipCode', String),
    Column('Phone1', String),
    Column('Phone2', String),
    Column('Fax1', String),
    Column('Fax2', String),
    Column('Email', String),
    Column('Contact1', String),
    Column('Contact2', String),
    Column('NPWP', String),
    Column('NPWPdate', DateTime),
    Column('NPWPKukuh', String),
    Column('NPWPdateKukuh', DateTime),
    Column('NPWP1', String),
    Column('NPWPdate1', DateTime),
    Column('NPWPKukuh1', String),
    Column('NPWPdateKukuh1', DateTime),
    Column('APITU', String),
    Column('SPR', String),
    Column('SIUP', String),
    Column('Note1', String),
    Column('Note2', String),
    Column('CorAdd1', String),
    Column('CorAdd2', String),
    Column('CorAdd3', String),
    Column('CorAdd4', String),
    Column('CorCityID', String),
    Column('CorCountryID', String),
    Column('CorZipCode', String),
    Column('CorPhone1', String),
    Column('CorPhone2', String),
    Column('CorFax1', String),
    Column('CorFax2', String),
    Column('CorEmail', String),
    Column('CorContact1', String),
    Column('CorContact2', String),
    Column('Active', String),
    Column('UserID', String)
)
