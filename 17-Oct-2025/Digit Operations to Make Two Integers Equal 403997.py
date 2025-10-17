# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        def neighbors(num):
            s = list(str(num))
            res = []
            for i, ch in enumerate(s):
                d = int(ch)
                for nd in [d - 1, d + 1]:
                    if 0 <= nd <= 9:
                        ns = s.copy()
                        ns[i] = str(nd)
                        new_num = int("".join(ns))
                        # skip leading zeros (must have same length)
                        if len(str(new_num)) == len(s):
                            res.append(new_num)
            return res

        if is_prime(n) or is_prime(m):
            return -1

        pq = [(n, n)]  # (cost_so_far, current_number)
        dist = {n: n}

        while pq:
            cost, cur = heapq.heappop(pq)
            if cur == m:
                return cost
            if cost > dist[cur]:
                continue
            for nxt in neighbors(cur):
                if is_prime(nxt):
                    continue
                new_cost = cost + nxt
                if new_cost < dist.get(nxt, float('inf')):
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))
        return -1