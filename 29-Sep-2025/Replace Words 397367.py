# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Dict=defaultdict(int)
        for root in dictionary:
            Dict[root]=1

        res=[]
        for word in sentence.split(" "):
            for i in range(len(word)):
                temp=word[:i+1]
                found=False
                if Dict[temp]: 
                    res.append(temp)
                    found=True
                    break
            if not found: res.append(word)

        return  " ".join(res)