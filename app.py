import json

from flask import Flask

from Extractor import Extractor

app = Flask(__name__)

extractObj = Extractor('data.csv',6)
@app.route('/')
def hello_world():  # put application's code here
    return extractObj.extract()
@app.route('/j1')
def hello_world1():
    return extractObj.extract1()
@app.route('/j2')
def hello_world2():
    return extractObj.extract2()
if __name__ == '__main__':
    app.run()
