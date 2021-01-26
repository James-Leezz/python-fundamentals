

import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        # 字节类型
        while 1:
            # 针对window系统
            try:
                print("等待信息")
                data = self.request.recv(1024)  # 阻塞
                # 针对linux
                if len(data) == 0:
                    break
                if data == b'exit':
                    break
                response = data + b'SB'
                self.request.send(response)
            except Exception as e:
                break

        self.request.close()


# 1 创建socket对象 2 self.socket.bind()  3 self.socket.listen(5)
server=socketserver.ForkingUDPServer(("127.0.0.1",8899),Myserver)

server.serve_forever()












