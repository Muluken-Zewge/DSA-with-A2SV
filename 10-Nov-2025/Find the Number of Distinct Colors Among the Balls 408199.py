# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = defaultdict(int)
        colors_count = defaultdict(int)
        result = []

        for query in queries:
            ball = query[0]
            color = query[1]
        # if a ball aready exist in ball_colors,decrement it's color(delete if it become 0)
            if ball in ball_colors:
                previous_color = ball_colors[ball]
                colors_count[previous_color] -= 1
                if colors_count[previous_color] == 0:
                    del colors_count[previous_color]
        
            ball_colors[ball] = color
            colors_count[color] += 1
        # append len(colors_count) in result array
            result.append(len(colors_count))
       
        return result