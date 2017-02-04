class singleton(object):
    pass


singleton = singleton()


if __name__ == '__main__':
    from singleton_import import singleton as s
    s1 = s


    from singleton_import import singleton as ss
    s2 = ss

    print id(s1)
    print id(s2)
