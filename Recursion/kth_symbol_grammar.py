"""
For the given N and K, return 1 or 0 for the grammar --> 0--> 0,1 and 1--> 1,0
Grammar for N=4 would be :
         k=1  k=2  k=3  k=4
N=1      0                                     --> 2**0  --> length of a row
N=2      0    1                                --> 2**1
N=3      0    1    1    0                      --> 2**2
N=4      0    1    1    0    1    0    0   1   --> 2**3

Hypothesis:  solve(N,K)   --> returns 0, 1
             mid =  (2**N-1)/2      if K <= mid , solve(N-1, K)   ---> returns 0, 1  [similar to the previous row]
             if K > mid, !solve(N-1,N-mid)  --> complement of previous row which is second of the current row.
Induction : nothing
Base condition : If N,k== 1, return 0
"""
def solve(N,K):
    if(N == 1 or K == 1):
        return 0

    mid = (2**N-1) // 2
    if(K <= mid):
        return (solve(N-1, K))
    else:
        return (solve(N-1, K-mid) + 1) % 2

print(solve(4,8))
