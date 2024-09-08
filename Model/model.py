# model.py
class Model:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)
        # Benachrichtige den Presenter
        self.notify_observers()