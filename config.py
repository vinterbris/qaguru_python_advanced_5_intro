class Server:
    def __init__(self, env):
        self.reqres = {
            'dev': 'http://localhost:8000/api',
            'beta': '',
            'rc': ''
        }[env]
        self.microservice_1 = {
            'dev': '',
            'beta': '',
            'rc': ''
        }[env]
        self.microservice_2 = {
            'dev': '',
            'beta': '',
            'rc': ''
        }[env]