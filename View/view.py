import wx

class View(wx.Frame):
    def __init__(self, *args, **kw):
        super(View, self).__init__(*args, **kw)
        
        # Panel erstellen
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Beschriftung hinzufügen
        lbl = wx.StaticText(pnl, label="Hallo, Welt!")
        vbox.Add(lbl, flag=wx.CENTER | wx.TOP, border=10)

        # Schaltfläche hinzufügen
        btn = wx.Button(pnl, label="Klick mich")
        vbox.Add(btn, flag=wx.CENTER | wx.TOP, border=10)

        # Event-Bindung für die Schaltfläche
        btn.Bind(wx.EVT_BUTTON, self.on_button_click)
        pnl.SetSizer(vbox)

    def on_button_click(self, event):
        wx.MessageBox("Schaltfläche geklickt!", "Information", wx.OK | wx.ICON_INFORMATION)