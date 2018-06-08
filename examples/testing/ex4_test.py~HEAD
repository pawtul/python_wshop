import unittest

import mock
import requests

# właściwosci mocka
mock_obj = mock.MagicMock()
print("=====nieistniejacy atrybut")
print(mock_obj.nieistniejacy_atrybut)  # nieistniejące atrybuty zostaną zastąpione nowymi Mockami
mock_obj.metoda = mock.MagicMock()  # to będzie metoda
print("=====wywolanie metody")
print(mock_obj.metoda())  # znowu jest MagicMock
mock_obj.metoda.return_value = 123
print(mock_obj.metoda())  # teraz jest wartość

print("=====wywolanie metody z side_effect")
def side_effect():
    print("side effect")

mock_obj.metoda.side_effect = side_effect
print(mock_obj.metoda())  # wykonał się side_effect - ale nie ma return value!


def read_content_of_webpage(url):
    return requests.get(url).text


class MockedTestCase(unittest.TestCase):
    def test_reading_content(self):
        response = mock.MagicMock()  # tworzymy response
        response.text = 'Hello'  # atrybut text odpowiedzi to 'Hello'
        requests.get = mock.MagicMock(return_value=response)  # podstawiamy naszego mocka za funkcję 'get'
                                                              # od razu oznaczamy response jako wartość,
                                                              # którą zmokowana funkcja ma nam zwrócić
        content = read_content_of_webpage('blablabla')
        self.assertEqual(content, 'Hello')
        # dodatkowe ciekawe motody mocka
        m = requests.get
        m.call_args_list  # lista argumentów wywołań
        m.call_args  # argumenty z ostatniego wywołania
        m.assert_called_with('blablabla')
        m.assert_called_once()
        m.assert_called_once_with('blablabla')
        m.assert_called()
        m.reset()  # czysci mocka


if __name__ == '__main__':
    unittest.main()

