import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_top = None
        self.btn_analizza = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        #PRIMO DROPDOWN
        self.dd_anno=ft.Dropdown(label="anno", width=300)
        self.dd_brand=ft.Dropdown(label="brand", width=300)
        self.dd_retailer=ft.Dropdown(label="retailer", expand=True) #prende tutto lo spazio rimasto sulla riga

        row1=ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer])

        self._controller.fillddAnno()
        self._controller.fillddBrand()
        self._controller.fillddRetailer()

        self._page.controls.append(row1)

        #ROW2 with buttons
        self.btn_top=ft.ElevatedButton(text="Top vendite",
                                       width=200,
                                       on_click=self._controller.handleTopVendite)
        self.btn_analisi=ft.ElevatedButton(text="Analizza vendite",
                                           on_click=self._controller.handleAnalisiVendite,
                                           width=200)

        row2=ft.Row([self.btn_top, self.btn_analisi],
                    ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
