
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

t=int(input())
for _ in range(t):
    n=int(input())
    if n%4==0:
        print("Bob")
    else:
        print("Alice")