def getTopThreeScores(*scores:float)->tuple:
    for item in scores :
        if not (isinstance(item,float)):
            raise RuntimeError("Float is not passed to function geTopThreeScores")
    if not scores:
        return None
    result = ()
    for i in range (3):
        scores = tuple(scores)
        result = result + (max(scores),)
        scores = list(scores)
        scores.remove(max(scores))
    return result

ans = getTopThreeScores(1.0,2.0,3.0,21.0,33.0,4.01)
print(f"The top three scores of the class are {ans}")