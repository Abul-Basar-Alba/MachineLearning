
#B: Tournament
# t=int(input())

# for _ in range(t):
#     n,j,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     aj=a[j-1]
#     if k>=2:
#         print("YES")
#     else:
#         mx=max(a)
#         if(aj==mx):
#            print("YES")
#         else:
#             print("NO")


# A. Blackboard Game

# t=int(input())
# for _ in range(t):
#     n=int(input())
#     if n%4==0:
#         print("Bob")
#     else:
#         print("Alice")

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=['0'] * n 

    cur_min=float('inf')
    for i in range(n):
        if a[i]<cur_min:
            cur_min=a[i]
            ans[i]='1'

    cur_max=float('-inf')
    for i in range(n-1,-1,-1):
        if a[i]>cur_max:
            cur_max=a[i]
            ans[i]='1'

    print(''.join(ans))