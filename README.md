# Heuristic Graph Pathfinding Agent Search Engine

## Live Preview

Try the app in the browser here:

[Heuristic Graph Pathfinding Agent Live Preview](https://heuristic-graph-pathfinding-agent-search.onrender.com)

##

A Python-based pathfinding project that compares **A\* Search** and **Dijkstra's algorithm** across grid mazes. It measures path lengths, expanded nodes, node-expansion density, and runtime, and exports benchmark results and a text visualization.

## Project Objectives

- Implement A\* Search and Dijkstra's algorithm from scratch.
- Find shortest paths through grid mazes while avoiding obstacles.
- Compare algorithm behavior across different maze layouts.
- Record metrics including path length, expanded nodes, expansion density, and runtime.
- Export benchmark results and a maze visualization log.
- Test reachable and unreachable goal scenarios.

## Algorithms

### Dijkstra's Algorithm

Dijkstra's algorithm explores the frontier node with the lowest known cost from the start. With non-negative edge costs, it finds a shortest path when a route exists.

### A\* Search

A\* prioritizes nodes using:

`f(n) = g(n) + h(n)`

Where:
- `g(n)` is the cost from the start to node `n`.
- `h(n)` is the estimated cost from node `n` to the goal.

This project uses **Manhattan distance** for four-directional grid movement:

`h(n) = |x_goal - x_n| + |y_goal - y_n|`

Movement is limited to up, down, left, and right, with a cost of `1` per move.

## Benchmark Results

The project evaluates six maze layouts, including five reachable mazes and one maze with no valid route.

| Maze | Shortest Path Length | Dijkstra Expanded Nodes | A\* Expanded Nodes | A\* Node Reduction |
|---|---:|---:|---:|---:|
| Maze 1 — Simple | 8 | 19 | 17 | 10.53% |
| Maze 2 — More Obstacles | 8 | 19 | 19 | 0.00% |
| Maze 3 — Dense Obstacles | 8 | 18 | 16 | 11.11% |
| Maze 4 — Larger 10×10 Grid | 18 | 61 | 49 | 19.67% |
| Maze 5 — Different Layout | 8 | 15 | 11 | 26.67% |
| Maze 6 — No Path | No path | 11 | 11 | 0.00% |

### Key Findings

- A\* and Dijkstra found equal-length shortest paths in all five reachable mazes.
- A\* expanded fewer nodes in four of the six test cases.
- The largest reduction in expanded nodes was **26.67%** in Maze 5.
- In the larger 10×10 Maze 4, A\* expanded 49 nodes compared with 61 for Dijkstra.
- Both algorithms correctly identified the unreachable goal in Maze 6.

Runtime measurements are included in the CSV output. Since the searches are very small, runtime can vary with machine load and measurement overhead; treat it as illustrative rather than a stable performance claim.

## Project Structure

```text
Heuristic-Graph-Pathfinding-Agent-Search-Engine/
├── app.py
├── src/
│   ├── __init__.py
│   └── project.py
├── tests/
│   └── test_pathfinding.py
├── results/
│   ├── benchmark_results.csv
│   └── maze_4_visualization.txt
├── reports/
│   └── benchmark_summary.md
├── README.md
├── LICENSE
└── .gitignore
```

## Requirements

- Python 3
- No external third-party package is required for the core algorithms if the project uses only Python standard-library modules.

The code uses Python modules such as `heapq` for priority queues and `time.perf_counter` for runtime measurement. The automated tests use `unittest`.

## Setup and Run

### 1. Clone the repository

```bash
git clone https://github.com/MuhammadAhmedSubhani/Heuristic-Graph-Pathfinding-Agent-Search-Engine.git
cd Heuristic-Graph-Pathfinding-Agent-Search-Engine
```

### 2. Run the project

If Python is available on your system:

```bash
python app.py
```

On Windows, if the `python` command is not available, activate or use the Python environment configured on your machine. For example, from the repository folder, if the environment is in the parent folder:

```powershell
& "..\.venv\Scripts\python.exe" app.py
```

The application runs the benchmark and generates or updates the project output files according to the implementation in `app.py`.

## Run Automated Tests

Run the test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

If using the virtual environment located in the parent folder on Windows:

```powershell
& "..\.venv\Scripts\python.exe" -m unittest discover -s tests -v
```

### Verified Test Results

The latest test run reported **3 tests passed**:

- `test_a_star_finds_a_valid_shortest_path`
- `test_a_star_matches_dijkstra_on_reachable_mazes`
- `test_both_algorithms_report_unreachable_goal`

## Output Files

| File | Description |
|---|---|
| `results/benchmark_results.csv` | Benchmark metrics for the six maze cases, including paths, expanded nodes, expansion density, runtime, and node reduction. |
| `results/maze_4_visualization.txt` | Text-based search visualization for Maze 4. |
| `reports/benchmark_summary.md` | Summary of benchmark methodology, results, and key findings. |

## Metrics

### Expanded-Node Reduction

The relative reduction in expanded nodes is calculated against Dijkstra's expanded-node count:

```text
((Dijkstra expanded nodes - A* expanded nodes) / Dijkstra expanded nodes) * 100
```

### Path Length

Path length is the number of moves in the returned route. Since each move has a cost of `1`, the path length is also the total route cost.

### Expansion Density and Runtime

Expansion density and runtime are recorded by the project in the benchmark CSV. Runtime is sensitive to system load and measurement noise, especially for small mazes.

## Limitations and Future Improvements

- The experiments use six fixed maze layouts; more randomized and larger mazes could provide broader evaluation.
- The current movement model supports four directions and uniform movement costs.
- Runtime comparisons could be strengthened by running repeated trials and reporting averages and variation.
- Future versions could include weighted terrain, configurable start/goal positions, and richer visualizations.

## Technologies Used

- **Language:** Python
- **Search algorithms:** A\* Search, Dijkstra's algorithm
- **Priority queue:** `heapq`
- **Runtime measurement:** `time.perf_counter`
- **Testing:** `unittest`
- **Output formats:** CSV and text
- **Version control:** Git and GitHub

## Author

**Muhammad Ahmed Subhani**

## Repository

[GitHub Repository](https://github.com/MuhammadAhmedSubhani/Heuristic-Graph-Pathfinding-Agent-Search-Engine)

## License

See the [`LICENSE`](LICENSE) file for license details.
