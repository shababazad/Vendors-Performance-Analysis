import pandas as pd
import sqlite3
import time
import logging
from Ingestion_db import ingest_db 

logging.basicConfig(
    filename='logs/get_vendor_summary.log',
    level =logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode ='a'
)

def create_vendor_summary(conn):
    vendor_sales_summary =pd.read_sql('''with FrieghtSummary as(
    select 
        VendorNumber ,
        sum(Freight) as FreightCost 
    from vendor_invoice 
    group by VendorNumber
    ),
    PurchaseSummary as(
         select
         p.VendorNumber,
         p.VendorName,
         p.Brand,
         p.Description,
         p.PurchasePrice,
         pp.Volume,
         pp.Price as ActualPrice,
         sum(p.Quantity) as TotalPurchaseQuantity,
         sum(p.Dollars) as TotalPurchaseDollars
     from purchases as p
     join purchase_prices pp
     on
     p.Brand = pp.Brand
     where p.purchasePrice >0
     group by p.VendorNumber ,p.VendorName,p.Brand,p.Description,p.PurchasePrice,pp.Price,pp.Price,pp.Volume
     order by TotalPurchaseDollars
    ),
    SalesSummary as(
        select 
        VendorNo,
        Brand,
        sum(SalesDollars) TotalSalesDollars,
        sum(Salesprice) TotalSalesPrice,
        sum(SalesQuantity) TotalSalesQuantity,
        sum(ExciseTax) TotalExciseTax
    from sales
    group by VendorNo,Brand

    )
    select
    ps.VendorNumber,
    ps.VendorName,
    ps.Brand,
    ps.Description,
    ps.PurchasePrice,
    ps.ActualPrice,
    ps.Volume,
    ps.TotalPurchaseQuantity,
    ps.TotalPurchaseDollars,
    ss.TotalSalesQuantity,
    ss.TotalSalesDollars,
    ss.TotalSalesPrice,
    ss.TotalExciseTax,
    fs.FreightCost
    from 
    PurchaseSummary ps
    left join SalesSummary ss
    on ps.Brand =ss.Brand
    and
    ps.VendorNumber=ss.VendorNo
    left join FrieghtSummary fs
    on ps.VendorNumber =fs.VendorNumber
    order by ps.TotalPurchaseDollars desc
    ''',conn)
    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''

    #changing datatypes to float
    df['Volume'] =df['Volume'].astype('float')

    #filling missing valuewith 0
    df.fillna(0,inplace=True)

    #removing spaces from categorical columns
    df['VendorName'] =df['VendorName'].str.strip()
    df['Description'] =df['Description'].str.strip()

    #creating new columns for better analysis'

    df["GrossProfit"] =df["TotalSalesDollars"]-df["TotalPurchaseDollars"]
    df["ProfitMargin"] =(df["GrossProfit"]/df["TotalSalesDollars"])*100
    df["StockTurnover"] = df["TotalSalesQuantity"]/df["TotalPurchaseQuantity"]
    df["SalestoPurchaseRatio"] = df["TotalSalesDollars"]/df["TotalPurchaseDollars"]

    return df

if __name__ =='__main__':
    #creating database connection
    conn =sqlite3.connect('inventory.db')

    logging.info('Creating Vendor Summary Table .....')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    #cleaning the data
    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    #ingesting the cleaing database
    logging.info('Ingesting the Data.....')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Ingestion Completed')
    
    

    
    