# Heuristic Graph Pathfinding Agent

Compare Dijkstra's algorithm and A* on a collection of grid mazes. The project
reports shortest-path lengths, explored nodes, search-space density, and runtime,
and saves a text visualization of both searches.

## Highlights

- Six mazes, including a 10 x 10 grid and an intentionally unreachable goal.
- Four-direction movement with unit cost per step.
- A* uses Manhattan distance, an admissible heuristic for this movement model.
- Side-by-side benchmark output, CSV results, and a readable maze visualization.
- No third-party Python packages required.

## Quick Start

Requires Python 3.8 or newer.

```bash
python app.py
```

The command runs both algorithms across all mazes, prints a comparison, and
updates the generated files in `results/`. It also displays and saves the
search visualization for Maze 4.

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
Heuristic-Graph-Pathfinding-Agent-Search-Engine/
├── app.py                      
├── src/
|   ├── __init__.py
|   ├── project.py
├── tests/
|   ├── test_pathfinding.py
├── results/
|   ├── benchmark_results.csv        
|   ├── maze_4_visualization.txt 
├── reports/
|   ├── benchmark_summary.md         
├── README.md
└── LICENSE
```

## Algorithms

| Algorithm | Priority | Notes |
| --- | --- | --- |
| Dijkstra | Accumulated path cost `g(n)` | Explores by increasing distance from the start. |
| A* | `g(n) + h(n)` | Uses Manhattan distance `h(n)` to guide the search toward the goal. |

Both algorithms return shortest paths for the project's unweighted, four-way
mazes. A maze with no valid route is reported as `No path`.

## Results

The checked-in sample run found an 18-step route through Maze 4 with both
algorithms. Dijkstra expanded 61 nodes and A* expanded 49, a 19.67% reduction
for that maze. Runtime measurements are very small and vary by machine and run;
the CSV is the source for the latest recorded measurements.

Maze 6 is intentionally unsolvable. Both algorithms correctly report no path.
More detail is available in [`reports/benchmark_summary.md`](reports/benchmark_summary.md).

## Visualization Legend

| Symbol | Meaning |
| --- | --- |
| `S` | Start |
| `G` | Goal |
| `#` | Obstacle |
| `*` | Selected shortest path |
| `E` | Expanded search node |
| `.` | Unvisited walkable cell |

The visualization gives the final path precedence over expanded-node markers.