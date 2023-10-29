import numpy as np


class Result:
    def __init__(self, positions, substrate):
        self.positions_sorted = np.array(sorted(positions, key=lambda item: item[0], reverse=True))
        self.frame = substrate.rows, substrate.cols

    def get_2d_result(self):
        num_gc = len(self.positions_sorted[:, 0])
        pseudo_y = np.linspace(0, self.frame[1], num_gc)
        return self.positions_sorted[:, 0], pseudo_y

    def __str__(self):
        return f"Final Positions (sorted by X):\n{self.positions_sorted}"

