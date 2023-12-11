from typing import List

itemset_type = frozenset
dataset_type = List[List[object]]

def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """
    # initializing the counter to keep track of the occurrence in the list
    count = 0

    total_transactions = len(data_set)

    # looping through the entire dataset for occurrence of itemset
    for transaction in data_set:
        if itemsets.issubset(transaction):
            count = count + 1

    # implementing support method
    support_value = count / total_transactions

    return support_value


