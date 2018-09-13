import dns.resolver

def dig_A(lookup_domain):
    resolver = dns.resolver.Resolver()
    query = resolver.query(lookup_domain, 'A')
    
    answer_A_list = []
    for item in query:
        answer_A = ''
        result_string_A = ''.join([str(item), answer_A])

        answer_A_list.append(result_string_A)

    answer = answer_A_list
    return answer

def dig_MX(lookup_domain):  
    resolver = dns.resolver.Resolver()
    query = resolver.query(lookup_domain, 'MX')

    answer_MX_list = []
    for item in query:
        answer_MX = ''
        result_string_MX = ''.join([str(item), answer_MX])

        ttl, mx = result_string_MX.split(' ')
        append_tuple = [ttl, mx]
        
        answer_MX_list.append(append_tuple)

    answer = answer_MX_list
    return answer

def dig_NS(lookup_domain):
    resolver = dns.resolver.Resolver()
    query = resolver.query(lookup_domain, 'NS')
    
    answer_NS_list = []
    for item in query:
        answer_NS = ''
        result_string_NS = ''.join([str(item), answer_NS])
        answer_NS_list.append(result_string_NS)
        
    answer = answer_NS_list
    return answer


def dig_TXT(lookup_domain):
    resolver = dns.resolver.Resolver()
    query = resolver.query(lookup_domain, 'TXT')
    
    answer_TXT_list = []
    for item in query:
        answer_TXT = ''
        result_string_TXT = ''.join([str(item), answer_TXT])
        answer_TXT_list.append(result_string_TXT)
        
    answer = answer_TXT_list
    return answer