import math

import data
import lab4
import unittest

from lab4 import distance, manhattan_distance, distance_all


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        # write a second test here
        input = [[2, 2], [5, 4]]
        result = lab4.first_element(input)
        expected = [2, 5]
        self.assertEqual(expected, result)




    # Part 2
    def test_x_coordinates(self):
        point1 = data.Point(3, 4)
        point2 = data.Point(5, 6)
        input = [point1,point2]
        result = lab4.x_coordinates(input)
        expected = [3,5]
        self.assertEqual(expected,result)

    # Part 3
    def test_are_in_positive_quadrant(self):
        point1 = data.Point(3, 4)
        point2 = data.Point(5, 6)
        input = [point1, point2]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[3,4],[5,6]]
        self.assertEqual(expected, result)


    # Part 4
    def test_distance(self):
        point1 = data.Point(3, 4)
        point2 = data.Point(5, 6)
        result = distance(point1,point2)
        expected = math.sqrt(8)
        self.assertEqual(expected, result)


    # Part 5
    def test_manhattan_distance(self):
        point1 = data.Point(3, 4)
        point2 = data.Point(5, 6)
        result = manhattan_distance(point1, point2)
        expected = 4
        self.assertEqual(expected, result)


    # Part 6
    def test_distance_all(self):
        inp = data.Point(4, 5)
        inp2 = data.Point(4, 8)
        List2 = [inp, inp2]
        result = distance_all(List2)
        expected = [math.sqrt(41),math.sqrt(80)]
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
