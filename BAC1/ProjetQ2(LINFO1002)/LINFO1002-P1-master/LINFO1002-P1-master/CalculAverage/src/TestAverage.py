#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import CoorAverage as correct
import average as student

class TestAverage(unittest.TestCase):
    def test1_average(self):
        args = [10,5,6,14]
        rep = ("Votre fonction a retourné {} pour {} comme argument alors qu'elle devrait retourner {}.")
        try:
            student_ans = student.average(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans=correct.average(args)
        self.assertEqual(student_ans,correct_ans, rep.format(student_ans,args,correct_ans))
        
    def test3_average(self):
        args = []
        rep = ("Votre fonction a retourné {} pour {} comme argument alors qu'elle devrait retourner None")
        try:
            student_ans = student.average(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans=correct.average(args)
        self.assertEqual(student_ans,correct_ans, rep.format(student_ans,args,correct_ans))
        
    def test2_average(self):
        args = [-10,-5,-6,-14]
        rep = ("Votre fonction a retourné {} pour {} comme argument alors qu'elle devrait retourner {}")
        try:
            student_ans = student.average(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans=correct.average(args)
        self.assertEqual(student_ans,correct_ans, rep.format(student_ans,args,correct_ans))
if __name__=="__main__":
    unittest.main()

