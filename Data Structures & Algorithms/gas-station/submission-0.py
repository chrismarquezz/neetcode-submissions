class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_tank = 0
        total_gas = 0
        start = 0

        for i in range(len(gas)):
            curr_tank += (gas[i] - cost[i])
            total_gas += (gas[i] - cost[i])
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        
        return start if total_gas >= 0 else -1