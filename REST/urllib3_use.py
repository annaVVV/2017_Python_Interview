import unittest
import urllib3
import requests

class SimpleTest(unittest.TestCase):

    def test(self):
        print "Test using urllib3"
        http = urllib3.PoolManager()
        self.r = http.request('GET', 'http://httpbin.org/robots.txt')
        print self.r.status
        print self.r.data
        #'User-agent: *\nDisallow: /deny\n'       self.failUnless(True)
        self.assertEqual(self.r.status, 200, 'Status is not OK')

    def testRest(self):
        print "Test using requests"
        self.r = requests.request('GET', 'http://httpbin.org/robots.txt')
        print self.r.status_code
        print self.r.content
        self.assertEqual(self.r.status_code, 200, 'Status is not OK')

if __name__ == '__main__':
    unittest.main()
    
# output:
# Test using urllib3
# 200
# User-agent: *
# Disallow: /deny
# 
# Test using requests
# 200
# User-agent: *
# Disallow: /deny
