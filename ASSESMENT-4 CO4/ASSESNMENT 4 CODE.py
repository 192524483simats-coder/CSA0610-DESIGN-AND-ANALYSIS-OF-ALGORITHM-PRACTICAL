
# Cloud Release Budget Planner
# Greedy Algorithm + Dynamic Programming (0/1 Knapsack)

# Read input
n, W = map(int, input().split())

features = []

for i in range(n):
    name, cost, value = input().split()
    features.append((name, int(cost), int(value)))

# ---------------- GREEDY ALGORITHM ----------------

# Sort by decreasing value-to-cost ratio
order = sorted(
    range(n),
    key=lambda i: (-features[i][2] / features[i][1], i)
)

greedy_value = 0
remaining = W

for i in order:
    name, cost, value = features[i]

    if cost <= remaining:
        greedy_value += value
        remaining -= cost

# ---------------- DYNAMIC PROGRAMMING ----------------

dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    name, cost, value = features[i - 1]

    for w in range(W + 1):

        # Do not select the feature
        dp[i][w] = dp[i - 1][w]

        # Select the feature if it fits
        if cost <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - cost] + value
            )

# ---------------- FIND MAXIMUM VALUE ----------------

max_value = dp[n][W]

# Find smallest budget achieving maximum value
budget = 0

for w in range(W + 1):
    if dp[n][w] == max_value:
        budget = w
        break

# ---------------- BACKTRACKING ----------------

selected = [False] * n
w = budget

for i in range(n, 0, -1):

    if dp[i][w] != dp[i - 1][w]:
        selected[i - 1] = True
        w -= features[i - 1][1]

# ---------------- FINAL OUTPUT ----------------

print("Greedy Value =", greedy_value)
print("Maximum Value =", max_value)

chosen = []
budget_used = 0

for i in range(n):
    if selected[i]:
        chosen.append(features[i][0])
        budget_used += features[i][1]

print("Selected =", " ".join(chosen) if chosen else "NONE")
print("Budget Used =", budget_used)
