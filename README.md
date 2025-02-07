

Libraries Used

matplotlib - for generating charts

time - for measuring algorithm execution time

gc - for enabling and disabling garbage collection to avoid interference with execution time measurements

Project Structure

The project consists of three files:

nary_heap.py: Contains the NaryHeap class. When creating an object of this class, you must specify the heap's arity and optionally provide a list of numbers to build the heap from. By default, the NaryHeap object is created with an empty list.

main.py: Contains the function for measuring execution time and generating performance charts.

test_heap.py: Contains unit tests for the NaryHeap class methods.

Installation and Execution

Clone the repository:


To run the program, execute:

python3 main.py

The program generates three charts showing execution time as a function of the number of elements for the following methods:

push (inserting an element into the heap)

pop (removing the heap's top element)

build_heap (heap construction)

These charts are saved as .png files.


Example Charts

Push Method

Heap Construction

Pop Method

Chart Analysis

The charts indicate that removing the heap's top element, inserting an element, and constructing the heap are slowest for a binary heap and fastest for a 7-ary heap. This is because heaps with smaller arity have a greater height for the same number of elements, negatively impacting execution time.

Heap Display in Terminal

Binary Heap

5-ary Heap

7-ary Heap

