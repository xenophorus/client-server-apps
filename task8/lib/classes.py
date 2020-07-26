import json
import time


class Message:
    def __init__(self):
        self.action = 'message'
        self.from_user = 'user'
        self.to_user = 'all'
        self.time_date = time.asctime()
        self.message = ''

    def __repr__(self):
        return f'Message from {self.from_user} to {self.to_user},' \
               f'action: {self.action}, date: {self.time_date}\n' \
               f'message: {self.message}'

    @staticmethod
    def _jsoncode(msg, command):
        if command == 'dec':
            return json.loads(msg.decode('utf-8'))
        if command == 'enc':
            return json.dumps(msg.to_dict()).encode('utf-8')

    def _set_msg(self):
        self.message = input('Enter your message:\n')

    def create(self, action, from_user, to_user):
        self.action = action
        self.time_date = time.asctime()
        self.from_user = from_user
        self.to_user = to_user
        self._set_msg()
        return dict(action=self.action, time=self.time_date, to=self.to_user,
                    from_user=self.from_user, message=self.message)

    @staticmethod
    def decode(self, data):
        ddata = self._jsoncode(data, 'dec')
        self.action = ddata.get('action')
        self.time_date = ddata.get('time')
        self.to_user = ddata.get('to')
        self.from_user = ddata.get('from_user')
        self.message = ddata.get('message')
        return dict(action=self.action, time=self.time_date, to=self.to_user,
                    from_user=self.from_user, message=self.message)

    def encode(self):
        return self._jsoncode(self, 'enc')

    def values(self):
        return [self.action, self.time_date, self.from_user, self.to_user, self.message]

    def message_str(self):
        return self.message

    def to_dict(self):
        return dict(action=self.action, time=self.time_date, to=self.to_user,
                    from_user=self.from_user, message=self.message)
