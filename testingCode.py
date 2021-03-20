import unittest
from main import cal
import csv

class TestAdd(unittest.TestCase):
    '''Testing the calculator'''

    def test_add(self):
        '''Testing add menthod'''
        filePath = 'testCases/Unit Test Addition.csv'
        val1 = []
        val2 = []
        res = []
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    val1.append(float(row[0]))
                    val2.append(float(row[1]))
                    res.append(float(row[2]))
                line_count += 1

        calculator = cal("Addition Calculator Testing")
        passed = 0
        failed = 0
        for i in range(0,len(val1)):
            try:
                self.assertEqual(calculator.add(val1[i], val2[i]), res[i])
                passed +=1
            except Exception:
                failed+=1;
        print("Addition test-report : Passed:"+str(passed)+"   Failed:"+str(failed))

    def test_subtract(self):
        '''Testing subtract menthod'''
        filePath = 'testCases/Unit Test Subtraction.csv'
        val1 = []
        val2 = []
        res = []
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    val1.append(float(row[0]))
                    val2.append(float(row[1]))
                    res.append(float(row[2]))
                line_count += 1

        calculator = cal("Subtraction Calculator Testing")
        passed = 0
        failed = 0
        for i in range(0, len(val1)):
            try:
                self.assertEqual(calculator.subtract(val1[i], val2[i]), res[i])
                passed += 1
            except Exception:
                failed += 1;
        print("Subtraction test-report : Passed:" + str(passed) + "   Failed:" + str(failed))

if __name__ == '__main__':
    unittest.main(verbosity=2)