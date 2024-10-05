import Model.model
import wx

class AlbumPresenter(object):
    '''
    This is the object that takes care of the logic of your application.
    It also creates a "higher level language" in which you express what happens 
    inside your application.
    '''
    def __init__(self, albums, view):
        self.albums = albums
        self.view = view
        self.isListening = True
        self.order = 1
        self.initView()
        self.initBindings()
        view.start()
        
    def initBindings(self):
        self.view.albums.Bind(wx.EVT_LISTBOX, self.OnReloadNeeded)
        self.view.title.Bind(wx.EVT_TEXT, self.OnDataFieldUpdated)
        self.view.artist.Bind(wx.EVT_TEXT, self.OnDataFieldUpdated)
        self.view.composer.Bind(wx.EVT_TEXT, self.OnDataFieldUpdated)
        self.view.classical.Bind(wx.EVT_CHECKBOX, self.OnDataFieldUpdated)
        self.view.apply.Bind(wx.EVT_BUTTON, self.OnApply)
        self.view.cancel.Bind(wx.EVT_BUTTON, self.OnReloadNeeded)

    def initView(self):
        '''
        Upon first start, load the albums, set the selection on the first album and update the view.
        '''
        self.view.setAlbums(self.albums)
        self.view.setSelectedAlbum(0)
        self.loadViewFromModel()
    
    def OnReloadNeeded(self, evt):
        self.loadViewFromModel()

    def loadViewFromModel(self):
        '''
        1. guard against recursive call caused by events generated uppon loading of the data
        2. update the view data with the information from the model
        '''
        if self.isListening:
            self.isListening = False
            self.refreshAlbumList()
            self.view.setTitle(self.selectedAlbum.title)
            self.updateWindowTitle()
            self.view.setArtist(self.selectedAlbum.artist)
            self.view.setClassical(self.selectedAlbum.isClassical)
            if self.selectedAlbum.isClassical:
                self.view.setComposer(self.selectedAlbum.composer)
            else:
                self.view.setComposer("")
            if self.order == -1:
                self.view.setOrderLabel("A->Z")
            else:
                self.view.setOrderLabel("Z->A")
            self.view.setComposerEnabled(self.selectedAlbum.isClassical)
            self.enableApplyAndCancel(False)
            self.isListening = True
            
    def refreshAlbumList(self):
        '''
        1. save the selection
        2. sort the list
        3. update the list
        4. restore the selection
        '''
        currentAlbum = self.view.getSelectedAlbum()
        self.selectedAlbum = self.albums[currentAlbum]
        self.view.setAlbums(self.albums)
        self.view.setSelectedAlbum(self.albums.index(self.selectedAlbum))
        
    def updateWindowTitle(self):
        self.view.setWindowTitle("Album: " + self.view.getTitle())
        
    def enableApplyAndCancel(self, enabled):
        self.view.setApplyEnabled(enabled)
        self.view.setCancelEnabled(enabled)
        
    def toggleOrder(self):
        self.order = -1*self.order
        self.loadViewFromModel()
        
    def addNewAlbum(self):
        newAlbum = Model.model.Album("Unknown Artist", "New Album Title")
        self.albums.append(newAlbum)
        self.view.setAlbums(self.albums)
        self.view.setSelectedAlbum(self.albums.index(newAlbum))
        self.loadViewFromModel()

    def OnApply(self, evt):
        self.updateModel()

    def updateModel(self):
        '''
        Saves the data from the view in the model
        Disable the Apply/Cancel buttons and resync the view
        '''
        self.selectedAlbum.title = self.view.getTitle()
        self.selectedAlbum.artist = self.view.getArtist()
        self.selectedAlbum.isClassical = self.view.isClassical()
        if self.view.isClassical:
            self.selectedAlbum.composer = self.view.getComposer()
        else:
            self.selectedAlbum.composer = None
        self.enableApplyAndCancel(False)
        self.loadViewFromModel()
        

    def OnDataFieldUpdated(self, evt):
        self.dataFieldUpdated()

    def dataFieldUpdated(self):
        '''
        Upon a change in the view, enables the Apply/Cancel buttons and the composer field
        Since the Album title might have been changed we also update the title of the frame
        Optimisation: If the data is updated by the loadViewFromModel ignore the call
        '''
        if self.isListening:
            self.enableApplyAndCancel(True)
            self.view.setComposerEnabled(self.view.isClassical())
            self.updateWindowTitle()