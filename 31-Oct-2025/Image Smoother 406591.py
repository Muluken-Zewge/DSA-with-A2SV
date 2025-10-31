# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])  
        output = [[0] * cols for _ in range(rows)] 

        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
            (0, -1),  (0, 0),  (0, 1),   # Left, Center, Right
            (1, -1),  (1, 0),  (1, 1)    # Bottom-left, Bottom, Bottom-right
        ]

        for r in range(rows):
            for c in range(cols):
                neighbors = []
                
                for dr, dc in directions:
                    ni, nj = r + dr, c + dc  
                    if 0 <= ni < rows and 0 <= nj < cols: 
                        neighbors.append(img[ni][nj])
                
                output[r][c] = sum(neighbors) // len(neighbors)
        
        return output