#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import Mot as student
import CorrMot as correct

class Test_mot(unittest.TestCase):
    def test_mot1(self): 
        args="Bonjour" #0
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.PlusLongMot(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.PlusLongMot(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_mot2(self): #OUI
        args="Bonjour Monsieur"
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.PlusLongMot(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.PlusLongMot(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_mot1(self): #0
        args="Je suis le patron de cette entreprise"
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.PlusLongMot(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.PlusLongMot(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_mot2(self): #Salaire insuffisant
        args="Veillez sortir tranquillement"
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.PlusLongMot(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.PlusLongMot(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    def test_mot2(self): #Salaire insuffisant
        args=" "
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.PlusLongMot(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.PlusLongMot(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
if __name__=='__main__':
    unittest.main()
