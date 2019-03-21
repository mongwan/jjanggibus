from flask import Flask, render_template
import re
from parser import parse

app = Flask(__name__)

electric_bus_list = (
    '6442', '6443', '1664', '1824', '3744',
    '3768', '5007', '9411', '1902', '1905',
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
