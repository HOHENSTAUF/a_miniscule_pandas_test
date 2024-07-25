import unittest
import drawing
import pandas as pd

class TestDrawing(unittest.TestCase):
    
    def test_split(self):
        #checks that function is working on normal input
        df = pd.read_json("./data/deviations.json")
        test_result = ['./corners_histogram',
                       './deviations histograms for 4 corners.png',
                       './deviations histograms for 8 corners.png',
                       './deviations histograms for 6 corners.png',
                       './deviations histograms for 10 corners.png'
                       ]
        result = drawing.drawing_plots.draw_plots(df)
        self.assertEqual(result, test_result)
        #checks that function is producing type error on wrong input
        with self.assertRaises(TypeError):
            drawing.drawing_plots.draw_plots()


if __name__ == '__main__':
    unittest.main()
