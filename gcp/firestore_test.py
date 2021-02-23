import unittest
import firestore 

fs = firestore.Firestore()
test_key = "testDude"
test_value = { 
    "score":1, 
    "failure_by": "Crushed by Rock"
}

class TestFirestoreMethods(unittest.TestCase):

    def tearDown(self):
        test_key = "testDude"
        fs.delete(collection="users", key=test_key)

    def test_lookup(self):
        self.assertFalse(fs.lookup(collection="users", key=test_key))
        fs.add(collection="users", key=test_key, value= test_value)
        self.assertTrue(fs.lookup(collection="users", key=test_key))

    def test_add(self):
        fs.add(collection="users", key=test_key, value=test_value)
        self.assertTrue(fs.lookup(collection="users", key=test_key))

    def test_delete(self):
        fs.add(collection="users", key=test_key, value=test_value)
        self.assertTrue(fs.lookup(collection="users", key=test_key))

    '''
    def test_update(self):
        fs.add(collection="users", key=test_key, value=test_value)
        self.assertTrue(fs.lookup(collection="users", key=test_key))
    '''
    

if __name__ == '__main__':
    unittest.main()