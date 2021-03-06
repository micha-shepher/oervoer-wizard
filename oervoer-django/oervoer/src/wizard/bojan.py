import pymysql

__author__ = 'mshepher'

class ImportOervoer(object):
    '''connect to the oervoer mysql server and import the stuff we need for the wizard.
    these are: orders, products, owners, pets, tastes and meattypes.
    owners and pets are gathered from the order table.'''
    def __init__(self, user='bvdheide_micha', pw='lelijkgedrocht', cur=None):
        self.user = user
        self.pw = pw
        self.cur = cur
        self.conn = None

        if not cur:
            self.connect()

    def connect(self):
        if self.conn:
            return True
        try:
            print 'connecting to {0}@{1}'.format(self.user, 'oervoer.com')
#            self.conn = pymysql.connect(host='oervoer.com', port=3306,
#                                        user=self.user, passwd=self.pw, db='bvdheide_magento')
            self.conn = pymysql.connect(host='46.19.33.91', port=3306,
                                        user=self.user, passwd=self.pw, db='bvdheide_magento')
            print 'connected'
        except pymysql.err.OperationalError:
            print 'no connection'
            return False

    def execute(self):
        try:
            self.cur = self.conn.cursor()

            self.cur.execute(self.query)
            return True
        except pymysql.err.OperationalError:
            print 'cannot obtain cursor'
            return False

    def get_cur(self):
        return self.cur

    def set_query(self, query):
        self.query = query

    def importtable(self):

        self.execute()
        query_results = self.cur.fetchall()
        return query_results


def readqty(prod):
    x=ImportOervoer()
    query = '''
    SELECT inv.qty FROM cataloginventory_stock_item AS inv
    WHERE {0} = inv.product_id
    '''.format(prod)

    x.set_query(query)
    x.execute()
    results = x.cur.fetchall()
    print results

def updateqty(prod, qty):
    x=ImportOervoer()
    query = '''
    UPDATE cataloginventory_stock_item AS inv
    SET inv.qty = inv.qty - {0},
    is_in_stock = 1
    WHERE {1} = inv.product_id
    '''.format(qty, prod)
    query_ = '''
    UPDATE cataloginventory_stock_status AS inv
    SET inv.qty = {0},
    inv.stock_status = 1
    WHERE {1} = inv.product_id
    '''.format(qty, prod)

    x.set_query(query)
    x.execute()
    results = x.cur.fetchall()
    print int(results[0][0])
    print type(results[0][0])
    x.conn.commit()


if __name__ == '__main__':
    # updateqty(236, -2)
    readqty(236)