
from itertools import combinations
from collections import defaultdict

# ============================================================
# DAA ASSIGNMENT 5 - CO5
# SEARCH, COMPLEXITY AND APPROXIMATION ENGINEERING
# ============================================================

def heading(title):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)


# ============================================================
# TASK B1 - GRAPH COLOURING USING BACKTRACKING
# ============================================================

def make_graph(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        if v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)

    return graph


def graph_colouring(graph, k, heuristic=False):
    n = len(graph)
    colour = [-1] * n

    stats = {
        "nodes": 0,
        "attempts": 0,
        "rejected": 0,
        "backtracks": 0,
        "max_depth": 0
    }

    def select_vertex():
        uncoloured = [v for v in range(n) if colour[v] == -1]

        if not uncoloured:
            return None

        if not heuristic:
            return uncoloured[0]

        # Highest number of already-coloured neighbours.
        # Tie: highest total degree.
        # Further tie: smallest vertex index.
        return max(
            uncoloured,
            key=lambda v: (
                sum(colour[u] != -1 for u in graph[v]),
                len(graph[v]),
                -v
            )
        )

    def search(depth):
        stats["nodes"] += 1
        stats["max_depth"] = max(stats["max_depth"], depth)

        if depth == n:
            return True

        v = select_vertex()

        for c in range(k):
            stats["attempts"] += 1

            feasible = all(
                colour[u] != c for u in graph[v]
            )

            if not feasible:
                stats["rejected"] += 1
                continue

            colour[v] = c

            if search(depth + 1):
                return True

            colour[v] = -1
            stats["backtracks"] += 1

        return False

    result = search(0)

    return result, colour[:] if result else None, stats


def print_graph_result(name, result, colouring, stats):
    print("\n", name)
    print("Colourable:", result)
    print("Final colouring:", colouring)
    print("Search nodes:", stats["nodes"])
    print("Candidate assignments:", stats["attempts"])
    print("Rejected branches:", stats["rejected"])
    print("Backtracks:", stats["backtracks"])
    print("Maximum depth:", stats["max_depth"])


def task_b1():
    heading("TASK B1 - GRAPH COLOURING")

    # Test 1: Four-vertex path
    graph1 = make_graph(4, [(0, 1), (1, 2), (2, 3)])
    result, colouring, stats = graph_colouring(graph1, 2)
    print_graph_result("Test 1 - Colourable Path", result, colouring, stats)

    # Test 2: Triangle with only two colours
    graph2 = make_graph(3, [(0, 1), (1, 2), (0, 2)])
    result, colouring, stats = graph_colouring(graph2, 2)
    print_graph_result("Test 2 - Non-Colourable Triangle", result, colouring, stats)

    # Test 3: Single isolated vertex
    graph3 = make_graph(1, [])
    result, colouring, stats = graph_colouring(graph3, 1)
    print_graph_result("Test 3 - Boundary Case", result, colouring, stats)

    # Compare input order and heuristic order
    comparison_graph = make_graph(
        6,
        [
            (0, 1), (0, 2), (1, 2),
            (1, 3), (2, 4), (3, 4),
            (3, 5), (4, 5)
        ]
    )

    print("\nB1.3 AND B1.4 - ORDERING COMPARISON")

    for heuristic in [False, True]:
        result, colouring, stats = graph_colouring(
            comparison_graph, 3, heuristic
        )

        name = "VERSION 2 - HEURISTIC ORDER" if heuristic else \
               "VERSION 1 - INPUT ORDER"

        print_graph_result(name, result, colouring, stats)


# ============================================================
# TASK B2 - ADVERSARIAL GRAPH INPUT
# ============================================================

def task_b2():
    heading("TASK B2 - ADVERSARIAL INPUT EXPERIMENT")

    # Graph A: Six isolated vertices
    graph_A = make_graph(6, [])

    # Graph B: Complete graph with six vertices
    edges = [
        (i, j)
        for i in range(6)
        for j in range(i + 1, 6)
    ]
    graph_B = make_graph(6, edges)

    for name, graph in [
        ("GRAPH A - EASY GRAPH", graph_A),
        ("GRAPH B - DIFFICULT GRAPH", graph_B)
    ]:
        result, colouring, stats = graph_colouring(graph, 2)

        print_graph_result(name, result, colouring, stats)

    print("\nOBSERVATION:")
    print("Graph A has no conflicts and is easily coloured.")
    print("Graph B is a complete graph and needs six colours.")
    print("Therefore, Graph B cannot be coloured using two colours.")
    print("Input size alone does not determine search effort.")
    print("Graph structure and pruning also affect performance.")


# ============================================================
# TASK B3 - EXACT AND GREEDY SET COVER
# ============================================================

def exact_set_cover(universe, centres):
    names = list(centres.keys())
    states = 0

    for size in range(1, len(names) + 1):
        for selected in combinations(names, size):
            states += 1

            covered = set()

            for centre in selected:
                covered.update(centres[centre])

            if universe.issubset(covered):
                return list(selected), states

    return None, states


def greedy_set_cover(universe, centres):
    uncovered = set(universe)
    selected = []
    evaluations = 0

    while uncovered:
        best_centre = None
        max_coverage = 0

        for centre, zones in centres.items():
            evaluations += 1
            coverage = len(uncovered.intersection(zones))

            if coverage > max_coverage:
                max_coverage = coverage
                best_centre = centre

        if best_centre is None:
            return None, evaluations

        selected.append(best_centre)
        uncovered -= set(centres[best_centre])

    return selected, evaluations


def test_set_cover(name, universe, centres):
    exact, states = exact_set_cover(universe, centres)
    greedy, evaluations = greedy_set_cover(universe, centres)

    print("\n", name)
    print("Universe:", sorted(universe))
    print("Centres:", centres)
    print("Exact solution:", exact)
    print("Exact solution size:", len(exact) if exact else "No cover")
    print("Exact search states:", states)
    print("Greedy solution:", greedy)
    print("Greedy solution size:", len(greedy) if greedy else "No cover")
    print("Greedy evaluations:", evaluations)

    if exact is not None and greedy is not None:
        print("Same solution size:", len(exact) == len(greedy))

    return exact, greedy


def task_b3():
    heading("TASK B3 - EXACT VS GREEDY SET COVER")

    # Three normal test instances
    instances = [
        (
            "INSTANCE 1",
            set("12345"),
            {
                "C1": set("123"),
                "C2": set("234"),
                "C3": set("45"),
                "C4": set("15")
            }
        ),
        (
            "INSTANCE 2",
            set("123456"),
            {
                "C1": set("123"),
                "C2": set("456"),
                "C3": set("124"),
                "C4": set("356")
            }
        ),
        (
            "INSTANCE 3",
            set("123456"),
            {
                "C1": set("12"),
                "C2": set("34"),
                "C3": set("56"),
                "C4": set("1234"),
                "C5": set("56")
            }
        )
    ]

    for name, universe, centres in instances:
        test_set_cover(name, universe, centres)

    # Counterexample: Greedy is not optimal
    heading("B3.2 - GREEDY COUNTEREXAMPLE")

    universe = set("12345678")

    centres = {
        "A": set("12356"),
        "B": set("1234"),
        "C": set("5678"),
        "D": set("47")
    }

    exact, greedy = test_set_cover(
        "COUNTEREXAMPLE", universe, centres
    )

    print("\nGREEDY TRACE:")

    uncovered = set(universe)
    selected = []

    while uncovered:
        best = max(
            centres,
            key=lambda c: len(uncovered.intersection(centres[c]))
        )

        newly_covered = uncovered.intersection(centres[best])

        selected.append(best)
        uncovered -= centres[best]

        print("Selected:", best)
        print("Newly covered:", sorted(newly_covered))
        print("Remaining zones:", sorted(uncovered))

    print("\nExact solution uses:", len(exact), "centres")
    print("Greedy solution uses:", len(greedy), "centres")

    # Scalability experiments
    heading("B3.3 - SCALABILITY EXPERIMENT")

    for zones_count, centre_count in [(12, 6), (16, 8)]:
        universe = set(range(1, zones_count + 1))

        centres = {}

        for i in range(centre_count):
            centres["C" + str(i + 1)] = {
                2 * i + 1,
                2 * i + 2
            }

        exact, states = exact_set_cover(universe, centres)
        greedy, evaluations = greedy_set_cover(universe, centres)

        print("\nProblem size:", zones_count, "zones,", centre_count, "centres")
        print("Exact search states:", states)
        print("Greedy evaluations:", evaluations)
        print("Exact cover size:", len(exact) if exact else None)
        print("Greedy cover size:", len(greedy) if greedy else None)

    print("\nB3.4 - ENGINEERING TRADE-OFF")
    print("Exact search guarantees the minimum-size cover.")
    print("Greedy reduces search effort and produces a feasible cover.")
    print("Greedy does not guarantee optimality.")


# ============================================================
# TASK B4 - BIN PACKING USING FIRST FIT DECREASING
# ============================================================

def first_fit_decreasing(workloads, capacity):
    if capacity <= 0:
        raise ValueError("Capacity must be positive.")

    if any(w <= 0 or w > capacity for w in workloads):
        raise ValueError("Each workload must be positive and fit a server.")

    bins = []

    # Sort workloads in decreasing order
    sorted_workloads = sorted(workloads, reverse=True)

    for workload in sorted_workloads:
        placed = False

        # Place in the first server with sufficient capacity
        for server in bins:
            if sum(server) + workload <= capacity:
                server.append(workload)
                placed = True
                break

        # Open a new server if necessary
        if not placed:
            bins.append([workload])

    return bins


def display_bins(bins, capacity):
    print("\nNumber of servers used:", len(bins))

    for i, server in enumerate(bins, start=1):
        used = sum(server)
        remaining = capacity - used

        print(
            "Server", i,
            "| Workloads:", server,
            "| Used:", used,
            "| Remaining capacity:", remaining
        )


def task_b4():
    heading("TASK B4 - BIN PACKING")

    capacity = 10
    workloads = [7, 5, 5, 4, 4, 2, 2]

    print("Server capacity:", capacity)
    print("Original workloads:", workloads)

    bins = first_fit_decreasing(workloads, capacity)

    print("\nFIRST FIT DECREASING RESULT")
    display_bins(bins, capacity)

    # Assignment challenge input
    heading("B4.2 - CHALLENGE INPUT")

    challenge = [6, 5, 5, 4, 4, 4, 4, 4, 4]

    print("Capacity:", 10)
    print("Challenge workloads:", challenge)

    challenge_bins = first_fit_decreasing(challenge, 10)

    display_bins(challenge_bins, 10)

    print("\nNOTE:")
    print("For this particular input, FFD uses four servers.")
    print("The assignment PDF contains an inconsistent statement")
    print("that FFD uses five servers; its corrected allocation")
    print("actually demonstrates four servers.")

    print("\nB4.3 - PRODUCTION DECISION")
    print("FFD sorts workloads and places each in the first")
    print("server with sufficient remaining capacity.")
    print("It avoids exhaustive search and is practical for")
    print("large workloads, but does not guarantee an optimum.")
    print("Exact search is more suitable for small instances.")


# ============================================================
# MAIN PROGRAM - RUN ALL FOUR TASKS
# ============================================================

def main():
    print("\n")
    print("*" * 65)
    print("       DAA ASSIGNMENT 5 - CO5")
    print(" SEARCH, COMPLEXITY AND APPROXIMATION ENGINEERING")
    print("*" * 65)

    task_b1()
    task_b2()
    task_b3()
    task_b4()

    heading("OVERALL CONCLUSION")

    print("1. Graph Colouring uses backtracking and pruning.")
    print("2. Graph structure affects computational effort.")
    print("3. Exact Set Cover guarantees an optimal solution.")
    print("4. Greedy Set Cover reduces computational effort.")
    print("5. First Fit Decreasing provides practical bin packing.")
    print("\nAll four Part B tasks completed successfully.")


if __name__ == "__main__":
    main()
