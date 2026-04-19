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
        return DAO.getFilteredSales(anno, brand, codice)