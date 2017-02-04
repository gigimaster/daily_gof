
def singleton(cls):
    instances = dict()
    def _singleton(*args, **kv):
        if cls not in instances:
            instances[cls] = cls(*args, **kv)
        return instances[cls]
    return _singleton

@singleton
class Test(object):
    pass

if __name__ == '__main__':
    t1 = Test()
    t2 = Test()
    print id(t1)
    print id(t2)

