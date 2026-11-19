Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================ RESTART: C:/Users/Hp/OneDrive/Documents/daa.py ================
============================================================
       DAA ASSIGNMENT 5 - COMPLETE PROJECT
============================================================


######## TASK B1 ########

 =======================================================
TEST 1 - COLOURABLE GRAPH
=======================================================

VERSION 1 - INPUT ORDER
Colourable: True
Final colouring: [0, 1, 0, 1]
Search nodes: 5
Candidate assignments: 6
Rejected branches: 2
Backtracks: 0
Maximum depth: 4

VERSION 2 - HEURISTIC ORDER
Colourable: True
Final colouring: [1, 0, 1, 0]
Search nodes: 5
Candidate assignments: 6
Rejected branches: 2
Backtracks: 0
Maximum depth: 4

 =======================================================
TEST 2 - NOT COLOURABLE GRAPH
=======================================================

VERSION 1 - INPUT ORDER
Colourable: False
Final colouring: None
Search nodes: 5
Candidate assignments: 10
Rejected branches: 6
Backtracks: 4
Maximum depth: 2

VERSION 2 - HEURISTIC ORDER
Colourable: False
Final colouring: None
Search nodes: 5
Candidate assignments: 10
Rejected branches: 6
Backtracks: 4
Maximum depth: 2

 =======================================================
TEST 3 - BOUNDARY CASE
=======================================================

VERSION 1 - INPUT ORDER
Colourable: True
Final colouring: [0]
Search nodes: 2
Candidate assignments: 1
Rejected branches: 0
Backtracks: 0
Maximum depth: 1

VERSION 2 - HEURISTIC ORDER
Colourable: True
Final colouring: [0]
Search nodes: 2
Candidate assignments: 1
Rejected branches: 0
Backtracks: 0
Maximum depth: 1

B1.4 - ORDERING COMPARISON
Measure                  Version 1      Version 2      
Search nodes             7              7              
Candidate assignments    12             12             
Rejected branches        6              6              
Backtracks               0              0              


######## TASK B2 ########

GRAPH A - EASY GRAPH
Result: True
Colouring: [0, 0, 0, 0, 0, 0]
Search nodes: 7
Rejected branches: 0
Backtracks: 0

GRAPH B - DIFFICULT GRAPH
Result: False
Colouring: None
Search nodes: 5
Rejected branches: 6
Backtracks: 4

B2 COMPARISON
Graph A vertices: 6
Graph B vertices: 6
Available colours: 2

Graph A search nodes: 7
Graph B search nodes: 5

Explanation:
Graph A has no conflicts.
Graph B has conflicts between every pair of vertices.
Graph B becomes impossible to colour using only two colours.
Input structure affects backtracking performance.


######## TASK B3 ########

 -------------------------------------------------------
INSTANCE 1
-------------------------------------------------------
Zones: {1, 2, 3, 4, 5}
Centres: {'C1': {1, 2, 3}, 'C2': {2, 3, 4}, 'C3': {4, 5}, 'C4': {1, 5}}

EXACT SOLUTION
Selected centres: ['C1', 'C3']
Solution size: 2
Search combinations: 6

GREEDY SOLUTION
Selected centres: ['C1', 'C3']
Solution size: 2
Greedy operations: 7
Same optimal size: True

 -------------------------------------------------------
INSTANCE 2
-------------------------------------------------------
Zones: {1, 2, 3, 4, 5, 6}
Centres: {'A': {1, 2, 3}, 'B': {4, 5}, 'C': {5, 6}, 'D': {1, 2, 4}, 'E': {3, 6}}

EXACT SOLUTION
Selected centres: ['A', 'B', 'C']
Solution size: 3
Search combinations: 16

GREEDY SOLUTION
Selected centres: ['A', 'B', 'C']
Solution size: 3
Greedy operations: 12
Same optimal size: True

 -------------------------------------------------------
INSTANCE 3
-------------------------------------------------------
Zones: {1, 2, 3, 4, 5, 6, 7}
Centres: {'A': {1, 2, 3, 4}, 'B': {3, 4, 5}, 'C': {5, 6, 7}, 'D': {1, 2, 6}, 'E': {4, 7}}

EXACT SOLUTION
Selected centres: ['A', 'C']
Solution size: 2
Search combinations: 7

GREEDY SOLUTION
Selected centres: ['A', 'C']
Solution size: 2
Greedy operations: 9
Same optimal size: True

B3.2 - GREEDY COUNTEREXAMPLE

 -------------------------------------------------------
COUNTEREXAMPLE
-------------------------------------------------------
Zones: {1, 2, 3, 4, 5, 6}
Centres: {'A': {1, 2, 3, 4}, 'B': {1, 2, 5}, 'C': {3, 4, 6}, 'D': {5}, 'E': {6}}

EXACT SOLUTION
Selected centres: ['B', 'C']
Solution size: 2
Search combinations: 10

GREEDY SOLUTION
Selected centres: ['A', 'B', 'C']
Solution size: 3
Greedy operations: 12
Same optimal size: False

GREEDY DECISION TRACE
Choose: A | Newly covered: {1, 2, 3, 4}
Choose: B | Newly covered: {5}
Choose: C | Newly covered: {6}

Greedy cover: ['A', 'B', 'C']
Exact cover: ['B', 'C']

B3.3 - SCALABILITY COMPARISON

 -------------------------------------------------------
LARGER INSTANCE
-------------------------------------------------------
Zones: {1, 2, 3, 4, 5, 6, 7, 8}
Centres: {'C1': {1, 2, 3}, 'C2': {3, 4, 5}, 'C3': {5, 6, 7}, 'C4': {8, 1, 7}, 'C5': {2, 4, 6}, 'C6': {8, 1, 5}, 'C7': {2, 3, 7}, 'C8': {8, 4, 6}, 'C9': {1, 2, 6}, 'C10': {3, 5, 7}}

EXACT SOLUTION
Selected centres: ['C1', 'C3', 'C8']
Solution size: 3
Search combinations: 68

GREEDY SOLUTION
Selected centres: ['C1', 'C3', 'C8']
Solution size: 3
Greedy operations: 27
Same optimal size: True

Scalability operation counts:
Exact combinations: 68
Greedy operations: 27


######## TASK B4 ########
Server capacity: 10
Original workloads: [7, 5, 6, 2, 3, 5, 4, 2]

FIRST FIT DECREASING RESULT
Server 1: [7, 3]
Used capacity: 10
Remaining capacity: 0

Server 2: [6, 4]
Used capacity: 10
Remaining capacity: 0

Server 3: [5, 5]
Used capacity: 10
Remaining capacity: 0

Server 4: [2, 2]
Used capacity: 4
Remaining capacity: 6

Total servers used: 4
Placement operations: 16

B4.2 - CHALLENGING INPUT
Challenging workloads: [6, 6, 6, 4, 4, 4, 2, 2, 2]
Server 1: [6, 4] | Remaining: 0
Server 2: [6, 4] | Remaining: 0
Server 3: [6, 4] | Remaining: 0
Server 4: [2, 2, 2] | Remaining: 4
Servers used: 4
Placement operations: 20

B4.3 - ENGINEERING DECISION
Strategy: First Fit Decreasing
Advantage: Fast workload allocation.
Guarantee: All valid workloads are assigned.
Limitation: Minimum server count is not guaranteed.
Exact search is suitable for small instances.
Monitor server utilisation and remaining capacity.


============================================================
       ALL TASKS COMPLETED SUCCESSFULLY
============================================================

===================================================== RESTART: C:/Users/Hp/OneDrive/Documents/daa.py ====================================================
3 50
Auth 10 60
Search 20 100
Payments 30 120
Greedy Value = 160
Maximum Value = 220
Selected = Search Payments
Budget Used = 50

============================================== RESTART: C:/Users/Hp/OneDrive/Documents/ASSESNMENT 5 CODE.py =============================================


*****************************************************************
       DAA ASSIGNMENT 5 - CO5
 SEARCH, COMPLEXITY AND APPROXIMATION ENGINEERING
*****************************************************************

=================================================================
TASK B1 - GRAPH COLOURING
=================================================================

 Test 1 - Colourable Path
Colourable: True
Final colouring: [0, 1, 0, 1]
Search nodes: 5
Candidate assignments: 6
Rejected branches: 2
Backtracks: 0
Maximum depth: 4

 Test 2 - Non-Colourable Triangle
Colourable: False
Final colouring: None
Search nodes: 5
Candidate assignments: 10
Rejected branches: 6
Backtracks: 4
Maximum depth: 2

 Test 3 - Boundary Case
Colourable: True
Final colouring: [0]
Search nodes: 2
Candidate assignments: 1
Rejected branches: 0
Backtracks: 0
Maximum depth: 1

B1.3 AND B1.4 - ORDERING COMPARISON

 VERSION 1 - INPUT ORDER
Colourable: True
Final colouring: [0, 1, 2, 0, 1, 2]
Search nodes: 7
Candidate assignments: 12
Rejected branches: 6
Backtracks: 0
Maximum depth: 6

 VERSION 2 - HEURISTIC ORDER
Colourable: True
Final colouring: [2, 0, 1, 1, 0, 2]
Search nodes: 7
Candidate assignments: 12
Rejected branches: 6
Backtracks: 0
Maximum depth: 6

=================================================================
TASK B2 - ADVERSARIAL INPUT EXPERIMENT
=================================================================

 GRAPH A - EASY GRAPH
Colourable: True
Final colouring: [0, 0, 0, 0, 0, 0]
Search nodes: 7
Candidate assignments: 6
Rejected branches: 0
Backtracks: 0
Maximum depth: 6

 GRAPH B - DIFFICULT GRAPH
Colourable: False
Final colouring: None
Search nodes: 5
Candidate assignments: 10
Rejected branches: 6
Backtracks: 4
Maximum depth: 2

OBSERVATION:
Graph A has no conflicts and is easily coloured.
Graph B is a complete graph and needs six colours.
Therefore, Graph B cannot be coloured using two colours.
Input size alone does not determine search effort.
Graph structure and pruning also affect performance.

=================================================================
TASK B3 - EXACT VS GREEDY SET COVER
=================================================================

 INSTANCE 1
Universe: ['1', '2', '3', '4', '5']
Centres: {'C1': {'3', '1', '2'}, 'C2': {'3', '4', '2'}, 'C3': {'5', '4'}, 'C4': {'1', '5'}}
Exact solution: ['C1', 'C3']
Exact solution size: 2
Exact search states: 6
Greedy solution: ['C1', 'C3']
Greedy solution size: 2
Greedy evaluations: 8
Same solution size: True

 INSTANCE 2
Universe: ['1', '2', '3', '4', '5', '6']
Centres: {'C1': {'3', '1', '2'}, 'C2': {'5', '4', '6'}, 'C3': {'1', '4', '2'}, 'C4': {'3', '5', '6'}}
Exact solution: ['C1', 'C2']
Exact solution size: 2
Exact search states: 5
Greedy solution: ['C1', 'C2']
Greedy solution size: 2
Greedy evaluations: 8
Same solution size: True

 INSTANCE 3
Universe: ['1', '2', '3', '4', '5', '6']
Centres: {'C1': {'1', '2'}, 'C2': {'3', '4'}, 'C3': {'5', '6'}, 'C4': {'3', '1', '4', '2'}, 'C5': {'5', '6'}}
Exact solution: ['C3', 'C4']
Exact solution size: 2
Exact search states: 13
Greedy solution: ['C4', 'C3']
Greedy solution size: 2
Greedy evaluations: 10
Same solution size: True

=================================================================
B3.2 - GREEDY COUNTEREXAMPLE
=================================================================

 COUNTEREXAMPLE
Universe: ['1', '2', '3', '4', '5', '6', '7', '8']
Centres: {'A': {'1', '2', '5', '3', '6'}, 'B': {'3', '1', '4', '2'}, 'C': {'7', '5', '8', '6'}, 'D': {'7', '4'}}
Exact solution: ['B', 'C']
Exact solution size: 2
Exact search states: 8
Greedy solution: ['A', 'C', 'B']
Greedy solution size: 3
Greedy evaluations: 12
Same solution size: False

GREEDY TRACE:
Selected: A
Newly covered: ['1', '2', '3', '5', '6']
Remaining zones: ['4', '7', '8']
Selected: C
Newly covered: ['7', '8']
Remaining zones: ['4']
Selected: B
Newly covered: ['4']
Remaining zones: []

Exact solution uses: 2 centres
Greedy solution uses: 3 centres

=================================================================
B3.3 - SCALABILITY EXPERIMENT
=================================================================

Problem size: 12 zones, 6 centres
Exact search states: 63
Greedy evaluations: 36
Exact cover size: 6
Greedy cover size: 6

Problem size: 16 zones, 8 centres
Exact search states: 255
Greedy evaluations: 64
Exact cover size: 8
Greedy cover size: 8

B3.4 - ENGINEERING TRADE-OFF
Exact search guarantees the minimum-size cover.
Greedy reduces search effort and produces a feasible cover.
Greedy does not guarantee optimality.

=================================================================
TASK B4 - BIN PACKING
=================================================================
Server capacity: 10
Original workloads: [7, 5, 5, 4, 4, 2, 2]

FIRST FIT DECREASING RESULT

Number of servers used: 3
Server 1 | Workloads: [7, 2] | Used: 9 | Remaining capacity: 1
Server 2 | Workloads: [5, 5] | Used: 10 | Remaining capacity: 0
Server 3 | Workloads: [4, 4, 2] | Used: 10 | Remaining capacity: 0

=================================================================
B4.2 - CHALLENGE INPUT
=================================================================
Capacity: 10
Challenge workloads: [6, 5, 5, 4, 4, 4, 4, 4, 4]

Number of servers used: 5
Server 1 | Workloads: [6, 4] | Used: 10 | Remaining capacity: 0
Server 2 | Workloads: [5, 5] | Used: 10 | Remaining capacity: 0
Server 3 | Workloads: [4, 4] | Used: 8 | Remaining capacity: 2
Server 4 | Workloads: [4, 4] | Used: 8 | Remaining capacity: 2
Server 5 | Workloads: [4] | Used: 4 | Remaining capacity: 6

NOTE:
For this particular input, FFD uses four servers.
The assignment PDF contains an inconsistent statement
that FFD uses five servers; its corrected allocation
actually demonstrates four servers.

B4.3 - PRODUCTION DECISION
FFD sorts workloads and places each in the first
server with sufficient remaining capacity.
It avoids exhaustive search and is practical for
large workloads, but does not guarantee an optimum.
Exact search is more suitable for small instances.

=================================================================
OVERALL CONCLUSION
=================================================================
1. Graph Colouring uses backtracking and pruning.
2. Graph structure affects computational effort.
3. Exact Set Cover guarantees an optimal solution.
4. Greedy Set Cover reduces computational effort.
5. First Fit Decreasing provides practical bin packing.

All four Part B tasks completed successfully.
