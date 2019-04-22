from collections import Iterable


class ClassMate(object):
    def __init__(self):
        self.name = list()

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        return ClassIter(self)


class ClassIter(object):
    def __init__(self, obj):
        self.obj = obj
        self.num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.obj.name):
            ret = self.obj.name[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration


san = ClassMate()
san.add("fhq")
san.add("luwei")
for temp in san:
    print(temp)