from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks: return 0
        # Counter-ize the tasks, how many times tasks are repeated
        task_counter = Counter(tasks).values()
        # Find out how the number of the most repeated task
        majority = max(task_counter)
        # Find out how many tasks are repeated `majority` of times
        amount_majority = list(task_counter).count(majority)
        # [A, A, A, B, B, B, C, C, D, D]
        # cooldown = 1, 2, 3, 4: cooldown <= unique(tasks) 
        # A B C D A B C D A B C D A B is the fastest way
        # cooldown = 5, ... : cooldown > unique(tasks)
        # A B C D i A B C D i A B C D i A B is the fastest way
        # 3 chunks of A B C D, and then leftover majority tasks
        return max(len(tasks), (majority - 1) * (n + 1) + amount_majority)
        
## Solution non asynchronous
#         lookup = {}
#         total_time = len(tasks)
#         for index, task in enumerate(tasks):
#             # Check if the task is still running
#             if task in lookup and index - lookup[task] < n + 1: 
#                 total_time += (n + 1) - (index - lookup[task])
            
#             # Renew task/put this task in
#             lookup[task] = index
#         return total_time
