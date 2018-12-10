from flask import Flask, render_template
import re
from parser import parse

app = Flask(__name__)

electric_bus_list = (
    '3744', '6443', '9411', '5007', '1902'
)


@app.route('/')
def main_page():
    bus_list = [(re.findall(r"\d+", i.findtext('plainNo'))[1], i.findtext('gpsY'), i.findtext('gpsX')) for i in parse()]
    return render_template('index.html',
                           bus_list=bus_list,
                           electric_bus_list=electric_bus_list
                           )


if __name__ == '__main__':
    app.run(debug=True)
