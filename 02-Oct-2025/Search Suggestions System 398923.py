# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # store up to 3 smallest products

class Solution:
    def suggestedProducts(self, products, searchWord):
        # Sort products 
        products.sort()
        
        root = TrieNode()
        
        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestions) < 3:  # store up to 3 suggestions
                    node.suggestions.append(product)
        
        # Search prefixes of searchWord
        result = []
        node = root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])  # no suggestions if prefix not found
        
        return result
