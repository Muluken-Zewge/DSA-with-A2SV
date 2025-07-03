# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_graph = {e.id : e for e in employees}
        importance = 0

        def dfs(id):
            nonlocal importance
            employee = employee_graph[id]
            importance += employee.importance
            
            if len(employee.subordinates) == 0:
                return
            for sub in employee.subordinates:
                dfs(sub)
                    
        dfs(id)
        return importance
