#!/usr/bin/env python

from tornado import websocket
import tornado.ioloop
from tornado.ioloop import PeriodicCallback

# Python 3.5.2
filename = "sunshine.ulaw"
#filename = "sample2.ulaw"

# 800 samples == 100ms, if you change this to 1600 then change PeriodicCallback to 200, etc
g711 = []
with open(filename, "rb") as f:
    byte = f.read(800)
    while byte != b"":
        g711.append(byte)
        byte = f.read(800)
print("audio array has this many sets of samples: {}!".format(len(g711)))


class EchoWebSocket(websocket.WebSocketHandler):
    i = 0
    pc = None
    def open(self):
        print("Websocket Opened")
        self.pc = PeriodicCallback(self.sendaudio, 100)
        self.pc.start()

    def sendaudio(self):
      print("in sendaudio {}".format(self.i))
      self.write_message(g711[self.i],binary=1)
      self.i = (self.i+1) % len(g711)

    def on_message(self, message):
        self.write_message(u"You said: %s" % message)

    def on_close(self):
        print("Websocket closed")
        self.pc.stop()

application = tornado.web.Application([(r"/", EchoWebSocket),])

if __name__ == "__main__":
    application.listen(6120)
    tornado.ioloop.IOLoop.instance().start()

