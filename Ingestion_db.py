import os
from sqlalchemy import create_engine
import logging
import time
import pandas as pd

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def ingest_db(df,table_name,engine):
    df.to_sql(table_name,engine, if_exists='replace',index=False)


engine =create_engine('sqlite:///inventory.db')




def loadRawdata():
    '''This function simply collect the data from the server or a folder
        and injest the data in our database that we had created (inventory.db
        for bigger csv files it stores them in chunks but for the smaller one it
        directly stored them using .tosql inbuilt function)'''
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            
            path=os.path.join('data',file)
            table_name=file[:-4]
        
            logging.info(f'Ingesting : {file} in db')
            print("Ingestion of file started: ",file)
            
            if(file == 'sales.csv'):
                first=True
                for chunk in pd.read_csv(path,chunksize=100000):
                    chunk.to_sql(
                        table_name,
                        engine,
                        if_exists= 'replace' if first else 'append',
                        index=False)
                    
                    first=False
            else:
                df=pd.read_csv(path)
                df.to_sql(
                    table_name,
                    engine,
                    if_exists='replace',
                    index=False
                )
            print("Ingestion of the file completed: ",file)
    end=time.time()
    total_time=(end-start)/60
    logging.info('-------------Ingestion Complete-------------')
    logging.info(f'\nTotal Time taken : {total_time} minutes')
        
                
                
if __name__ == '__main__':
    loadRawdata()