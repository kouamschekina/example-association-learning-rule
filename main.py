from src.apriori import apriori

if __name__ == '__main__':
    #assigning the value of apriori to the results variable
    results = apriori([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0.3, 0.7)
    #display results
    print(results)
