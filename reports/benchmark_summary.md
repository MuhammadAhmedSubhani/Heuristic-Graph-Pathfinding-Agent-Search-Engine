# Benchmark Summary

## Overview

This report compares Dijkstra's algorithm and A* Search across six grid mazes, including five reachable mazes and one maze with no valid route to its goal.

Both algorithms found shortest paths of equal length in all five reachable mazes. A* expanded fewer nodes in four of the six test cases, with the largest reduction occurring in Maze 5.

## Benchmark Results

| Maze | Shortest Path Length | Dijkstra Expanded Nodes | A* Expanded Nodes | A* Node Reduction |
| --- | ---: | ---: | ---: | ---: |
| Maze 1 - Simple | 8 | 19 | 17 | 10.53% |
| Maze 2 - More Obstacles | 8 | 19 | 19 | 0.00% |
| Maze 3 - Dense Obstacles | 8 | 18 | 16 | 11.11% |
| Maze 4 - Larger 10x10 Grid | 18 | 61 | 49 | 19.67% |
| Maze 5 - Different Layout | 8 | 15 | 11 | 26.67% |
| Maze 6 - No Path | No path | 11 | 11 | 0.00% |

## Key Findings

- **Shortest-path correctness:** A* and Dijkstra found equal-length shortest paths in all five reachable mazes.
- **Node expansion:** A* expanded fewer nodes in four of the six test cases.
- **Best reduction:** Maze 5 achieved a 26.67% reduction in expanded nodes.
- **Larger grid:** On the 10x10 Maze 4, A* expanded 49 nodes compared with 61 for Dijkstra, a 19.67% reduction.
- **Unreachable goal:** Both algorithms correctly determined that Maze 6 has no valid path.

## Methodology and Limitations

Node reduction is calculated relative to Dijkstra's expanded-node count:

`((Dijkstra nodes - A* nodes) / Dijkstra nodes) * 100`

Both algorithms use unit movement costs. A* uses Manhattan distance as its heuristic for four-directional movement.

Runtime measurements are recorded in `../results/benchmark_results.csv`. Since execution times are very small and depend on the machine and individual run, they should be treated as illustrative rather than as stable performance claims.

## Output Files

- `../results/benchmark_results.csv` — benchmark metrics for all six mazes.
- `../results/maze_4_visualization.txt` — search visualization for Maze 4.
