
with open('a_example.txt', 'r') as f:
    B, L, D = [int(x) for x in f.readline().split()]
    BScores = [int(x) for x in f.readline().split()]
    for i in range(L):
        N, T, D = [int(x) for x in f.readline().split()]
        l = [int(x) for x in f.readline().split()]

# 6 2 7          # 6 books,2 libraries,7 days
# 1 2 3 6 5 4    # books in order
# 5 2 2          # lib 0,5 books,2days signup,2days scan
# 0 1 2 3 4      # books in lib 0
# 4 3 1          # lib 1,4 books,3days signup,1days scan
# 0 2 3 5        # books in lib 1
