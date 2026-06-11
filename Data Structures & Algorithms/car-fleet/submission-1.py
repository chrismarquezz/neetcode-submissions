class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(cars, key = lambda x: -x[0])
        times = [(target - p) / s for p, s in cars]
        stack = []
        for t in times:
            if stack and t <= stack[-1]:
                continue
            stack.append(t) 
        return len(stack)
