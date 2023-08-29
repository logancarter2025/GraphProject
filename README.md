
# Graph ADT with Applications

In this project, I designed a graph abstract data type (ADT) using Python's object-oriented programming (OOP) principles, with an emphasis on efficiency. This implementation ensures optimal runtime for traversing all nodes and edges of the graph. Furthermore, I integrated several renowned algorithms to determine the shortest-cost paths between two nodes and to generate minimal spanning trees.
## Usage/Examples

To execute any algorithm, you'll first need a text file formatted with data separated by commas. You can find sample files in the repository for reference. In this file, each line should contain two nodes followed by a floating-point number, separated by commas. This number signifies the distance between the connected nodes. For instance:

A,B,4.8  

This implies there's an edge connecting node A to node B with a length of 4.8.

Upon supplying the text file, you'll be asked to specify whether the graph is directed. If you input 'y', it means the edge is one-way – in the example given, you can traverse from A to B, but not from B to A. On the other hand, if you input 'n', it means the edge is bidirectional, allowing movement from A to B and vice versa, both with a distance of 4.8.

Certain algorithms might require additional inputs based on the specific information they need. Once you've provided all necessary details, the results from the algorithm will be displayed in the terminal.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [Logan Carter](https://www.github.com/logancarter2025)