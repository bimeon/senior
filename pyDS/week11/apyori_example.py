from apyori import apriori

transactions = [
    ['beer', 'nuts'],
    ['beer', 'cheese'],
    ['beer', 'cheese', 'milk'],
    ['milk', 'cheese'],
    ['milk', 'cheese', 'nuts'],
]

print(transactions)

results = list(apriori(transactions, min_support=0.3, min_confidence=0.5))

for res in results:
    print(res.ordered_statistics)