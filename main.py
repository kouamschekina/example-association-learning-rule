from src.apriori import apriori

if __name__ == '__main__':
    result = apriori([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0.3, 0.7)
    print(result)