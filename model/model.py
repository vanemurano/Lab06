from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getAllYears(self):
        return DAO.getAllYears()

    def getAllBrands(self):
        return DAO.getAllBrands()

    def getAllRetailers(self):
        return DAO.getAllRetailers()

    def getFilteredSales(self, anno, brand, codice):
        if anno=="Nessun filtro":
            anno=None
        if brand=="Nessun filtro":
            brand=None
        if codice=="Nessun filtro":
            codice=None
        #passa None se non c'è filtro in modo da nno crashare la query sql dopo
        return DAO.getFilteredSales(anno, brand, codice)