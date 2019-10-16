from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if the key exists in the storage
        if key in self.storage:
            # set the node to the item at the key in the storage
            node = self.storage[key]
            # move the node to end of order
            self.order.move_to_end(node)
            # return the node value
            return node.value
        # otherwise
        else:
            # return None
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key exists in storage
        if key in self.storage:
            # set the node to the storage at the key
            node = self.storage[key]
            # set the node value to the key value pair
            node.value = (key, value)
            # move the node to the end and return to caller
            self.order.move_to_end(node)
        # if the size is reaching the limit
        elif self.size == self.limit
            # delete the item at the head of the storage order

            # remove node from head of the order
            # decrement the size
        # add the key value pair to the orders tail
        # set the storage at key to the orders tail
        # increment size
