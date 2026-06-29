# Brute force solution

# def findSmallestSubstringWindow(patterns: list[str], S: str) -> list[int]:
#     n = len(S)
#     best = None
#     pats = set(patterns)
#     for l in range(n):
#         for r in range(l, n):
#             window = S[l:r+1]
#             if all(pat in window for pat in pats):
#                 if best is None or (r - l) < (best[1] - best[0]):
#                     best = [l, r]
    
#     return best if best else [-1, -1]

