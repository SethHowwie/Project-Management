#!usr/bin/python3
import os
import sys
script_path = os.path.dirname( os.path.realpath( __file__))
sys.path.insert(1, os.path,join( script_path, '..'))
sys.path.insert(1, os.path.join( script_path, '../demo_venv/lib/python3.5/site-packages' ) )
import unittest
import unittest.mock
import pylint.epylint
import hello

class CoinTossTester(unittest.TestCase):
    def test_heads(self):
        with unittest.mock.patch('random.randint', side_effect = [0]) as mock_randint:
            self.assertEqual(hello.coin_toss(), 'Heads' )
    def test_tails(self):
        with unittest.mock.patch('random.randint', side_effect = [0]) as mock_randint:
        self.assertEqaul(hello.coin_toss(), 'Tails')
if __name__ == '__main__':
    passes_checks = True
    runner = unittest.TextTestRunner()
    results = runner.run(unittest.makeSuite(CoinTossTester))
    if len(results.errors) > 0 or len(results.failures) > 0:
        print('Something went wrong so you should exit with non-zero')
        print(results.errors)
        print(results.failures)
        passes_checks = False
    (stdout, stderr) = pylint.epylint.py_run('hello.py --msg-template="{msg_id} ' +\
                                             'Line {line:3d}, comlumn {column:2d}: {msg}"', return_std=True )
    fault_codes = ['C0103' , 'C0301', 'E0104', 'C0303', 'C0121']
    

    for line in stdout.getvalue().lines():
        if len(line.split()) > 0 and line.split()[0] in fault_codes:
            passes_checks = False
            print("You messed up, here's how.")
            print(line)
    
    if not passes_checks:
        sys.exit(1)
    
        

