# Apriori

In association rules mining, the aprori help to find all frequent 
itemsets in a dataset and generate strong association rules.

## More Information

- https://en.wikipedia.org/wiki/Apriori_algorithm

## Pseudocode

```text
Algorithm: Apriori
Input: Dataset (D), Minimum Support (min_support), Minimum Confidence (min_confidence)
Output: Frequent Itemsets, Strong Rules

1. Initialize: L1 = {frequent 1-itemsets}
2. For (k = 2; Lk-1 is not empty; k++):
    a. Generate Ck, candidate k-itemsets, from Lk-1
    b. For each transaction t in D:
        i. Increment count of all candidates in Ck that are contained in t
    c. Lk = {c in Ck | support(c) >= min_support}
3. Frequent Itemsets = Union of all Lk
4. For each frequent itemset l in Frequent Itemsets:
    a. Generate all non-empty subsets of l
    b. For every non-empty subset s of l:
        i. Rule = s -> (l - s)
        ii. If Calculate_Confidence(D, Rule) >= min_confidence:
            a. Add Rule to Strong Rules
5. Return Frequent Itemsets, Strong Rules
```
