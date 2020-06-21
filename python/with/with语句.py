class File(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("existing")
        self.f.close()


with File('out.txt', 'w') as f:
    print("writing")
    print(type(f))
    f.write("hello python")