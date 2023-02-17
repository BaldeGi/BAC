#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import Divisor as student
import CorrDivisor as correct

class test_premier(unittest.TestCase):
    def test_premier1(self):
        args=[24,14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
        
    def test_premier2(self):
        args=[14,14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    
    def test_premier3(self):
        args=[-24,14]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
        
    def test_premier4(self):
        args=[-14,-4]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_premier5(self):
        args=[14,24]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_premier6(self):
        args=[14,-24]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.divisor(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.divisor(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_premier7(self):
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
