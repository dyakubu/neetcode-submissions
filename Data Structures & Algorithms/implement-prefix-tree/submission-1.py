class Node:
    def __init__(self, char=None, children=None, is_terminal=False):
        if char is None:
            self.char = "ROOT"
            print(f"Creating empty node with id {self.char}")
        else:
            self.char = char 
        
        if children == None:
            self.children = [None] * 26
        
        self.is_terminal = is_terminal

    def add_child(self, child):
        if not isinstance(child, Node):
            idx = ord('a') - ord(child)
            child = Node(child)
        
        else:
            idx = ord('a') - ord(child.char)
        
        # At this point, child is guaranteed to be a node and idx is its position
        # in the current node's children 

        if self.children[idx] is not None:
            if child.is_terminal:
                self.children[idx].is_terminal = child.is_terminal
        else:
            self.children[idx] = child 
        return self.children[idx]

    def get_child(self, child):

        if not isinstance(child, Node):
            child = Node(child)
        
        idx = ord('a') - ord(child.char)

        if self.children[idx] is None:
            return None  
        
        return self.children[idx]


    def is_terminal_node(self):
        return self.is_terminal



class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:

        self._insert_helper(self.root, word, 0, len(word))

        # Find first letter
        # if there, move on to next in same path
        # If not, create it

    def _insert_helper(self, node, word, start, stop):

        if start == stop - 1:
            cur = word[start]
            cur = Node(cur, is_terminal=True)
            node.add_child(cur)
            return

        cur = word[start]
        if cur not in node.children:
            cur = node.add_child(cur)
        else:
            cur = node.get_child(cur)
        self._insert_helper(cur, word, start+1, stop)


    def search(self, word: str) -> bool:
        return self._search_helper(self.root, word, 0, len(word), prefix_only=False)

    def _search_helper(self, node, word, start, stop, prefix_only):

        if not word:
            return True

        if start == stop:
            if prefix_only:
                return True
            return False

        cur_char = word[start] #a
        cur = node.get_child(cur_char)

        if cur is None:
            return False 
        
        if start == stop - 1 and cur.is_terminal_node():
            return True
        
        return self._search_helper(cur, word, start+1, len(word), prefix_only)


    def startsWith(self, prefix: str) -> bool:
        return self._search_helper(self.root, prefix, 0, len(prefix), prefix_only=True)
    
        
        