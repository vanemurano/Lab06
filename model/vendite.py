from dataclasses import dataclass


@dataclass
class Vendita:
    retailer_code:int
    product_number:int
    date:str
    ricavo:float

    def __eq__(self, other):
        return self.retailer_code==other.retailer_code and self.product_number==other.product_number and self.date==other.date

    def __hash__(self):
        return hash(self.retailer_code), hash(self.product_number), hash(self.date)

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Product: {self.product_number}"
