def Union(_firstList, _secondList):
    final_list = list(set(_firstList) | set(_secondList))
    return final_list

if __name__ == "__main__":
    list1 = [10,20,30,40,30,50,60]
    list2=[10,15,20,30,25,25]
    print(Union(list1, list2))
