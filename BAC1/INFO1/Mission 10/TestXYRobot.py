import unittest
import math
import XYRobot as tb

class TestXYRobot(unittest.TestCase):
    def setUp(self):
        self.t=tb.XYRobot("R2 D2")
        
    def test_init(self):
        self.assertEqual(self.t.getangle(), 0,)
        self.assertEqual(self.t.position(), (0,0))
        
    def test_moveforward(self):
        forward=100
        x,y=self.t.position()
        position=(x+forward,y+0)
        angle = self.t.getangle()
        self.t.moveforward(100)
        self.assertEqual(self.t.position(), position)
        self.assertAlmostEqual(self.t.getangle(), angle)
        
    def test_movebackward(self):
        backward=50
        x,y=self.t.position()
        position=(x-backward,y-0)
        angle = self.t.getangle()
        self.t.movebackward(50)
        self.assertEqual(self.t.position(), position)
        self.assertAlmostEqual(self.t.getangle(), angle)
        
    def test_turn_left(self):
        position = self.t.position()
        angle = (self.t.getangle() + 90) % 360
        self.t.turnleft()
        self.assertNotEqual(self.t.getangle(), angle)
        self.assertEqual(self.t.position(),position)
        
    def test_turn_right(self):
        position = self.t.position()
        angle = (self.t.getangle() - 90) % 360
        self.t.turnleft()
        self.assertEqual(self.t.getangle(), angle)
        self.assertEqual(self.t.position(), position)
        
    def test_getHistory(self):
        expected_position = self.t.getHistory()
        self.t.moveforward(50)
        self.t.turnright()
        self.t.movebackward(100)
        self.t.turnleft()
        history=[('forward', 50), ('right', 90), ('backward', 100), ('left', 90)]
        self.assertEqual(history, expected_position)
        

if __name__ == '__main__':
    unittest.main()
        

