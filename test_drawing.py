import unittest
import drawing

class TestDrawing(unittest.TestCase):
    
    def test_draw_plots():
        df = pd.read_json("./data/deviations.json")
        result = drawing.drawing_plots.draw_plots(df)
        test_result = ['./corners_histogram',
                       './deviations histograms for 4 corners.png',
                       './deviations histograms for 8 corners.png',
                       './deviations histograms for 6 corners.png',
                       './deviations histograms for 10 corners.png'
                       ]
        self.assertEqual(result, test_result)

if __name__ == '__main__':
    unittest.main()
