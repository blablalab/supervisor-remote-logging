#!/usr/bin/env python

import socketserver
import json


class SimpleTCPJsonServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

    @classmethod
    def instance(cls):
        return SimpleTCPJsonServer(("127.0.0.1", 22552), SimpleTCPJsonServerHandler)


class SimpleTCPJsonServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            data = json.loads(self.request.recv(1024).strip())
            # process the data, i.e. print(it:
            print(data)
            # send some 'ok' back
            self.request.sendall(json.dumps({"return": "ok"}))
        except Exception as e:
            print("Exception wile receiving message: ", e)


if __name__ == "__main__":
    server = SimpleTCPJsonServer.instance()

    print("Starting JSON TCP Server on 127.0.0.1:22552")
    server.serve_forever()
