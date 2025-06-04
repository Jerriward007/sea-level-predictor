# test_module.py

import unittest
import sea_level_predictor
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot_exists(self):
        fig = sea_level_predictor.draw_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure, "The returned object is not a matplotlib Figure.")

    def test_plot_axes_labels(self):
        fig = sea_level_predictor.draw_plot()
        ax = fig.axes[0]
        self.assertEqual(ax.get_xlabel(), "Year", "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), "Sea Level (inches)", "Y-axis label is incorrect.")
        self.assertEqual(ax.get_title(), "Rise in Sea Level", "Plot title is incorrect.")

if __name__ == "__main__":
    unittest.main()
