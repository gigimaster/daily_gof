
class Singleton(object):
    instance = None
    def __new__(self, *args, **kwargs):
        if not self.instance:
            self.instance = super(Singleton, self).__new__(self, *args, **kwargs)

        return self.instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1)==id(s2)
    print id(s1)
    print id(s2)
