class User:
    def __init__(self, **kwargs):
        json = kwargs.pop('json', {})
        self._id = kwargs.pop('id   ', None)
        self._first_name = kwargs.pop('first_name', None)
        self._last_name = kwargs.pop('last_name', None)
        self._email = kwargs.pop('email', None)
        self._avatar = kwargs.pop('avatar', None)
        self._json = json if json else {
            "id": self._id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "email": self._email,
            "avatar": self._avatar
        }

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def json(self):
        return self._json

    @property
    def avatar(self):
        return self._avatar

class ResponseGetUser:
    def __init__(self, **kwargs):
        json = kwargs.pop('json')
        self._data = kwargs.pop('data', User().json)
        self._json = json if json else {
            'data': self._data
        }

    @property
    def json(self):
        return self.json()