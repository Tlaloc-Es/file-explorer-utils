from IteratorFlow import IteratorFlow
from folderUtils import get_extension
import os


class FolderIterator(IteratorFlow):
    def __init__(self, filetypes=()):
        self.filetypes = []
        if filetypes:
            self.filetypes = tuple([filetype.lower()
                                    for filetype in filetypes])

    def iterate(self, path):
        for root, dirs, files in os.walk(path):
            for name in files:
                self.on_file(root, name)
                ext = get_extension(name)
                if ext in self.filetypes:
                    self.on_filetype(root, name, ext)
            for name in dirs:
                self.on_folder(root, name)
