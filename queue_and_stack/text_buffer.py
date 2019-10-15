from doubly_linked_list import DoublyLinkedList

class TextBuffer:

    def __init__(self, init=None):
        # create a storage contents for the buffer
        self.contents = DoublyLinkedList()
        # check if an init string has been provided
        if init:
            # if so insert the init string in to the contents
            for char in init:
                self.contents.add_to_tail(char)
        pass

    def __str__(str):
        pass

    def append(self, string_to_add):
        pass

    def prepend()