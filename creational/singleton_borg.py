class Borg(object):
    _dict = {}
    def __init__(self):
        self.__dict__ = self._dict

if __name__ == '__main__':
    s1 = Borg()
    s2 = Borg()
    s1.a = 100
    print id(s1)
    print id(s2)
    print s1.a
    print s2.a
