# Sorting edges into a path graph without cycles

The idea is to have a function that will accept a set of unordered edges, and will return them ordered so that each edge is traversed.

## Input

The input of the function is a list of dictionaries of the following format

```python
edges = [
    {'from': 'abu dhabi', 'to': 'rome'},
    {'from': 'london', 'to': 'new york'},
    ...
]
```

## Running the tests

```
python pathGraphTest.py
```

## Performances

The algorithm to order the edges is of linear complexity O(n).

The unordered edges array is scanned 4 times:

- to add metadata to each edge
- calculate the In-degree of the nodes
- select the starting point
- pick the next ordered edge
