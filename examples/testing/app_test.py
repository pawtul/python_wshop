import unittest

import mock

from app import read_content_of_file


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.path = 'report'

    @mock.patch('app.open')
    def test_reading_content(self, mocked_open):
        mocked_file = mock.MagicMock()
        mocked_file.read = mock.MagicMock(return_value='Hello')
        mocked_open.return_value = mocked_file
        self.assertEqual(read_content_of_file('asdf'), 'Hello')


if __name__ == '__main__':
    unittest.main()

