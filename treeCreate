from Bio import Phylo
from io import StringIO

# Example tree data in Newick format
treedata = "(A, (B, C), (D, E));"

# Parse the tree data
handle = StringIO(treedata)
tree = Phylo.read(handle, "newick")

# Print the tree
print(tree)

# You can also draw the tree
# Phylo.draw(tree) # Uncomment to draw the tree if you have matplotlib installed
