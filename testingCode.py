import unittest
from main import cal
import csv

class ReadData:
    @staticmethod
    def readData3Col(filePath):
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
        return val1,val2,res

    @staticmethod
    def readData2Col(filePath):
        val1 = []
        res = []
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    val1.append(float(row[0]))
                    res.append(float(row[1]))
                line_count += 1
        return val1,res

class TestAdd(unittest.TestCase):
    '''Testing the calculator'''

    calculator = None

    @classmethod
    def setUpClass(cls):
        cls.calculator = cal("Testing Calculator")

    def test_calC_init(self):
        self.assertIsInstance(self.calculator,cal,"Calculator object is not correctly instantiated.")

    def test_add(self):
        '''Testing add menthod'''
        filePath = 'testCases/Unit Test Addition.csv'

        val1,val2,res = ReadData.readData3Col(filePath)

        passed = 0
        failed = 0
        for i in range(0,len(val1)):
            try:
                self.assertEqual(self.calculator.add(val1[i], val2[i]), res[i])
                passed +=1
            except Exception:
                print("Addition : "+str(self.calculator.multiply(val1[i], val2[i]))+"!="+str(res[i]))
                failed+=1
        print("Addition test-report : Passed:"+str(passed)+"   Failed:"+str(failed))

    def test_subtract(self):
        '''Testing subtract menthod'''
        filePath = 'testCases/Unit Test Subtraction.csv'

        val1,val2,res = ReadData.readData3Col(filePath)

        passed = 0
        failed = 0
        for i in range(0, len(val1)):
            try:
                self.assertEqual(self.calculator.subtract(val1[i], val2[i]), res[i])
                passed += 1
            except Exception:
                print("Subtraction : "+str(self.calculator.multiply(val1[i], val2[i]))+"!="+str(res[i]))
                failed += 1
        print("Subtraction test-report : Passed:" + str(passed) + "   Failed:" + str(failed))

    def test_divide(self):
        '''Testing Division menthod'''
        filePath = 'testCases/Unit Test Division.csv'

        val1,val2,res = ReadData.readData3Col(filePath)

        passed = 0
        failed = 0
        for i in range(0, len(val1)):
            l = len(str(res[i]).split('.')[1])
            try:
                self.assertEqual(("{:."+str(l)+"f}").format(round(self.calculator.divide(val2[i], val1[i]),l)), str(res[i]))
                passed += 1
            except Exception:
                print("Division : "+str(("{:."+str(l)+"f}").format(round(self.calculator.divide(val2[i], val1[i]),l))) +" != "+str(res[i]))
                failed += 1
        print("Division test-report : Passed:" + str(passed) + "   Failed:" + str(failed))

    def test_multiply(self):
        '''Testing multiplication menthod'''
        filePath = 'testCases/Unit Test Multiplication.csv'

        val1,val2,res = ReadData.readData3Col(filePath)

        passed = 0
        failed = 0
        for i in range(0, len(val1)):
            try:
                self.assertEqual(self.calculator.multiply(val1[i], val2[i]), res[i])
                passed += 1
            except Exception:
                print("Multiplication : "+str(self.calculator.multiply(val1[i], val2[i]))+"!="+str(res[i]))
                failed += 1
        print("Multiplication test-report : Passed:" + str(passed) + "   Failed:" + str(failed))

    def test_square(self):
        '''Testing Square menthod'''
        filePath = 'testCases/Unit Test Square.csv'

        val1,res = ReadData.readData2Col(filePath)

        passed = 0
        failed = 0
        for i in range(0, len(val1)):
            try:
                self.assertEqual(self.calculator.square(val1[i]), res[i])
                passed += 1
            except Exception:
                print("Square : "+str(self.calculator.multiply(val1[i]))+"!="+str(res[i]))
                failed += 1
        print("Square test-report : Passed:" + str(passed) + "   Failed:" + str(failed))


    def test_square_root(self):
        '''Testing Square Root menthod'''
        filePath = 'testCases/Unit Test Square Root.csv'

        val1, res = ReadData.readData2Col(filePath)

        passed = 0
        failed = 0
        for i in range(0, len(val1)):

            l = len(str(res[i]).split('.')[1])
            try:
                self.assertEqual(("{:." + str(l) + "f}").format(round(self.calculator.square_root(val1[i]), l)),
                                 str(res[i]))
                passed += 1
            except Exception:
                print("Square Root : " + str(
                    ("{:." + str(l) + "f}").format(round(self.calculator.square_root( val1[i]), l))) + " != " + str(
                    res[i]))
                failed += 1

        print("Square Root test-report : Passed:" + str(passed) + "   Failed:" + str(failed))


if __name__ == '__main__':
    unittest.main(verbosity=2)