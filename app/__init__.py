from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import os



SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def index():
    ''' Default Route / Endpoint Users will hit '''
    data = [] # need to populate data else where
    return render_template('index.html',gearset=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)