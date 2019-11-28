"""
In a B+ tree, in contrast to a B tree, all data are saved in the leaves

The maximum number of ieys in a record is called the order of the B+ Tree

The minimum number of keys per record is 1/2 of the maximum number of the keys.

For a n-order B+ tree with a height of h:
- maximum number of keys is n^h
- minimum number of keys is 2(n/2)^h-1

B+Tree Properties
A B+Tree is a M-way search tree
- perfectly balanced (every leaf node is at the same depth)
- every node other than the root, is at least half full
M/2 - 1 <= # keys <= M - 1
- Every inner node with k keys has k+1 non-null children

B+ Tree in practice
Typical fill-factor: 67% B-tree is more efficient

Typical Capacities

"""
class Node:
    def __init__(self):
        raise NotImplementedError

class InnerNode(Node):
    def __int__(self):
        raise NotImplementedError

class LeafNode(Node):
    """
    Leaf Node values
    Approach #1: Record Ids
        - A pointer to the location of the the tuple that
         the index entry corresponds to
    Approach #2: Tuple Data
        - The actual contents of the tuple is stored in the leaf node
        - Secondary indexes have to store the record id as their values
    """
    def __int__(self):
        self.level = None
        self.slots = None
        self.prev = None
        self.next = None

        # break up because binary search / variable length
        self.sorted_keys = []
        self.vals = []

class Cursor:
    """
    Cursor represents an iterator that can traverse over
    all items in the tree in sorted order.
    Cursors can do a variety of things
    - delete a row pointed by a cursor
    - modify the row pointed by a cursor
    - search a table for a given ID, and create a cursor pointing to the row with that ID
    things people do
    - create a cursor at the begining/end/row
    """
    def __int__(self):
        raise NotImplementedError

class Btree:
    """
    Keys must be an integer

    Methods supported
    - Delete(key)
    - ReplaceOrInsert(item)
    """
    def __init__(self, max_deg):
        self.root = None
        self.max_deg = max_deg

    def insert(self, key, val):
        """
        Find the correct leaf node L. Put data entry into L into sorted order.
        If L has enough space, done!
        Otherwise split L keys into L and a new node L2
            - redistribute entries evenly, copy up middle key.
            - insert index entry point to L2 into parent of L
        """

    def delete(self, key):
        """
        Start at root, find leaf L where entry belongs
        Remove the entry.
        If L is at least half-full, done!
        If L has only M/2 - 1 entries,
            - Try to re-distribute, borrowing from sibling(adjacent node
            with the same parent as L)
            - Ir re-distribution fails,
        """
