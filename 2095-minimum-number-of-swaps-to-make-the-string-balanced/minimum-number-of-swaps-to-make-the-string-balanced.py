class Solution:
    def minSwaps(self, s: str) -> int:
        closing = 0
        maxClose = 0

        for c in s:
            if c == '[':
                closing -= 1
            else:
                closing += 1
            maxClose = max(maxClose,closing)

        return (maxClose + 1)//2
        