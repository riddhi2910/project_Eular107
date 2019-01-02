import unittest
import time

from algorithm import Kruskal


class test_algorithm(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.6f" % (self.id(), t))

    def test_a_Kruskal(self):
        print("Test against network file provided by Eular ")
        with open("network_file.txt", "rb") as data:
            y = Kruskal(data)
            print("Actual Answer=", y, "Expected Answer=", 259679)
            self.assertEqual(y, 259679)

    def test_b_Kruskal(self):
        print('-------------------------------------------------------------------------------------')
        print("Testing on implemented Kruskal Algorithm using testunit framework")
        print('-------------------------------------------------------------------------------------')
        print("Test Case 1 ---> against graph in TestCase1.txt")

        with open("TestCase1.txt", "rb") as data:
            y = Kruskal(data)
            print("Actual Answer=", y, "Expected Answer=", 113)
            self.assertEqual(y, 113)

        print('-------------------------------------------------------------------------------------')
        print("Test Case 2 ---> against graph in TestCase2.txt")

        with open("TestCase2.txt", "rb") as data:
            y = Kruskal(data)
            print("Actual Answer=", y, "Expected Answer=", 59)
            self.assertEqual(y, 59)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_algorithm)
    unittest.TextTestRunner(verbosity=0).run(suite)
