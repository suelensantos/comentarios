# import pdb; pdb.set_trace()
from comentario import app
import json
import unittest


class ComentarioTestCase(unittest.TestCase):

    def setUp(self):
        tester = app.test_client(self)
        self.response = tester.get('comentarios/1234', content_type='application/json')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_comentarios(self):
        data = json.loads(self.response.data)
        self.assertNotEqual(data[u'result'][u'post_id'], 0)


if __name__ == '__main__':
    unittest.main()
