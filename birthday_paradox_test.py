import unittest
import birthday_paradox
from datetime import date

class BirthdayParadoxTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bp = birthday_paradox

    def test_getBirthdays_return_correctLenList(self):
        for i in [1, 3, 8, 15, 20, 50]:
            with self.subTest(i=i):
                res = self.bp.getBirthdays(i)
                self.assertEqual(len(res), i)
                
    def test_getBirthdays_return_listOfDates(self):
        self.assertIsInstance(self.bp.getBirthdays(4), list)
        self.assertIsInstance(self.bp.getBirthdays(4)[0], date)

    def test_getMatch_noMatch_return_None(self):
        listBD = [date(2001,1,1), date(2001,2,2), date(2001,3,3)]
        res = self.bp.getMatch(listBD)
        self.assertIsNone(res)

    def test_getMatch_oneMatch_return_OneDate(self):
        listBD = [date(2001,1,1), date(2001,2,2), date(2001,3,3), date(2001,1,1)]
        exp = date(2001,1,1)
        res = self.bp.getMatch(listBD)
        self.assertEqual(exp, res)

    def test_getMatch_twoMatch_return_firstDate(self):
        listBD = [date(2001,1,1), date(2001,2,2), date(2001,3,3), date(2001,1,1), date(2001,3,3)]
        exp = date(2001,1,1)
        res = self.bp.getMatch(listBD)
        self.assertEqual(exp, res)

if __name__ == '__main__':
    unittest.main()