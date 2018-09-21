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

def run_dns_checks(lookup_result, result_type):
    if result_type is 'MX' and isinstance(lookup_result, list):
        #If type is MX then lookup_result is a list,
        #so we need to make a loop
        problem_detected = ''
        remote_provider = ''
        active_lowest_mx = ''
        active_lowest_mx_provider = ''

        lowest_ttl = min([x[0] for x in lookup_result])

        for item in lookup_result:
            ttl_str = item[0]
            mx_str = item[1]

            if lowest_ttl == ttl_str:
                # Found the lowest TTL, set it to a new variable
                active_lowest_mx = mx_str

            if 'protection.outlook.com' in mx_str:
                remote_provider = True
            elif 'google.com' in mx_str:
                remote_provider = True
            else:
                pass

        if 'protection.outlook.com' in active_lowest_mx:
            remote_provider_active = True
        elif 'google.com' in active_lowest_mx:
            remote_provider_active = True
        else:
            remote_provider_active = False


        if remote_provider_active == True and remote_provider == True:
            problem_detected = False
        else:
            problem_detected = True
    else:
        print('Type of lookup_result was not a list.')

    return problem_detected








