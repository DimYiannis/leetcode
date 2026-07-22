# Assignment name  : py_package_dependency_resolver
# Expected files   : py_package_dependency_resolver.py
# Allowed functions: None
# --------------------------------------------------------------------------------

# Write a function that determines a valid package installation order by resolving
# dependencies. Use topological sorting to ensure dependencies are installed before
# the packages that require them.

# Your function must be declared as follows:

# def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

# The function should:
# - Take a dictionary where keys are package names and values are lists of dependencies
# - Return packages in installation order (dependencies first)
# - Return empty list if no valid order exists (circular dependencies)
# - Handle empty input and isolated dependency chains
# - Ignore references to packages not in the input dictionary

# Algorithm requirements:
# - Use topological sorting (e.g., Kahn's algorithm)
# - Process packages with no remaining dependencies first
# - Ensure deterministic output when multiple valid orders exist

# Examples:

# Input: package_dependency_resolver({
#     "app": ["database"],
#     "database": ["driver"],
#     "driver": []
# })
# Output: ["driver", "database", "app"]
# # Dependencies: driver → database → app

# Input: package_dependency_resolver({
#     "A": [],
#     "B": ["A"],
#     "C": ["A", "B"]
# })
# Output: ["A", "B", "C"]
# # A has no deps, B needs A, C needs both A and B

# Input: package_dependency_resolver({})
# Output: []
# # Empty input

# Input: package_dependency_resolver({
#     "X": ["Y"],
#     "Y": ["X"]
# })
# Output: []
# # Circular dependency: X needs Y, Y needs X

# Input: package_dependency_resolver({
#     "web": [],
#     "api": [],
#     "frontend": ["web"],
#     "backend": ["api"]
# })
# Output: ["api", "web", "backend", "frontend"]
# # Two independent chains: api→backend and web→frontend

# Edge cases to handle:
# - Empty input: return empty list
# - Packages with no dependencies: include in output first
# - Multiple independent chains: process all chains
# - Circular dependencies: return empty list
# - Non-existent dependencies: ignore missing packages
# - Self-dependencies: return empty list

# Notes:
# - For deterministic output, process packages alphabetically when choices exist
# - A package cannot be installed until all its dependencies are installed
# - If any circular dependency exists, no valid installation order is possible

# Testing example:
# python3 main.py '{"app": ["database"], "database": ["driver"], "driver": []}'
# # Expected output: driver database app

# import json
# packages = json.loads('{"app": ["database"], "database": ["driver"], "driver": []}')
# result = package_dependency_resolver(packages)
# print(' '.join(result))  # Output: driver database app

'''
1.Find packages that require nothing and put them in a queue.
2.Take a ready package, add it to the result.
3.Check every package to see which ones depended on it.
4.Reduce their remaining dependency count.
5.If a package reaches zero remaining dependencies, add it to the queue.
6.Repeat until everything is processed or no packages remain.
'''

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    # removes dependencies that don't exist
    deps = {}
    for name, dependencies in packages.items():
        deps[name] = [d for d in dependencies if d in packages]

    # how many dependencies are still blocking this package
    in_degree = {name: len(d) for name, d in deps.items()}

    # only packages with no remaining dependencies can be installed.
    queue = sorted(name for name, deg in in_degree.items() if deg == 0)
    result = []

    # BFS level by level (each alphabetical "wave" before the next one)
    while queue:
        next_queue = []
        for current in queue:
            result.append(current)
            for name, dependencies in deps.items():
                if current in dependencies:
                    in_degree[name] -= 1
                    if in_degree[name] == 0:
                        next_queue.append(name)
        queue = sorted(next_queue)

    # Cycle detected? len(result) != len(packages)
    if len(result) != len(packages):
        return []
    return result


# res = package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})
# print(f"excepted: ["driver", "database", "app"]")
# print(f"got: {res}\n")

# res = package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})
# print(f"excepted: ["A", "B", "C"]")
# print(f"got: {res}\n")

# res = package_dependency_resolver({"X": ["Y"], "Y": ["X"]})
# print(f"excepted: []")
# print(f"got: {res}\n")

# res = package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})
# print(f"excepted: ["api", "web", "backend", "frontend"]")
# print(f"got: {res}\n")



# Description of the Kahn's algorithm

# Kahn’s algorithm is a well-known approach for computing a topological ordering of a directed
# acyclic graph (DAG). The main idea is to process the graph by always selecting nodes that have
# no incoming edges, which means they do not depend on any other nodes. At the beginning, the
# algorithm computes the in-degree of each node, defined as the number of edges entering that
# node. All nodes with an in-degree of zero are placed into a queue or set. The algorithm then
# repeatedly removes one node from this set, appends it to the topological order, and removes all
# of its outgoing edges from the graph. When an outgoing edge is removed, the in-degree of the
# destination node is decreased; if this in-degree becomes zero, the node is added to the set.
# The algorithm continues until there are no nodes left to process. If all nodes are included in
# the result, the graph is acyclic and the ordering is valid; otherwise, the presence of remaining
# edges indicates a cycle.