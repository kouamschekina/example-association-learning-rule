import support
dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]
from typing import List, Tuple
from support import support

dataset_type = List[List[object]]
rule_type = Tuple[List[object], List[object]]

def confidence(data_set: dataset_type, rule: rule_type) -> float:

    support_AB = support(data_set, rule[0] + rule[1])
    support_A = support(data_set, rule[0])
    if support_A != 0 :
        confidence = support_AB / support_A
    else:
        confidence = 0
    return confidence
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """
pass

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
