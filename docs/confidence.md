# Confidence

In association rules mining, the confidence help to measure the 
likelihood of occurrence of an itemset given another itemset.

## More Information

- https://en.wikipedia.org/wiki/Association_rule_learning#Confidence

## Pseudocode

```text
Algorithm: Calculate_Confidence
Input: Dataset (D), Rule (A -> B)
Output: Confidence value for Rule

1. Support_AB = Calculate_Support(D, A ∪ B)
2. Support_A = Calculate_Support(D, A)
3. If Support_A is not 0:
    a. Confidence = Support_AB / Support_A
   Else:
    a. Confidence = 0
4. Return Confidence
```
