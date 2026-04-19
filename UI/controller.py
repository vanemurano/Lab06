import flet as ft
from model import model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleTopVendite(self, e):
        self._view.txt_result.clean()
        vendite=self._model.getFilteredSales(self._view.dd_anno.value, self._view.dd_brand.value, self._view.dd_retailer.value)
        if self._view.dd_anno.value is None or self._view.dd_brand.value is None or self._view.dd_retailer.value is None:
            self._view.create_alert("Attenzione! Inserire tutti i filtri")
        stop=min(len(vendite), 5)
        if stop==0:
            self._view.txt_result.controls.append(
                ft.Text("Non ci sono vendite che corrispondono ai filtri selezionati",
                        color="blue")
            )
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"Ecco le prime {stop} vendite che corrispondono ai filtri selezionati, in ordine di ricavo:"))
        i=0
        while i<stop:
            self._view.txt_result.controls.append(
                ft.Text(f"{vendite[i]}")
            )
            i+=1
        self._view.update_page()

    def handleAnalisiVendite(self, e):
        pass

    def fillddAnno(self):
        for anno in self._model.getAllYears():
            self._view.dd_anno.options.append(
                ft.dropdown.Option(
                    key=anno,
                    text=anno))

    def fillddBrand(self):
        brands=self._model.getAllBrands()
        brands.sort()
        for brand in brands:
            self._view.dd_brand.options.append(
                ft.dropdown.Option(
                    key=brand,
                    text=brand))

    def fillddRetailer(self):
        retailers=self._model.getAllRetailers()
        retailers.sort(key=lambda x:x.retailer_name)
        for ret in retailers:
            self._view.dd_retailer.options.append(
                ft.dropdown.Option(
                    key=ret.retailer_code,
                    text=ret.retailer_name,
                    data=ret,
                    on_click=self.read_retailer #handler per leggere l'oggetto selezionato
                )
            )

    def read_retailer(self, e):
        self._retailer=e.control.data #cioè l'oggetto selezionato dall'esterno