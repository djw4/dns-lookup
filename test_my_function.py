import my_functions
import pytest

def test_dig_record_a():
  domain = "dns.google"
  expected_result = ['8.8.4.4', '8.8.8.8']
  result = my_functions.dig_record('dns.google', 'A')
  assert result[0] in expected_result
  assert result[1] in expected_result

def test_dig_record_ns():
  domain = "dns.google"
  expected_result = [ 'ns3.zdns.google.', 'ns4.zdns.google.', 'ns1.zdns.google.', 'ns2.zdns.google.' ]
  result = my_functions.dig_record('dns.google', 'NS')
  assert result[0] in expected_result
  assert result[1] in expected_result