from flask import Flask
import json
from parser import parse

app = Flask(__name__)


@app.route('/')
def main_page():
    t = 1
    bus_stop_list = []

    for i in parse():
        bus_stop_list.append(["busStop{}".format(t), i])
        t += 1

    return json.dumps(dict(bus_stop_list))


if __name__ == '__main__':
    app.run()
