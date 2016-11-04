# import pdb; pdb.set_trace()
from comentario import app
import json
import unittest


class ComentarioTestCase(unittest.TestCase):

    def test_comentarios(self):
        tester = app.test_client(self)
        response = tester.get('/comentarios/1234', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertNotEqual(data[u'result'][u'post_id'], 0)


if __name__ == '__main__':
    unittest.main()
