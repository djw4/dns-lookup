from flask import Flask, render_template, request, redirect, url_for
import os, json, requests, urllib3, zlib
import dns.resolver
import my_functions

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/", methods=['GET'])
def index():
    domain = ''
    return render_template('index.html', domain = domain)

@app.route("/lookup", methods=['POST', 'GET'])
def lookup():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        domain = request.form['domain']
        result_A   = my_functions.dig_A(domain)
        result_MX  = my_functions.dig_MX(domain)
        result_NS  = my_functions.dig_NS(domain)
        result_TXT = my_functions.dig_TXT(domain)

        return render_template('lookup.html', 
            domain = domain,
            return_A = result_A,
            return_MX = result_MX,
            return_NS = result_NS,
            return_TXT = result_TXT)


if __name__ == '__main__':
    app.run()