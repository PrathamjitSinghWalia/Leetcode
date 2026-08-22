import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        heap = []

        # Create max heap using negative frequencies
        for task, freq in count.items():
            heapq.heappush(heap, (-freq, task))

        time = 0

        while heap:

            temp = []

            # One cycle has n + 1 slots
            for i in range(n + 1):

                if heap:
                    freq, task = heapq.heappop(heap)

                    # One occurrence of this task is completed
                    freq += 1

                    # Task still has occurrences remaining
                    if freq < 0:
                        temp.append((freq, task))

                    time += 1

                elif temp:
                    # No task available, so CPU is idle
                    time += 1

            # Put unfinished tasks back into heap
            for item in temp:
                heapq.heappush(heap, item)

        return time