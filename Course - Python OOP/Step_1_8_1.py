# Условие задачи https://stepik.org/lesson/709885/step/1?unit=710450

class Server:

    ip = 1

    def __new__(cls, *args, **kwargs):
        cls.ip += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = Server.ip
        self.buffer = []
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        data = self.buffer[:]
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        del_server = self.servers.pop(server.ip, False)
        if del_server:
            server.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                server = self.servers[data.ip]
                server.buffer.append(data)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from, msg_lst_to)
