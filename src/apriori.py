from typing import List, Tuple, Dict
from itertools import chain, combinations

# Importing support and confidence functions
from support import support
from confidence import confidence

sub_dataset_type = Tuple[object]
support_type = float
strong_rules_type = Tuple[List[object], List[object]]
confidence_type = float


def apriori(transactions: List[List[object]], min_support: float = 0.7, min_confidence: float = 0.5) \
        -> Tuple[Dict[sub_dataset_type, support_type], Dict[strong_rules_type, confidence_type]]:
    """
    To find all frequent itemsets in a dataset and generate strong association rules.
    """

    # Initializes dictionaries to store frequent itemsets and strong rules.
    frequent_itemsets = {}
    strong_rules = {}

    # Creates unique 1-itemsets and calculates their support using the support function.
    # Initialize L1 = {frequent 1-itemsets}
    unique_items = set(item for transaction in transactions for item in transaction)
    candidates_1 = [frozenset([item]) for item in unique_items]
    frequent_itemsets[1] = {candidate: support(transactions, [list(candidate)]) for candidate in candidates_1}

    # Iterates over the levels of itemsets (k) until no more frequent itemsets are found and generating candidate sets
    # For (k = 2; Lk-1 is not empty; k++):
    k = 2
    while len(frequent_itemsets[k - 1]) > 0:
        # Generating Ck, candidate k-itemsets, from Lk-1
        candidates_k = generate_candidates(list(frequent_itemsets[k - 1]), k)

        # For each transaction t in D:
        for transaction in transactions:
            # Increment count of all candidates in Ck that are contained in t
            for candidate in candidates_k:
                if set(candidate).issubset(transaction):
                    frequent_itemsets[k - 1][frozenset(candidate)] += 1

        # Lk = {c in Ck | support(c) >= min_support}
        frequent_itemsets[k] = {candidate: support_value for candidate, support_value in
                                frequent_itemsets[k - 1].items()
                                if support_value / len(transactions) >= min_support}

        k += 1

    # Frequent Itemsets = Union of all Lk
    frequent_itemsets = {itemset: support_value for itemsets in frequent_itemsets.values() for itemset, support_value in
                         itemsets.items()}

    # For each frequent itemset l in Frequent Itemsets:
    for itemset in frequent_itemsets.keys():

        # Generate all non-empty subsets of l
        subsets = get_subsets(itemset)

        # For every non-empty subset s of l:
        for subset in subsets:
            # Rule = s -> (l - s)
            rule = (subset, list(set(itemset) - set(subset)))

            # If Calculate_Confidence(D, Rule) >= min_confidence:
            confidence_value = confidence(transactions, rule)
            if confidence_value >= min_confidence:
                # Add Rule to Strong Rules
                strong_rules[tuple(rule)] = confidence_value

    # Return Frequent Itemsets, Strong Rules
    return frequent_itemsets, strong_rules


def generate_candidates(frequent_itemsets: List[frozenset], k: int) -> List[frozenset]:
    """
    Generate candidate k-itemsets from frequent (k-1)-itemsets.
    """
    candidates = []
    n = len(frequent_itemsets)

    for i in range(n):
        for j in range(i + 1, n):
            # Merging the frequent (k-1)-itemsets to generate candidates
            candidate = frozenset(sorted(set(frequent_itemsets[i]).union(frequent_itemsets[j])))

            # Check if the candidate has length k
            if len(candidate) == k:
                candidates.append(candidate)

    return candidates



def get_subsets(itemset: List[object]) -> List[List[object]]:
    """
    Generate all non-empty subsets of a set.
    """
    return [list(subset) for subset in chain.from_iterable(combinations(itemset, r) for r in range(1, len(itemset)))]








    