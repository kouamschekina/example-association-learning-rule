from src.apriori import apriori

dataset = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]

min_support = 0.3
min_confidence = 0.7

# Call the apriori function
frequent_itemsets, strong_rules = apriori(dataset, min_support, min_confidence)

# Display the results
print("Frequent Itemsets:")
for itemset, support_value in frequent_itemsets.items():
    print(f"{itemset}: {support_value}")

print("\nStrong Rules:")
for rule, confidence_value in strong_rules.items():
    print(f"{rule[0]} -> {rule[1]} (Confidence: {confidence_value})")