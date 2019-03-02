# p = 'abcdabcef'                                                                       # pattern
# t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text


# m, n = len(p), len(t)
# next = [0] * (m + 1) # 편의상 p의 길이보다 1 긴(인덱스 0을 버리기 위함..) 리스트를 생성

# # 전처리
# next[0] = -1 # 맨 앞을 시작의 의미로 -1로 설정
# i, j = 0, -1
# while i < m:
#     while j >= 0 and p[j] != p[i]: # j 가 시작값인 -1이 되지 않기 위함..
#         j = next[j]

#     i, j = i + 1, j + 1
#     next[i] = j

# print(next)

# # 매칭
# i = j = 0
# while i < n:
#     while j >= 0 and p[j] != t[i]:
#         j = next[j]

#     i, j = i + 1, j + 1

#     if j == m:
#         print(i - j, t[:i - j], t[i - j:i - j + m], t[i - j + m:])
#         break
