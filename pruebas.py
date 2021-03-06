import unittest
import sistemaCuantico

class TestStringMethods(unittest.TestCase):

    def test_amplitudTrancision(self):
        v1=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
        v2=[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]
        self.assertEqual(sistemaCuantico.amplitudTrancision(v1,v2), (-0.02, -0.13))

    def test_ProgrammingDrill411(self):
        v=[(3,-1),(0,-2),(0,1),(2,0)]
        self.assertEqual(sistemaCuantico.probabilidadParticula(v,2), 5.26)

    def test_probabilidadParticula(self):
        v1=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]        
        self.assertEqual(sistemaCuantico.probabilidadParticula(v1,7), 10.87)
            
    def test_valorEsperado(self):
        v3=[(1/((2)**0.5),0),(0,1/((2)**0.5))]
        m1=[[(2,0),(1,1)],[(1,-1),(3,0)]]
        self.assertEqual(sistemaCuantico.valorEsperado(m1,v3), (1.5, 0.0))
        
if __name__ == '__main__':
    unittest.main()
