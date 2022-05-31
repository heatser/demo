import unittest
from unittest.mock import Mock

from game_stats import GameStats


class TestFile(unittest.TestCase):
    """测试读最高分如文件的类"""

    def test_read_high_score(self):
        mock = Mock()
        stats = GameStats(mock)
        self.assertEqual(20375, stats.high_score)

if __name__ == "__main__":
    unittest.main()
