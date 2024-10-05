class Album(object):
    '''
    Just a dumb object that incapsulates the information of the album
    '''
    def __init__(self, artist, title, isClassical=False, composer=None):
        self.artist = artist
        self.title = title
        self.isClassical = isClassical
        self.composer = composer

someAlbums = [
    ("Mike Oldfield", "The Songs of Distant Earth"),
    ("Loreena McKennitt", "The Visit"),
    ("Music Instructor", "Electric City"),
    ("Domingo, Plowright, Fassbaender, Zancanaro, Nesterenko", "Il Trovatore", True, "Giuseppe Verdi"),
    ("Riccardo Muti", "Rigoletto", True, "Giuseppe Verdi")
    ]

def GetDemoAlbums():
    '''Just transforms a list of tuples containing data into a list of Albums using list comprehension'''
    return [Album(*data) for data in someAlbums]