from flask import Flask, render_template, request, redirect, url_for
from geolite2 import geolite2
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
        domain          = request.form['domain']
        result_A        = my_functions.dig_record(domain, 'A')
        result_NS       = my_functions.dig_record(domain, 'NS')
        result_TXT      = my_functions.dig_record(domain, 'TXT')
        result_MX       = my_functions.dig_record(domain, 'MX')
        
        result_A_str    = " ".join(str(i) for i in result_A)
        ip_location     = my_functions.whois_ip(result_A_str)

        if ip_location != None:
            result_A_country = ip_location.get("country", {}).get("names", {}).get("en", {})
        else:
            result_A_country = 'Country Not Found'
        
        print(ip_location)

        return render_template('lookup.html', 
            domain = domain,
            return_A = result_A,
            return_MX = result_MX,
            return_NS = result_NS,
            return_TXT = result_TXT,
            return_A_country = result_A_country)
            #return_PTR = result_PTR)

@app.route("/whois/<ip>", methods=['GET'])
def whois(ip):
    ip_location = my_functions.whois_ip(ip)

    if ip_location != None:
        answer_country_en = ip_location.get("country", {}).get("names", {}).get("en", {})
    else:
        answer_country_en = 'Country Not Found'

    return render_template('whois.html',
        ip = ip,
        ip_country = answer_country_en)


if __name__ == '__main__':
    app.run()