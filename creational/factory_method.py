
class notification(object):
    def __init__(self):
        pass

    def send(self):
        pass

class factory(object):
    def __init__(self):
        pass

    def get(self):
        pass

"""blabla

"""

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


class email(notification):
    def __init__(self):
        pass

    def send(self):
        print 'send email'

class email_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return email()

class message_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return message()

class send_nothing_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return send_nothing()

class wechat(notification):
    def __init__(self):
        pass

    def send(self):
        print 'send wechat'

class wechat_factory(factory):
    def __init__(self):
        pass

    def get(self):
        return wechat()


if __name__ == '__main__':
    sender = email_factory().get()
    sender.send()

    sender = message_factory().get()
    sender.send()

    sender = send_nothing_factory().get()
    sender.send()

    sender = wechat_factory().get()
    sender.send()
