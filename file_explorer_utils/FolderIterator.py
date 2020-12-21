import os


class FolderIterator:
    def __init__(self, filetypes=()):
        if filetypes:
            self.filetypes = tuple([filetype.lower() for filetype in filetypes])

    def on_folder(self, path, name):
        pass

    def on_file(self, path, name):
        pass

    def on_filetype(self, path, name, ext):
        pass

    def iterate(self, path):
        for root, dirs, files in os.walk(path):
            for name in files:
                self.on_file(root, name)
                ext = os.path.splitext(name)[-1].lower()
                if ext in self.filetypes:
                    self.on_filetype(root, name, ext)
            for name in dirs:
                self.on_folder(root, name)
