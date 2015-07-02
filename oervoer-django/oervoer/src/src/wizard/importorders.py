#!/usr/bin/env python
'''expand this to import all pets, by importing all orders and parsing the 
product_options to obtain the owner and pet attributes. Then feed the database with
the list of owners and pets (related).
''' 

import csv

import pymysql
import phpserialize
import re
import string
#import pprint



#user = 'bvdheide_oervoer'
#pw = '{0%M5s7Xs3gL(,_N'
user = 'bvdheide_micha'
pw = 'lelijkgedrocht'
usercpanel = 'bvdheide'
pwcpanel= 'p1fN7k<cG;r/-5x'

def get_name_and_weight(options):
    name = 'niet bekend'
    weight = '10'
    pat = re.compile('(\d+\.{0,1}\d*)')

    for option in options.keys():
        
        if options[option]['label'].startswith('Wat is de naam'):
            name = options[option]['option_value']
        if options[option]['label'].startswith('Wat is het gewicht'):
            weight = options[option]['option_value']
            weight = weight.replace(',','.')
            m = re.search(pat, weight)
            if m:
                weight = m.group(0)
            
    return name, weight
 
def lengthreplace(matchobj):
    '''replace badly generated string length to fix PHP serialize bug.
    '''   
    a = matchobj.group(1)
    b = matchobj.group(2)
    if not int(a) == len(b):
        return 's:{}:"{}"'.format(len(b),b)
    else:
        return matchobj.group(0)
 
def correct_string_len(s):
    '''example: "s:17:bla bla bla bla bla b"
                 matches. group 1 is '17' and group 2 is "bla bla bla bla bla b" '''
    pat = re.compile(r's:(\d*?):"(.*?)"')
    return re.sub(pat, lengthreplace, s)
    
print 'connecting to {}@{}'.format(user, 'oervoer.com')
conn = pymysql.connect(host='oervoer.com', port=3306, user=user, passwd=pw, db='bvdheide_magento')
if conn:
    print 'connected'
   
cur = conn.cursor()

query ='''
SELECT sal.entity_id, sal.status, sal.customer_id, item.sku, item.product_id, item.weight, item.product_options
FROM  `sales_flat_order` AS sal
INNER JOIN sales_flat_order_item AS item
ON sal.entity_id=item.order_id
WHERE sal.status in ('processing','pending') AND item.product_id in (58,60,85,125,126,127,187,192,193,424,426,428)
'''
cur.execute(query)
query_results = cur.fetchall()
for r in query_results:
   print(r[:-1])
print len(query_results)

orderfile = file('orders.csv','w')
fieldnames=('owner','dier','gewicht','kilo pakket', 'soort pakket','hond/poes')
of = csv.DictWriter(orderfile, delimiter=',',fieldnames=fieldnames)
of.writerow({'owner':'owner', 'dier':'dier', 'gewicht':'gewicht','kilo pakket':'kilo pakket','soort pakket':'soort pakket','hond/poes':'HOND of KAT'})
for r in query_results:
    pakket = r[3]
    if pakket in (58,125,193,426):
        pak = 'PLUS'
    elif pakket in (85,126,187,428):
        pak = 'COMBI'
    else:
        pak = '100'
    if pakket in (58,60,85,187,192,193):
        kh = 'HOND'
    else:
        kh = 'KAT'
    
    s=filter(lambda x: x in string.printable, r[5])
    d = phpserialize.loads(correct_string_len(s))
#    pprint.pprint (d)
    name, weight = get_name_and_weight(d['options'])
    of.writerow({'owner':r[1], 'dier':name, 
                            'gewicht':weight,
                            'kilo pakket':r[4],'soort pakket':pak,'hond/poes':kh})

orderfile.close()

#print phpserialize.loads(query_results[0][5])
#with file('z','w') as f:
#    for r in query_results:
#        s=filter(lambda x: x in string.printable, r[5])
#        d = phpserialize.loads(correct_string_len(s))
#        pprint.pprint(d,f)
#        f.write('\n')



cur.close()
conn.close()
