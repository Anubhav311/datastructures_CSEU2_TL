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

    def __str__(str):
        # set an empty string variable
        s = ""
        # set our current node to the contents head
        current_node = self.contents.head
        # while there are still nodes
        while current_node:
            # append the current value to the return string
            s += current_node.value
            # set current nodes to current nodes next
            current_node = current_node.next
        # return the string
        return s

    def append(self, string_to_add):
        # loop over each character in the string and add it to tail
        for char in string_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, string_to_add):
        # reverse incoming string to maintain order
        # loop over each character in string and add it to head
        for char in string_to_add[::-1]:
            self.contents.add_to_head(char)

    def delete_front(self, chars_to_remove):
        # loop over all chars to remove
        for _ in range(chars_to_remove):
            # remove from tail
            self.contents.remove_from_head()