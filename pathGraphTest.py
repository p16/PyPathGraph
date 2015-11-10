import unittest
import pathGraph

class MyTest(unittest.TestCase):
    def testSingleEdge(self):
        edges = [
            {'from': 'Dubai', 'to': 'Abu Dhabi'}
        ]

        orderedEdges = pathGraph.sortEdges(edges)

        self.assertEqual(1, len(orderedEdges))
        self.assertEqual('Dubai', orderedEdges[0]['from'])
        self.assertEqual('Abu Dhabi', orderedEdges[0]['to'])

    def testTwoEdges(self):
        edges = [
            {'from': 'abu dhabi', 'to': 'doha'},
            {'from': 'Dubai', 'to': 'Abu Dhabi'}
        ]

        orderedEdges = pathGraph.sortEdges(edges)

        self.assertEqual(2, len(orderedEdges))
        self.assertEqual('Dubai', orderedEdges[0]['from'])
        self.assertEqual('Abu Dhabi', orderedEdges[0]['to'])
        self.assertEqual('abu dhabi', orderedEdges[1]['from'])
        self.assertEqual('doha', orderedEdges[1]['to'])

    def testMoreEdges(self):
        edges = [
            {'from': 'abu dhabi', 'to': 'rome'},
            {'from': 'london', 'to': 'new york'},
            {'from': 'doha', 'to': 'abu dhabi'},
            {'from': 'Dubai', 'to': 'doha'},
            {'from': 'Rome', 'to': 'paris'},
            {'from': 'new york', 'to': 'dallas'},
            {'from': 'paris', 'to': 'London'}
        ]

        orderedEdges = pathGraph.sortEdges(edges)

        self.assertEqual(7, len(orderedEdges))
        self.assertEqual('Dubai', orderedEdges[0]['from'])
        self.assertEqual('doha', orderedEdges[0]['to'])
        self.assertEqual('doha', orderedEdges[1]['from'])
        self.assertEqual('abu dhabi', orderedEdges[1]['to'])
        self.assertEqual('abu dhabi', orderedEdges[2]['from'])
        self.assertEqual('rome', orderedEdges[2]['to'])
        self.assertEqual('Rome', orderedEdges[3]['from'])
        self.assertEqual('paris', orderedEdges[3]['to'])
        self.assertEqual('paris', orderedEdges[4]['from'])
        self.assertEqual('London', orderedEdges[4]['to'])
        self.assertEqual('london', orderedEdges[5]['from'])
        self.assertEqual('new york', orderedEdges[5]['to'])
        self.assertEqual('new york', orderedEdges[6]['from'])
        self.assertEqual('dallas', orderedEdges[6]['to'])

    def testExceptionMoreThanOneStartFromSamePoint(self):
        edges = [
            {'from': 'dubai', 'to': 'abu dhabi'},
            {'from': 'dubai', 'to': 'doha'}
        ]

        try:
            orderedEdges = pathGraph.sortEdges(edges)
        except Exception as e:
            self.assertEqual('Found duplicated edge that starts from: dubai', e.message)


    def testExceptionMoreThanOneStartingPoint(self):
        edges = [
            {'from': 'dubai', 'to': 'abu dhabi'},
            {'from': 'doha', 'to': 'dubai'},
            {'from': 'rome', 'to': 'dubai'}
        ]

        try:
            orderedEdges = pathGraph.sortEdges(edges)
        except Exception as e:
            self.assertEqual('There are more than one possible starting points', e.message)

    def testExceptionCyclicGraph(self):
        edges = [
            {'from': 'dubai', 'to': 'abu dhabi'},
            {'from': 'doha', 'to': 'dubai'},
            {'from': 'abu dhabi', 'to': 'doha'}
        ]

        try:
            orderedEdges = pathGraph.sortEdges(edges)
        except Exception as e:
            self.assertEqual('The given edges form a cycle, no starting point can be automatically selected', e.message)

suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner(verbosity=2).run(suite)
