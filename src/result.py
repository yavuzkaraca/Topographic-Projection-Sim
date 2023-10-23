import numpy as np

class Result:
    def __init__(self, positions, substrate):
        self.positions = np.array(sorted(positions, key=lambda item: item[0], reverse=True))
        self.frame = substrate.rows, substrate.cols

    def get_2d_result(self):
        return self.positions[:, 0], self.positions[:, 1]


