# words = ['a', 'b', 'a', 'c', 'd']
# words2 = list(words)
# stopwords = ['a', 'c']
# for word in words2:  # iterating on a copy since removing will mess things up
#     if word in stopwords:
#         words.remove(word)

# print(words)

nums = [[5,2,3],[4,5,1],[7,6,3]]
# new = []

# for num in nums:
#     new.extend(num)
# print(new)

d = [new.extend(num) for num in nums]
print(d)