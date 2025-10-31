# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        output = []
        for domain in cpdomains:
            visits, dom = domain.split()
            # split the sub domains and store them in a dictionary(key=domain, value=visits)
            counter[dom] += int(visits)
            i = dom.find('.',0)
            while i != -1:
                counter[dom[i+1:]] += int(visits)
                i = dom.find('.',i+1)
        # iterate over the dictonary and store the result in an array
        for domain, visits in counter.items():
            formated = f"{visits} {domain}"
            output.append(formated)
        
        return output