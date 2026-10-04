# Benchmark Summary

The checked-in CSV is a sample run of Dijkstra and A* across five reachable
mazes and one maze with no route to its goal. Both algorithms found paths of
equal length in every reachable maze, as expected for these unit-cost grids.

| Maze | Shortest path | Dijkstra nodes | A* nodes | A* node reduction |
| --- | ---: | ---: | ---: | ---: |
| Maze 1 - Simple | 8 | 19 | 17 | 10.53% |
| Maze 2 - More Obstacles | 8 | 19 | 19 | 0.00% |
| Maze 3 - Dense Obstacles | 8 | 18 | 16 | 11.11% |
| Maze 4 - Larger 10x10 Grid | 18 | 61 | 49 | 19.67% |
| Maze 5 - Different Layout | 8 | 15 | 11 | 26.67% |
| Maze 6 - No Path | None | 11 | 11 | 0.00% |

Node reduction is calculated relative to Dijkstra's expanded-node count. Search
runtime values are recorded in `../results/benchmark_results.csv`, but are
machine- and run-dependent; they should be treated as illustrative rather than
as a stable performance claim.