

class BiDirDict(dict):

    def __getitem__(self, key):
        if key in self.values():
            for k, v in self.items():
                if v == key:
                    item = k
        else:
            item = super(BiDirDict, self).__getitem__(key)
        return item

    def __contains__(self, key):
        if key in self.values():
            return True
        return super(BiDirDict, self).__contains__(key)
