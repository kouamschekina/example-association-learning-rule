itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    count = 0
    for transaction in itemsets:
        total_transactions = len(itemsets)
        if set(data_set).issubset(transaction):
            count += 1
        support = count / total_transactions
        return support

    """
    To find the frequency of itemsets in the dataset.
    """
    pass
