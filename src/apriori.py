sub_dataset_type = tuple[object]
support_type = float
strong_rules = list[object], list[object]
confidence_type = float


def apriori(transactions: list[list[object]], min_support: float = 0.7, min_confidence: float = 0.5) \
        -> tuple[dict[sub_dataset_type, support_type], dict[strong_rules, confidence_type]]:
    """
    To find all frequent itemsets in a dataset and generate strong association rules.
    """

    return frequent_items, strong_rules
