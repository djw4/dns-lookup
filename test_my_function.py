import my_functions
import pytest

def test_dig_record_a():
  domain = "dns.google"
  lookup_type = 'A'
  expected_result = ['8.8.4.4', '8.8.8.8']
  result = my_functions.dig_record(domain, lookup_type)
  assert result[0] in expected_result
  assert result[1] in expected_result

def test_dig_record_ns():
  domain = "dns.google"
  lookup_type = 'NS'
  expected_result = [ 'ns3.zdns.google.', 'ns4.zdns.google.', 'ns1.zdns.google.', 'ns2.zdns.google.' ]
  result = my_functions.dig_record(domain, lookup_type)
  assert result[0] in expected_result
  assert result[1] in expected_result

def test_dig_record_mx():
  domain = "google.com"
  lookup_type = 'MX'
  expected_result = [ 'aspmx.l.google.com.', 'alt4.aspmx.l.google.com.', 'alt3.aspmx.l.google.com.', 'alt1.aspmx.l.google.com.', 'alt2.aspmx.l.google.com.' ]
  result = my_functions.dig_record(domain, lookup_type)
  assert result[0][1] in expected_result