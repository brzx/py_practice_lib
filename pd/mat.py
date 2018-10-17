import os, sys, shutil, time, datetime, cx_Oracle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from pylab import *
from envdb import *
from functools import reduce

def getDF(fo):
    df = pd.read_csv(os.path.join('./tablecount/', fo), names=['tabnm','date','count'])
    df.rename(columns={'count' : str(df['date'].unique()[0])[-4:]}, inplace=True)
    del df['date']
    return df

def combineDF(d1, d2):
    nd = pd.merge(d1, d2, on='tabnm', how='outer')
    return nd

def generateImg(name, ns):
    plt.figure(figsize=(16,8))
    #plt.rcParams["figure.figsize"] = (16,8)
    plt.plot(ns.index, ns.values, color='k', marker='o', linestyle='dashed')
    plt.title(name)
    plt.xlabel('date')
    plt.ylabel('count')
    plt.savefig(name + '_' + datetime.datetime.now().strftime('%Y%m%d') + '_' + str(time.time()) + '.png')
    #plt.show()
    print('%s has been generated' % (name,))

def getTableRows():
    env = EnvSetOracle()
    env.setCountryProd()
    ocap = OracleConnect(env.host, env.port, env.dbname, env.username, env.userpwd)
    cursor = ocap.getCursor()
    cursor.callproc('count_rows')
    cursor.close()
    sql = 'select table_name, count_date, num_rows from table_rows'
    cur = ocap.getCursor()
    cur.execute(sql)
    reap = cur.fetchall()
    data = DataFrame(reap)
    print(data)
    filename = 'rn_' + datetime.datetime.now().strftime('%Y%m%d') + '_' + str(time.time()) + '.csv'
    data.to_csv(filename, index=False, header=False)
    cur.close()
    ocap.closeConn()
    shutil.move(filename, './tablecount/'+filename)

def printList(df, no):
    if no == 1:
        nameLi = list(df.index.values)
        for index, nl in enumerate(nameLi):
            print('%d->%s' % (index, nl))
        print('%s->back' % (len(nameLi),))
        return nameLi
    elif no == 2:
        last1 = ndf2[df.columns.values[-1:]]
        last2 = ndf2[df.columns.values[-2:-1]]
        last1.rename(columns={last1.columns.values[0] : 'cc'}, inplace=True)
        last2.rename(columns={last2.columns.values[0] : 'cc'}, inplace=True)
        fdf1 = (last1-last2)/last2
        fdf2 = fdf1[abs(fdf1)['cc']>0.1]
        nameLi = list(fdf2.index.values)
        for index, nl in enumerate(nameLi):
            print('%d->%s' % (index, nl))
        print('%s->back' % (len(nameLi),))
        return nameLi
    else:
        return []

def printAMenu(df=None):
    nameLi = None
    back = 0
    while True:
        print('1. print all tables')
        print('2. print recent two days change more than 10% tables')
        print('3. generate table data for today')
        print('4. exit program')
        cmd = input('Please input command number: ')
        if str(cmd) == '1' or str(cmd) == '2':
            nameLi = printList(df, int(cmd))
            back = 2
            break
        elif str(cmd) == '3':
            getTableRows()
        elif str(cmd) == '4':
            print('byebye')
            sys.exit(0)
        else:
            print('not a valid number')
            continue
    return {'value':nameLi, 'back':back}

def printBMenu(nameLi=None):
    tabNM = None
    back = 0
    while True:
        nmStr = input('Please input table number: ')
        try:
            no = int(nmStr)
        except:
            print('not a number')
            continue
        if no < 0:
            print('not a valid number')
            continue
        if no == len(nameLi):
            back = 1
            break
        try:
            tabNM = nameLi[no]
        except:
            print('not a valid number')
            continue
        if tabNM is not None:
            break
    return {'value':tabNM, 'back':back}

if __name__ == '__main__':
    li = os.listdir('./tablecount/')
    li.sort()
    shortLi = li[-15:]
    dfli = list(map(getDF, shortLi))
    ndf = reduce(combineDF, dfli)
    ndf1 = ndf.fillna(0).copy()
    ndf2 = ndf1.set_index(['tabnm']).copy()
    returnA = printAMenu(df=ndf2)
    while True:
        if returnA['back'] == 2:
            returnB = printBMenu(nameLi=returnA['value'])
            if returnB['back'] == 1:
                returnA = printAMenu(df=ndf2)
                continue
            else:
                generateImg(returnB['value'], ndf2.loc[returnB['value']])
                returnA = printAMenu(df=ndf2)
                #returnA['back'] = 1
        else:
            print('byebye')
            sys.exit(0)    