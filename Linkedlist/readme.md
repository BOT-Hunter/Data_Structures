This readme file instructs the use of this linkedlist.

Classes:
a) Node:

b) linkedlist:
Methods available:
- append() -> takes a node obj and appends at the end.
- pop() -> takes no argument, removes the last element of the linked list.
- insert() -> takes one int and one node obj as argument and insert the node obj at the postion of the int.
- delete() -> takes one int for position and delete the element from that position.
- size() -> returns the size of the linkedlist.
- get() -> takes one int argument and returns the element at the index(int).
- get_first() -> returns the first element of the linkedlist.
- get_last() -> returns the last element of the linkedlist.
- to_array() -> converts the linkedlist into a python list and return it.
- printlist() -> prints the linkedlist converted into python list.

Note:
--> Index start from 1 except of 0.
--> If the int provided as positional argument is greater than size of the linkedlist, it raises IndexError exception.
--> Inserting on position 1 in an empty linkedlist is possible and will initialize the linkedlist with that node.