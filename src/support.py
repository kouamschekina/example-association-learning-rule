itemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """
    #initialising the counter to keep track of the occurance in the list
    count=0

    total_transactions=len(data_set)

#looping through the entire dataset for occurance of itemset

    for transaction in data_set:
        if set(itemsets).issubset(transaction):

            count = count + 1
 #implementing support method
 
    support_value=count / total_transactions

    return support_value

    
