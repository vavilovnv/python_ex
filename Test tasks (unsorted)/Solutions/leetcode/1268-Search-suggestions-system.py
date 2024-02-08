"""
https://leetcode.com/problems/search-suggestions-system/

Category - Medium

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after
each character of searchWord is typed. Suggested products should have common
prefix with searchWord. If there are more than three products with a common
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of
searchWord is typed.
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, p_len = [], len(products)
        ind = [i for i in range(p_len)]
        for _i, c in enumerate(searchWord):
            temp = []
            for i in ind:
                if len(products[i]) > _i and products[i][_i] == c:
                    temp.append(i)
            res.append(products[i] for i in temp[:3])        
            ind = temp
        return res
