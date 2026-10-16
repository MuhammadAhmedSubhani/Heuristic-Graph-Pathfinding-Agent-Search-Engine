# Heuristic Graph Pathfinding Agent

A lightweight Python project that compares Dijkstra's algorithm and A* on a set of grid mazes, highlighting path cost, explored nodes, efficiency, and runtime behavior.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/Algorithms-Dijkstra%20%2B%20A*-%234B8BBE?style=for-the-badge" alt="Algorithms" />
</p>

## Live Preview

Try the app in the browser here:

[Heuristic Graph Pathfinding Agent Live Preview](https://heuristic-graph-pathfinding-agent-search.onrender.com)

## Why this project?

This project is designed to make pathfinding behavior easy to compare visually and numerically. It evaluates how each algorithm:

- finds the shortest valid route,
- expands different numbers of nodes,
- trades off speed and efficiency,
- handles unreachable goals and obstacle-heavy maps.

## Highlights

- Six mazes, including a 10x10 grid and an intentionally unsolvable goal.
- Four-direction movement with unit cost per step.
- A* uses Manhattan distance as an admissible heuristic for this movement model.
- Side-by-side performance benchmark output and CSV-based result tracking.
- Maze visualization saved as plain-text output for easy inspection.
- No third-party Python dependencies required.

## Quick Start

Requires Python 3.8 or newer.

```bash
python app.py
```

This runs both algorithms across all mazes, prints a comparison summary, and updates the generated files in `results/`. It also displays and saves the search visualization for Maze 4.

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
Heuristic-Graph-Pathfinding-Agent-Search-Engine/
├── app.py
├── src/
│   ├── __init__.py
│   ├── project.py
├── tests/
│   ├── test_pathfinding.py
├── results/
│   ├── benchmark_results.csv
│   ├── maze_4_visualization.txt
├── reports/
│   ├── benchmark_summary.md
│   ├── Task 3 Final Report.pdf  
├── README.md
├── LICENSE
└── .gitignore
```

## Algorithm Comparison

| Algorithm | Priority Function | Notes |
| --- | --- | --- |
| Dijkstra | `g(n)` | Expands nodes by accumulated path cost from the start. |
| A* | `g(n) + h(n)` | Uses Manhattan distance `h(n)` to head toward the goal efficiently. |

Both algorithms return shortest paths for the project's unweighted, four-way mazes. A maze with no valid route is reported as `No path`.

## Sample Results

A representative sample run found an 18-step route through Maze 4 with both algorithms.

- Dijkstra expanded 61 nodes.
- A* expanded 49 nodes.
- A* achieved a ~19.67% reduction in explored nodes for that maze.

Runtime varies by machine and execution conditions, so the CSV file remains the authoritative record of the latest metrics.

Maze 6 is intentionally unsolvable, and both algorithms correctly report no path.
More detailed information is available in [reports/benchmark_summary.md](reports/benchmark_summary.md).

## Visualization Legend

| Symbol | Meaning |
| --- | --- |
| `S` | Start |
| `G` | Goal |
| `#` | Obstacle |
| `*` | Selected shortest path |
| `E` | Expanded search node |
| `.` | Unvisited walkable cell |

The maze visualization prioritizes the final shortest path, while expanded nodes are marked separately to keep the search pattern readable.

## License

This project is distributed under the terms of the included [LICENSE](LICENSE).