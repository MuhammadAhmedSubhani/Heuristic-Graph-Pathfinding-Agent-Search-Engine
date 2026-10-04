import unittest

from src import project


class PathfindingTests(unittest.TestCase):
    def setUp(self):
        project.grid = project.mazes[0]["grid"]
        project.start = project.mazes[0]["start"]
        project.goal = project.mazes[0]["goal"]

    def test_a_star_finds_a_valid_shortest_path(self):
        distances, parents, _ = project.a_star()
        path = project.reconstruct_path(parents)

        self.assertEqual(path[0], project.start)
        self.assertEqual(path[-1], project.goal)
        self.assertEqual(len(path) - 1, distances[project.goal])
        self.assertEqual(len(path) - 1, 8)
        for current, following in zip(path, path[1:]):
            self.assertEqual(
                abs(current[0] - following[0]) + abs(current[1] - following[1]),
                1,
            )
            self.assertEqual(project.grid[following[0]][following[1]], 0)

    def test_a_star_matches_dijkstra_on_reachable_mazes(self):
        for maze in project.mazes[:5]:
            with self.subTest(maze=maze["name"]):
                project.grid = maze["grid"]
                project.start = maze["start"]
                project.goal = maze["goal"]
                dijkstra_distances, _, _ = project.dijkstra()
                a_star_distances, _, _ = project.a_star()

                self.assertEqual(
                    a_star_distances[project.goal],
                    dijkstra_distances[project.goal],
                )

    def test_both_algorithms_report_unreachable_goal(self):
        maze = project.mazes[5]
        project.grid = maze["grid"]
        project.start = maze["start"]
        project.goal = maze["goal"]

        for search in (project.dijkstra, project.a_star):
            with self.subTest(algorithm=search.__name__):
                _, parents, _ = search()
                self.assertEqual(project.reconstruct_path(parents), [])


if __name__ == "__main__":
    unittest.main()