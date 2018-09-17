import dns.resolver
from geolite2 import geolite2

def dig_record(lookup_domain, type):
    resolver = dns.resolver.Resolver()
    try:
        query = resolver.query(lookup_domain, type)
    except:
        query = 'null'
    
    answer_list = []
    if query == 'null':
        answer = 'null'
    else:
        for item in query:
            answer_string = ''
            result_string = ''.join([str(item), answer_string])

            if type == 'MX':
                ttl, mx = result_string.split(' ')
                append_tuple = [ttl, mx]
                answer_list.append(append_tuple)
            else:
                answer_list.append(result_string)

        answer = answer_list
    return answer

def dig_ptr(lookup_domain):
    resolver = dns.resolver.Resolver()
    try:
        query = resolver.query(lookup_domain, 'A')
    except:
        query = 'null'

    answer_list = []

    print(query)
    
    if query == 'null':
        answer = 'null'
    else:
        for item in query:
            answer_string = ''
            result_string = ''.join([str(item), answer_string])
            
            print(result_string)
            #reverse_lookup = dns.reversename.from_address(item)
            #answer_list.append(reverse_lookup)

        #answer = answer_list

    return 'null'

def whois_ip(ip):
    reader = geolite2.reader()
    answer = reader.get(ip)
    geolite2.close()

    return answer


def whois_ip_name(ip):
    reader = geolite2.reader()
    lookup = reader.get(ip)
    geolite2.close()

    results = lookup.lookup_rdap(depth=1)
    answer = results.get("network", {}).get("name", {})
    
    return answer








