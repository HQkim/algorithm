
# # 2중 for문 사용. O(n^2)
# def solution(prices):
    
#     answer = []
    
#     for i in range(len(prices)):
#         price = prices[i]
#         not_down = 0
#         for j in range(i+1, len(prices)):
#             not_down += 1
#             if price > prices[j]:
#                 break
#         answer.append(not_down)
    
    
#     return answer

# stack 이용 O(n)
def solution(prices):
    l = len(prices)
    ans = [0] * l
    st = [(0, prices[0])]
    for i, v in enumerate(prices[1:], 1):
        t1, v1 = st[-1]
        while v < v1:
            st.pop()
            ans[t1] = i - t1
            if st:
                t1, v1 = st[-1]
            else:
                break
        st.append((i, v))
    
    # 남아있는애들
    while st:
        t, v = st.pop()
        ans[t] = l - 1 - t
    
    return ans

print(solution([1,2,3,2,3]))