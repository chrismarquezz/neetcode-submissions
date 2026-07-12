class CountSquares:

    def __init__(self):
        self.x_to_y = defaultdict(set)
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts[(x, y)] += 1
        self.x_to_y[x].add(y)

    def count(self, point: List[int]) -> int:
        total = 0
        qx, qy = point
        for py in self.x_to_y[qx]:
            side = abs(py - qy)
            if side == 0: continue
            for dx in (side, -side):
                total += self.pts[(qx, py)] * self.pts[(qx+dx, qy)] * self.pts[(qx+dx, py)]
        return total