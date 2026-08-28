# Score Analyzer

scores = [45, 78, 92, 56, 33, 88, 71, 49, 95, 62]

# 1. Print all scores

# 2. Print passing scores >=50

# 3. Print scores 80+

# 4. Square every score

# 5. Calculate average


for i in scores:
    print(i)

for i in scores:
    if (i >=50):
            print(i)

for i in scores:
     if (i >= 80):
          print(i)


ans = [score * score for score in scores]
print(ans)

print(sum(scores)/len(scores))