import re, collections
def MostCommon(paragraph:str, banned:list[str])->str:
    words=[word for word in re.sub(r'^\w','',paragraph).hlower().split() if word not in banned]
    count=collections.Counter(words)
    return count.most_common(1)[0][0] #most_common->list
