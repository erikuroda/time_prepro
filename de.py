def conll_file_demo():
    print('Mass conll_read demo...')
    graphs = [DependencyGraph(entry) for entry in conll_data2.split('\n\n') if entry]
    for graph in graphs:
        tree = graph.tree()
        print('\n')
        tree.pprint()


def conll_demo():
    """
    A demonstration of how to read a string representation of
    a CoNLL format dependency tree.
    """
    dg = DependencyGraph(conll_data1)
    tree = dg.tree()
    tree.pprint()
    print(dg)
    print(dg.to_conll(4))
