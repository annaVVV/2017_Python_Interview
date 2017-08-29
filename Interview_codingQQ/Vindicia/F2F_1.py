# Implement method to verify if IP4 address is valid

import unittest, re

def validate_ip4_address(address):
    #print 'add:',address
    ppp = "^([0]|[1-9]\d?|[1]\d?\d?|2[1-4]\d|25[0-5])(\.([1-9]\d?|[1]\d?\d?|2[1-4]\d|25[0-5])){3}"
    match = re.search(ppp, address)
    if match:
        #print  match.group(), True
        return 1
    else:
        #print address, False
        return 0

class DataTestCase(unittest.TestCase):
    def __init__(self, number):
        unittest.TestCase.__init__(self, methodName='test_ip4_address')
        self.number = number

    def test_ip4_address(self):
        #print self.number[0], self.number[1]
        self.assertEqual(validate_ip4_address(self.number[0]), self.number[1])

    def shortDescription(self):
        # We need to distinguish between instances of this test case.
        return 'DataTestCase for IP address:', self.number[0], 'Expected result', self.number[1]

def get_test_data_suite():
    data = [('0.1.1.1', 1),('255.255.255.255', 1),('10.25.30.99', 1),('0.9.9.9', 1),('1.1.1.1', 1),
            ('9.1.1.1', 1),('100.100.100.100', 1),('255.1.1.1', 1),('0.25.254.1', 1),('0.254.254.1', 1),
            ('-1.101.222.234', 0),('122.0.111.123', 0),('256.123.155.10', 0),('0.001.255.1', 0),('00.19.11.111', 0),
            ('122.0.111.123', 0),('a.1.1.1', 0),('100..100.100', 0),('255.1.1', 0),('', 0)]
    print 'data:',data
    return unittest.TestSuite([DataTestCase(n) for n in data])

if __name__ == '__main__':
    testRunner = unittest.TextTestRunner()
    testRunner.run(get_test_data_suite())
    validate_ip4_address('0.1.1.1')


# Unix commands: sed, awk
#  remove empty lines from file 

# SQL find second max salary and employee ID
