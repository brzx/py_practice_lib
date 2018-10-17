#!/usr/bin/python

''' connect to a sqlite3 database, if it is not exists, then create it.
'''

import sqlite3
import beatbox

conn = sqlite3.connect('sfdc.db')
print "Opened database successfully";

try:
    conn.execute('drop table sobjects')
except sqlite3.OperationalError as e:
    print(e.args[0])
else:
    print "Table droped successfully";

conn.execute('''create table sobjects
                            (id int primary key not null,
                             name text not null,
                             label text not null,
                             labelPlural text,
                             activateable text);''')
print "Table created successfully";

try:
    conn.execute('drop table sfields')
except sqlite3.OperationalError as e:
    print(e.args[0])
else:
    print "Table droped successfully";

conn.execute('''create table sfields
                            (sobject_id int not null,
                             sobject_name text not null,
                             sobject_label text not null,
                             field_name text,
                             field_type text,
                             field_length int,
                             field_precision int,
                             field_referenceto text,
                             field_scale int);''')
print "Table created successfully";

svc = beatbox.PythonClient()
beatbox.gzipRequest = False
svc.serverUrl = svc.serverUrl.replace('login.', 'test.')
login = svc.login('sfdc username', 'pw')
dg = svc.describeGlobal()
print(dg.keys())
input = raw_input('continue running? ')
if input == 'yes':
    object_list = dg['sobjects']
    for i, ol in enumerate(object_list):
        sql = "insert into sobjects (id, name, label, labelPlural, activateable) values (%d, '%s', '%s', '%s', '%s')" \
                % (i+1, ol.name, ol.label, ol.labelPlural, ol.activateable)
        conn.execute(sql)
        pass
    conn.commit()
    print "Records created successfully";

    cursor = conn.execute("select id, name from sobjects")
    for row in cursor:
        #print "id = ", row[0]
        dr = svc.describeSObjects(row[1]) # dr is a list, have only one value
        for f in dr[0].fields.keys():
            if dr[0].fields[f].type == 'reference' and len(dr[0].fields[f].referenceTo)>1:
                referenceTo = dr[0].fields[f].referenceTo[0]
            else:
                referenceTo = ''
            sql = "insert into sfields (sobject_id, sobject_name, sobject_label, field_name, field_type, field_length, \
                     field_precision, field_referenceto, field_scale) values (%d, '%s', '%s', '%s', '%s', %d, %d, '%s', %d)" \
                     % (row[0], dr[0].name, dr[0].label, dr[0].fields[f].name, dr[0].fields[f].type, dr[0].fields[f].length, \
                     dr[0].fields[f].precision, referenceTo, dr[0].fields[f].scale)
            #print(sql)
            conn.execute(sql)
            pass
        conn.commit()
        pass

    print "Records created successfully";

conn.close()
