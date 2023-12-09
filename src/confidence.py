dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]
from support import support

def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """
    #association rule in the form (antecedent, consequent).
    antecedent, consequent = rule

    support_ab = support(antecedent + consequent, data_set)

    support_a = support(antecedent, data_set)

    if support_a != 0:
 #validating the value of the Supp of the antecedent before computation
 
        confidence_value = support_ab / support_a

    else:
        confidence_value = 0

    return confidence_value
    
