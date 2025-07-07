# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = deque()
        queue.append(0)
        visited = [False for _ in range(n)]
        visited[0] = True

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if visited[key] == False and key != room:
                    visited[key] = True
                    queue.append(key)
                    
        return all(visited[i] == True for i in range(n))
            