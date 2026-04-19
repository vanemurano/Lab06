from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendite import Vendita


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears ():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query="""select distinct year (date) as year
                from go_daily_sales"""

        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(int(row["year"]))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getAllBrands ():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query="""select distinct product_brand 
                from go_products"""

        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(row["product_brand"])

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getAllRetailers ():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query="""select distinct retailer_code, retailer_name
                from go_retailers"""

        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(Retailer(**row)) #crea l'oggetto retailer dai campi selezionati

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getFilteredSalesYear(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select gds.retailer_code, gds.product_number, gds.date, (gds.unit_sale_price*gds.quantity) as ricavo 
                    from go_daily_sales gds, go_products gp, go_retailers gr 
                    where gds.product_number=gp.product_number 
                            and	gds.retailer_code=gr.retailer_code 
                            and year(gds.date)=coalesce(%s, year(gds.date))
                    order by ricavo desc"""

        cursor.execute(query, (anno,))

        res = []
        for row in cursor:
            res.append(Vendita(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getFilteredSales(anno, brand, codice):
    #ritorna le vendite con il ricavo più alto in base ai filtri selezionati
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select gds.retailer_code, gds.product_number, gds.date, (gds.unit_sale_price*gds.quantity) as ricavo 
                        from go_daily_sales gds, go_products gp, go_retailers gr 
                        where gds.product_number=gp.product_number 
                                and	gds.retailer_code=gr.retailer_code 
                                and gds.retailer_code=coalesce(%s, gds.retailer_code) 
                                and gp.product_brand=coalesce(%s, gp.product_brand)
                                and year(gds.date)=coalesce(%s, year(gds.date))
                        order by ricavo desc"""
        #con il comando coalesce, se passo come parametro un None l'istruzione viene semplicemente ignorata e si passa avanti

        cursor.execute(query, (codice, brand, anno,))

        res = []
        for row in cursor:
            res.append(Vendita(**row))

        cursor.close()
        cnx.close()

        return res