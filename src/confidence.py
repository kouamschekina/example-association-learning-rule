from typing import List, Tuple
from support import support

dataset_type = List[List[object]]
rule_type = Tuple[List[object], List[object]]


def confidence(dataset: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """
    antecedent, consequent = rule
    antecedent_support = support(antecedent, dataset)
    rule_support = support(antecedent + consequent, dataset)

    if antecedent_support == 0:
        return 0  # Avoid division by zero

    confidence_value = rule_support / antecedent_support
    return confidence_value
