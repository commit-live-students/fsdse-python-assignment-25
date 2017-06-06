from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dic = {1: 10, 2: 20, 3: 30}
        res = solution(dic)

        self.assertEqual(res, 60)


