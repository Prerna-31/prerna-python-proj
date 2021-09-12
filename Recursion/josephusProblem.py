def killPerson(length, k, persons, ind):
    if(length == 1):
        return persons[0]
    killerInd = ind
    victimInd = (ind + k)%length
    print("{} kills {}".format(persons[killerInd], persons[victimInd]))
    persons.remove(persons[victimInd])
    killPerson(len(persons), k, persons, victimInd)
    return(persons[0])

persons = [1,2,3,4,5,6,7]
savePosition = killPerson(len(persons), 1 , persons , 0)
print("Josephus should sit at {}th position".format(savePosition))