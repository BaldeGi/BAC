#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import Credit as student
import CorrCredit as correct

class Test_credit(unittest.TestCase):
    def test_credit1(self): #0
        args=[100,5/100,10,1500]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.credit(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.credit(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_credit1(self):
        args=[10000,5/100,10,1500]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.credit(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.credit(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_credit2(self): #OUI
        args=[10000,2/100,2,15000]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.credit(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.credit(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_credit1(self):
        args=[10000,5/100,10,1500]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.credit(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.credit(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_credit2(self): #Salaire insuffisant
        args=[10000,2/100,2,0]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.credit(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.credit(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_credit1(self):
        args=[10000,5/100,10,1500]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.credit(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.credit(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
        
        
        
if __name__=='__main__':
    unittest.main()
        