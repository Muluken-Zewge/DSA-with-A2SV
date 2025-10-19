# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = [False] * n
        visited[id] = True
        queue = deque([(id, 0)])
        
        # Step 1: BFS to find people exactly `level` away
        level_friends = []
        while queue:
            person, dist = queue.popleft()
            if dist == level:
                level_friends.append(person)
            elif dist < level:
                for f in friends[person]:
                    if not visited[f]:
                        visited[f] = True
                        queue.append((f, dist + 1))
        
        # Step 2: Count videos from those level friends
        video_count = Counter()
        for f in level_friends:
            for v in watchedVideos[f]:
                video_count[v] += 1
        
        # Step 3: Sort by frequency, then alphabetically
        result = sorted(video_count.keys(), key=lambda x: (video_count[x], x))
        return result