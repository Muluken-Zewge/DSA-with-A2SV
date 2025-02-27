# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')

            return f"{name[0]}*****{name[-1]}@{domain}"

        else:
            digits = "".join([char for char in s if char.isdigit()])
            local_number = digits[-10:]
            country_code = len(digits) - 10

            if country_code == 0:
                return f"***-***-{digits[-4:]}"
            elif country_code == 1:
                return f"+*-***-***-{digits[-4:]}"
            elif country_code == 2:
                return f"+**-***-***-{digits[-4:]}"
            else:
                return f"+***-***-***-{digits[-4:]}"