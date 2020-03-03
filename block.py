import zmq
import time
import sys


print(sys.argv)
ctx = zmq.Context.instance()
s = ctx.socket(zmq.PULL)
s.bind("tcp://0.0.0.0:{}".format(sys.argv[1]))
print("blocking port {}".format(sys.argv[1]))
while True:
    time.sleep(1)

