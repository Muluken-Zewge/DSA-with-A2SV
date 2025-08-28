# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Step 1: Assign unique groups to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Graphs
        item_graph = defaultdict(list)
        group_graph = defaultdict(list)
        item_indegree = [0] * n
        group_indegree = [0] * m

        # Step 2: Build dependency graphs
        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indegree[v] += 1
                if group[v] != group[u]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        # Step 3: Topo sort helper
        def topo_sort(nodes, graph, indegree):
            q = deque([x for x in nodes if indegree[x] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return order if len(order) == len(nodes) else []

        # Step 4: Sort items and groups
        item_order = topo_sort(range(n), item_graph, item_indegree)
        if not item_order:
            return []
        group_order = topo_sort(range(m), group_graph, group_indegree)
        if not group_order:
            return []

        # Step 5: Collect items by group in item_order
        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        # Step 6: Merge group order with item order
        res = []
        for g in group_order:
            res.extend(ordered_groups[g])

        return res

        