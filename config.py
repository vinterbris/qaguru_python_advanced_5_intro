class Server:
    def __init__(self, env):
        self.reqres = {
            'dev': '',
            'beta': '',
            'rc': 'http://localhost:8000/api'
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