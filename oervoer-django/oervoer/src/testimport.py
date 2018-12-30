import pprint

from wizard.importoervoer import ImportOrders, Credentials, ImportProds, ImportSmaak, ImportVlees

imp = ImportOrders(Credentials.user, Credentials.pw)
if imp.connect():
    savecur = imp.get_cur()
imp.importtable()

imp = ImportProds(Credentials.user, Credentials.pw, savecur)
pprint.pprint(imp.importtable())

imp = ImportSmaak(Credentials.user, Credentials.pw, savecur)
imp.importtable()

imp = ImportVlees(Credentials.user, Credentials.pw, savecur)
imp.importtable()




