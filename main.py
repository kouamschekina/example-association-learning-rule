from src.apriori import apriori
def multiplication():
    try:
        a = input(float("enter the first number"))
        b = input(float("enter the second number"))
        product = (a*b)
        return product
    except ValueError:
        return("enter a valid number")
    

if __name__ == '__main__':
    #assigning the value of apriori to the results variable
    result = apriori([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0.3, 0.7)
    #display result
    print(result)
multiplication()