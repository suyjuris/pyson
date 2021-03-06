#!/usr/bin/env python

import unittest

import pyson
import pyson.stdlib
import pyson.runtime


class StdlibTest(unittest.TestCase):

    def test_concat_strings(self):
        agent = pyson.runtime.Agent()
        intention = pyson.runtime.Intention()
        X = pyson.Var()

        term = pyson.Literal(".concat", ("hello", " ", "world", X))
        next(pyson.stdlib._concat(agent, term, intention))

        self.assertEqual(X.grounded(intention.scope), "hello world")

    def test_concat_lists(self):
        agent = pyson.runtime.Agent()
        intention = pyson.runtime.Intention()
        X = pyson.Var()

        term = pyson.Literal(".concat", ((1, 2), (3, ), X))
        next(pyson.stdlib._concat(agent, term, intention))

        self.assertEqual(X.grounded(intention.scope), (1, 2, 3))


if __name__ == "__main__":
    unittest.main()
