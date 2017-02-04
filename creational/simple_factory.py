
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

class factory(object):
    def __init__(self):
        pass

    def get(self, type=None):
        inst = None
        if type == 'email':
            inst = email()
        elif type == 'message':
            inst = message()
        else:
            inst = send_nothing()
        return inst


if __name__ == '__main__':
    sender = factory().get('email')
    #sender = factory().get()
    sender = factory().get('message')



    sender.send()
    sender.send()
    sender.send()
    sender.send()
    sender.send()
    sender.send()


