import support
dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]


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
