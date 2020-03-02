import zmq
import json


def produce(url):
    """Produce messages"""
    ctx = zmq.Context.instance()
    s = ctx.socket(zmq.PUSH)
    s.connect(url)
    print("Producing %s")
    s.send_string(json.dumps({"hello": "world"}))


run = 0
while True:
    print("pushing {}".format(run))
    produce("tcp://127.0.0.1:5556")
    run += 1
