import unittest
import matrix
import numpy as np


class Test(unittest.TestCase):
    mat1=np.random.randint(1,10,size=(3,2))
    m1 = matrix.matrix(mat1.tolist())
    mat2=np.random.randint(1,10,size=(3,3))
    m2 = matrix.matrix(mat2.tolist())
    mat3=np.random.randint(1,10,size=(5,5))
    m3 = matrix.matrix(mat3.tolist())
    mat4=np.random.randint(1,10,size=(3,2))
    m4 = matrix.matrix(mat4.tolist())
    
    def test__init(self):
        self.assertEqual(3,self.m1.r)
        self.assertEqual(2,self.m1.c)
        self.assertEqual(self.mat1.tolist(),self.m1.matrix)

    def test_add(self):
        with self.assertRaises(ValueError):
            m = self.m1 + self.m3
        m = self.m1 + self.m4
        self.assertEqual((self.mat1+self.mat4).tolist(),m)

    def test_sub(self):
        with self.assertRaises(ValueError):
            m = self.m1 - self.m3
        m = self.m1 - self.m4
        self.assertEqual((self.mat1-self.mat4).tolist(),m)
    
    def test_mul(self):
        with self.assertRaises(ValueError):
            m = self.m1 * self.m3
        m = self.m2 * self.m1
        self.assertEqual((self.mat2.dot(self.mat1)).tolist(),m)

    def test_det(self):
        with self.assertRaises(ValueError):
            m = self.m4.det()
        mat5=[[1,2,3,4,1],[0,-1,2,4,2],[0,0,4,0,0],[-3,-6,-9,-12,4],[0,0,1,1,1]]
        m5 = matrix.matrix(mat5)
        m = m5.det()
        self.assertEqual(28,m)

    def test_exp(self):
        with self.assertRaises(ValueError):
            m = self.m4**3
        m = self.m2**1
        self.assertEqual(self.mat2.tolist(),m)
        m = self.m2**3
        mat = np.identity(3,int)
        for i in range(3): 
            mat = mat.dot(self.mat2)
        self.assertEqual(mat.tolist(),m)

if __name__ == '__main__':
    unittest.main()