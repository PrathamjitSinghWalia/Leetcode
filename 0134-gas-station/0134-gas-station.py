class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tgas=0
        tcost=0
        tank=0
        start=0
        for i in range(len(gas)):
            tgas=tgas+gas[i]
            tcost=tcost + cost[i]
            tank=tank+gas[i]-cost[i]

            if tank<0:
                start=i+1
                tank=0

        if tgas>=tcost:
            return start
        else:
            return -1
        

        

        