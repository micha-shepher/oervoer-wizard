

import pymysql
import re
import pprint

user = 'bvdheide_micha'
pw = 'lelijkgedrocht'

print 'connecting to {}@{}'.format(user, 'oervoer.com')
conn = pymysql.connect(host='oervoer.com', port=3306, user=user, passwd=pw, db='bvdheide_magento')
if conn:
    print 'connected'
   
cur = conn.cursor()

query ='''
SELECT DISTINCT v.value, v.option_id
FROM  eav_attribute_option AS o
INNER JOIN eav_attribute_option_value AS v ON o.option_id = v.option_id
WHERE o.attribute_id =184
ORDER BY v.value
'''
cur.execute(query)
query_results = cur.fetchall()
for r in query_results:
   print(r)
print len(query_results)


