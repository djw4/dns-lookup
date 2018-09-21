from flask import Flask, render_template, request, redirect, url_for
from geolite2 import geolite2
from ipwhois import IPWhois
from pprint import pprint
import os, json, requests, urllib3, zlib, dns.resolver
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
    result_A_all = []
    
    if request.method == 'POST':
        domain          = request.form['domain']

        try:
            result_A = my_functions.dig_record(domain, 'A')
        except:
            result_A = None

        #result_A        = my_functions.dig_record(domain, 'A')
        result_NS       = my_functions.dig_record(domain, 'NS')
        result_TXT      = my_functions.dig_record(domain, 'TXT')
        result_MX       = my_functions.dig_record(domain, 'MX')
        
        if result_A is not 'null':
            for item in result_A:
                output_dict = {}
                ip_location     = my_functions.whois_ip(item)
                if item is not 'null':
                    result_A_IP_country = ip_location.get("country", {}).get("names", {}).get("en", {})
                
                w = IPWhois(item)
                results = w.lookup_rdap(depth=1)
                result_A_IP_name    = results.get("network", {}).get("name", {})
                result_A_IP_asn     = results.get("asn", {})
                
                output_dict["ip"]           = item
                output_dict["ip_name"]      = result_A_IP_name
                output_dict["ip_country"]   = result_A_IP_country
                output_dict["ip_asn"]       = result_A_IP_asn
                result_A_all.append(output_dict)
            
            check_result_MX = my_functions.run_dns_checks(result_MX, 'MX')

            return render_template('lookup.html', 
                domain = domain,
                return_A_all = result_A_all,
                return_MX = result_MX,
                return_NS = result_NS,
                return_TXT = result_TXT,
                return_problem_MX = check_result_MX)

        else:
            return render_template('nxdomain.html', domain = domain)

    else:
        domain = 'null'
        return redirect(url_for('index'))


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