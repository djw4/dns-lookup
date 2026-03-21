import dns.resolver, os, requests
from ipwhois import IPWhois

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['1.1.1.1', '1.0.0.1']


def dig_record(lookup_domain, type):
    try:
        query = resolver.resolve(lookup_domain, type)
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
    try:
        query = resolver.resolve(lookup_domain, 'A')
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
    # ip-api.com free tier only supports HTTP (HTTPS requires a paid plan)
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success":
            return {"country": {"names": {"en": data.get("country", "")}}}
        return None
    except Exception:
        return None


def whois_ip_name(ip):
    obj = IPWhois(ip)
    results = obj.lookup_rdap(depth=1)
    return results['network']['name']

def run_dns_checks(lookup_result, result_type):
    if result_type == 'MX' and isinstance(lookup_result, list):
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








