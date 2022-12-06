import tree
f = open('lenses.txt')
lenses = [str.strip(inst).split('\t') for inst in f.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = tree.createTree(lenses, lensesLabels)
print(lensesTree)
