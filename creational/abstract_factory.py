
class notification(object):
    def __init__(self):
        pass

    def send(self):
        pass

class email(notification):
    def __init__(self):
        pass

    def send(self):
        print 'send email'

class message(notification):
    def __init__(self):
        pass

    def send(self):
        print 'send sms'

class send_nothing(notification):
    def __init__(self):
        pass

    def send(self):
        print 'sleeping'



class checker(object):
    def __init__(self):
        pass

    def check(self):
        pass

class email_checker(checker):
    def __init__(self):
        pass

    def check(self):
        print 'check email ok'

class message_checker(checker):
    def __init__(self):
        pass

    def check(self):
        print 'check sms ok'

class nochecker(checker):
    def __init__(self):
        pass

    def check(self):
        print 'checker sleeping'


class factory(object):
    def __init__(self):
        pass

    def get(self):
        pass

    def getchecker(self):
        pass

class email_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return email()

    def getchecker(self):
        return email_checker()

class message_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return message()

    def getchecker(self):
        return message_checker()

class send_nothing_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return send_nothing()

    def getchecker(self):
        return nochecker()

if __name__ == '__main__':

    factory_inst = message_factory()
    sender = factory_inst.get()
    checker = factory_inst.getchecker()

    sender.send()
    checker.check()

