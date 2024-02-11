import unittest
import algorithms


arrays = [[1, 9, 8, 2, 3, 4, 5, 7, 6],[11,31,50,69,78,95,92,4,25,36,74],[1156, 9812, 8882, 228181, 311,14, 225, 1817, 886],[158, 889, 528, 852, 823, 854, 54, 47, 56]]
#for i in arrays:
    #i.sort()
targets = [4,92,1156,159]  
expected = [5,6,0,-1]

class AlgorithmsTests(unittest.TestCase):
    def test_linear_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.linear_search(array,targets[i])
            print(result)
            self.assertTrue(result, expected[i])

    def test_binary_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.binary_search(array,targets[i])
            print(result)
            self.assertTrue(result,expected[i])
        
    def test_ternary_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.ternary_search(array,targets[i])
            print(result)
            self.assertTrue(result, expected[i])

if __name__ == "__main__":
   unittest.main()
