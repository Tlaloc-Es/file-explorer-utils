from IteratorFlow import IteratorFlow
from folderUtils import get_extension
import smbclient
import os
import queue


class SmbIterator(IteratorFlow):
    def __init__(self, server, share, username, password, domain, filetypes=()):
        self.server = server
        self.share = share
        self.username = username
        self.password = password
        self.domain = domain
        self.smb = smbclient.SambaClient(
            server=server, share=share, username=username, password=password, domain=domain)
        self.filetypes = []
        if filetypes:
            self.filetypes = tuple([filetype.lower()
                                    for filetype in filetypes])

    def iterateSmb(self, path):
        q = queue.Queue()
        q.put(path)
        while not q.empty():
            folder = q.get()
            try:
                for i in self.smb.lsdir(folder):
                    name = i[0]
                    if 'D' in i[1]:
                        q.put(os.path.join(folder, name))
                        self.on_folder(folder, name)
                    else:
                        self.on_file(folder, name)
                        ext = get_extension(name)
                        if ext in self.filetypes:
                            self.on_filetype(folder, name, ext)
            except Exception as e:
                self.on_path_error(folder, e)
