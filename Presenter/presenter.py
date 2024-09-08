from Model.model import Model
from View.view import View

class Presenter:
    def __init__(self):
        self.model = Model()
        self.view = View(None, title="Einfaches wxPython Beispiel", size=(600,600))
        self.view.presenter = self
        self.view.Show()

    def on_button_click(self):
        self.model.add_item("Neues Element")
        self.update_view()

    def update_view(self):
        # Aktualisiere die View basierend auf den Daten im Model
        pass