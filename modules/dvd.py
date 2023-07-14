from modules.library_item import LibraryItem

class Dvd(LibraryItem):

    def __init__(self, title, subject, upc, actors, directors, genre):
        LibraryItem.__init__(self, title, upc, subject)
        self.actors = actors, 
        self.directors = directors, 
        self.genre = genre