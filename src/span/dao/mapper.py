from datetime import datetime as dt
import cx_Oracle
import os
import numpy as np
import pandas as pd
from sqlalchemy.types import NVARCHAR
from sqlalchemy.engine import create_engine
from dateutil.relativedelta import relativedelta
from datetime import datetime
from multiprocessing import Pool
pd.options.display.max_rows=999
pd.options.display.max_columns=99
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'
import warnings
import logging
from .env import *
from ..core.logger import logger
warnings.simplefilter(action='ignore')


class Mapper(object):

    def __init__(self):

        return

    source_match_sql = "SELECT * FROM TC_HIS_FTR_MATCH WHERE TRADE_DATE BETWEEN '{start_date}' AND '{end_date}'"


    def _read_data(sql):
        print('read in bak func!!!')
        # conn = cx_Oracle.connect("biz", "biz123", "localhost/ORATEST")
        conn = cx_Oracle.connect(GetMainConnectString())
        cursor = conn.cursor()
        cursor.execute(sql)
        cols = np.array(cursor.description)[:, 0]
        data = []
        done = False
        while not done:
            try:
                record = cursor.fetchone()
                if record is None:
                    done = True
                else:
                    data.append(record)
            except UnicodeDecodeError:
                print('got an unicode error')
                pass
        df = pd.DataFrame(data, columns=cols)

        conn.close()
        return df


    def read_data(sql):
        print("read_data : {}".format(sql))
        t0 = dt.now()

        engine = create_engine(GetMainConnectString1())
        try:
            df = pd.read_sql_query(sql, engine)

        except UnicodeDecodeError:
            logging.error(sql)
        df.columns = [col.upper() for col in df.columns]
        df = df.reset_index(drop=True)
        t1 = dt.now()
        print('           successfully! shape:{}, time:{}'.format(df.shape, t1 - t0))
        logger.info('           successfully! shape:{}, time:{}'.format(df.shape, t1 - t0))
        return df


    def write_to_db(df, table_name):
        if not df.empty:
            try:
                date = df['TRADE_DATE'].unique()
                print('write data : {} shape:{}  date={}  now=[{}]'.format(table_name, df.shape, date, str(dt.now())))
                cols = df.dtypes[df.dtypes == 'object'].index
                type_mapping = {col: NVARCHAR(length=16) for col in cols}

                engine = create_engine(GetMainConnectString1())
                conn = engine.connect()
                df.to_sql(name=table_name, con=conn, if_exists='append', index=False, chunksize=10000, dtype=type_mapping)
                conn.close()
            except Exception as e:
                logging.error(str(e) + "failed to write data into {} on {} ".format(table_name, date))
                exit(e)
            else:
                logging.info("successfully write data into {} on {} ".format(table_name, date))
        else:
            logging.info("no data into {}".format(table_name))





