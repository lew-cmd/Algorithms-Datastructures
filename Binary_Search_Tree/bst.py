from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is not a TreeNode or not None.
        """
        self._root = root
        self._size = 0 if root is None else 1

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError

        if self.find(key):
            raise KeyError("key exists already")

        if self._root is None:
            self._root = TreeNode(key, value)
        else:
            self._insert_helper(self._root, key, value)

        self._size += 1

    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        if key is None or not isinstance(key, int):
            raise ValueError

        node = self.find_helper(self._root, key)

        #if node is None:
        #    raise KeyError
        #else:
        return node

    def find_helper(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return self.find_helper(root.left, key)
        else:
            return self.find_helper(root.right, key)


    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""
        return self._size

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size 

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError("key is not an integer")

        remove_node = self.find(key)
        root, left, right = False, False, False

        if not remove_node:
            raise KeyError("key does not exists")

        else:
            if key == self._root.key:
                #delete root - special case, no parent
                root = True

            #check if removal node is left or right of parent
            elif key < remove_node.parent.key:
                left = True
            elif key > remove_node.parent.key:
                right = True

            #find replacement node

            #easy case, no children
            if remove_node.left is None and remove_node.right is None:
                replace = None

            #one child
            elif (remove_node.left is None and remove_node.right is not None) or (
                    remove_node.left is not None and remove_node.right is None):
                if remove_node.left is not None:
                    remove_node.left.parent = remove_node.parent
                    replace = remove_node.left
                else:
                    remove_node.right.parent = remove_node.parent
                    replace = remove_node.right

            #two children
            elif remove_node.left is not None and remove_node.right is not None:
                #left child has right child
                if remove_node.left.right is not None:
                    remove_node.left.right.parent = remove_node.parent
                    remove_node.left.right.right = remove_node.right
                    replace = remove_node.left.right
                    remove_node.right.parent = replace
                #left child has no child or only a left child
                else:
                    remove_node.left.parent = remove_node.parent
                    remove_node.left.right = remove_node.right
                    replace = remove_node.left
                    remove_node.right.parent = replace


            #reconnecting parent to new child
            if left:
                remove_node.parent.left = replace
            elif right:
                remove_node.parent.right = replace
            elif root:
                self._root.parent = None
                self._root = replace

        # check if it worked
        check = self.find(key)
        if check == None:
            self._size -= 1
            return True
        else:
            return False

    # Hint: The following 3 methods can be implemented recursively, and
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        else:
            def inorder_rec(node):
                if node.left is not None:
                    yield from inorder_rec(node.left)
                yield node
                if node.right is not None:
                    yield from inorder_rec(node.right)

            yield from inorder_rec(node)

        """    #left up right
        if node.left:
            yield from self._inorder(node.left)
        if node.right:
            yield from self._inorder(node.right)
        def traverse_tree(node):
        if not node.children:
            yield node
        for child in node.children:
            yield from traverse_tree(child)"""

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())

        else:
            def preorder_rec(node):
                yield node
                if node.left is not None:
                    yield from preorder_rec(node.left)
                if node.right is not None:
                    yield from preorder_rec(node.right)

            yield from preorder_rec(node)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        else:
            def postorder_rec(node):
                if node.left is not None:
                    yield from postorder_rec(node.left)
                if node.right is not None:
                    yield from postorder_rec(node.right)
                yield node
            yield from postorder_rec(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]: 
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""

        if self._root is None:
            return False

        return self.check_bst(self._root)

    def check_bst(self, node):
        if node is None:
            return True

        if (node.left is not None) and (node.key < node.left.key):
            return False

        if (node.right is not None) and (node.key > node.right.key):
            return False

        return self.check_bst(node.left) and self.check_bst(node.right)

    def return_min_key(self) -> TreeNode:
        """Return the node with the smallest key (None if tree is empty)."""
        min = None
        min = self.min_search(self._root, min)
        return min

    def min_search(self, node, cur_min):

        if cur_min is None:
            cur_min = node
        elif cur_min.key > node.key:
            cur_min = node

        if node.left is not None:
            cur_min = self.min_search(node.left, cur_min)
        if node.right is not None:
            cur_min = self.min_search(node.right, cur_min)
        return cur_min

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute
            the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(node.key for node in self._preorder(self._root))
        print(python_list)

        bst = BinarySearchTree()

        for n in python_list:
            bst.insert(TreeNode(key=n, value=n))

        search = bst._root
        bst_comp = 0

        while (search.key != key and search.key != None):
            bst_comp += 1
            # by the bst rules, smaller stuff is left
            if key < search.key and search.left != None:
                search = search.left
            # bigger stuff is right
            elif key > search.key and search.right != None:
                search = search.right
            else:
                search = None
                break

        # time list
        list_comp = 0

        for n in python_list:
            list_comp += 1
            if key == n:
                break

        return tuple(bst_comp, list_comp)

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        output = []
        for k in self.inorder(current_node):
            output.append(k)
        return output

    def _preorder(self, current_node):
        output = []
        for k in self.preorder(current_node):
            output.append(k)
        return output

    def _postorder(self, current_node):
        output = []
        for k in self.postorder(current_node):
            output.append(k)
        return output

    def _insert_helper(self, cur, key, value):
        if cur.key < key:
            if cur.right is None:
                cur.right = TreeNode(key, value)
                cur.right.parent = cur
            else:
                self._insert_helper(cur.right, key, value)

        elif cur.key > key:
            if cur.left is None:
                cur.left = TreeNode(key, value)
                cur.left.parent = cur
            else:
                self._insert_helper(cur.left, key, value)

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)
