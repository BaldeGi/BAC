#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import Divisor as student
import CorrDivisor as correct

class test_divisor(unittest.TestCase):
    def test_divisor1(self):
        args=[24,14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
        
    def test_divisorr2(self):
        args=[14,14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    
    def test_divisor3(self):
        args=[-24,14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
        
    def test_divisor4(self):
        args=[-14,-4]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_divisor5(self):
        args=[14,24]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_divisor6(self):
        args=[14,-24]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_divisor7(self):
        args=[-4,-14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
if __name__=='__main__':
    unittest.main()

    
    
    