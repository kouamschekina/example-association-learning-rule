from src.apriori import apriori

if __name__ == '__main__':
    #assigning the value of apriori to the results variable
    result = apriori([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0.3, 0.7)
    print(result)
