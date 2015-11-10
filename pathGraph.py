def sortEdges(edges):
    edgesWithMetadata = {}

    for edge in edges:
        if edge['from'] in edgesWithMetadata.keys():
            raise Exception("Found duplicated edge that starts from: " + edge['from'])

        edgesWithMetadata[edge['from'].lower()] = {
            'edge': edge,
            'to': edge['to'].lower(),
            'incomingEdges': 0
        }

    for key, edge in edgesWithMetadata.iteritems():
        if edge['to'] in edgesWithMetadata.keys():
            edgesWithMetadata[edge['to']]['incomingEdges'] += 1

    start = None
    for key, edge in edgesWithMetadata.iteritems():
        if (start != None) & (edge['incomingEdges'] == 0):
            raise Exception("There are more than one possible starting points")

        if edge['incomingEdges'] == 0:
            start = edge['edge']

    if start == None:
        raise Exception("The given edges form a cycle, no starting point can be automatically selected")

    return _orderEdges(start, edgesWithMetadata)

def _orderEdges(edge, edgesWithMetadata):
    found = True;
    orderedEdges = [edge];

    while found:
        if edge['to'].lower() in edgesWithMetadata.keys():
            nexEdge = edgesWithMetadata[edge['to'].lower()]
            orderedEdges.append(nexEdge['edge']);
            edge = nexEdge['edge']
        else:
            found = False

    return orderedEdges

