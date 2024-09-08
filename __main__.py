import wx
from Presenter.presenter import Presenter

def main():
    # wx App erstellen
    app = wx.App(False)
    presenter = Presenter()
    app.MainLoop()

if __name__ == "__main__":
    main()
