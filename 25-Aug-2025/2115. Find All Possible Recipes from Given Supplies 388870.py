# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {}


        for r, ing_list in zip(recipes, ingredients):
            indegree[r] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(r)


        queue = deque(supplies)
        result = []


        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)


        return result
        