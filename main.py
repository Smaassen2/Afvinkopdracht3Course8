import itertools

def obtain_combinations():
    compoundlist = []
    with open('compounds.txt', 'r') as file:
    # with open('test.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                compoundlist.append(line)
    #print(len(compoundlist))
    file.close()

    molecular_effectslist = []
    with open('molecular_effects.txt', 'r') as file2:
        # with open('test.txt', 'r') as file:
        for line2 in file2:
            line2 = line2.strip()
            if line2:
                molecular_effectslist.append(line2)
    #print(len(molecular_effectslist))
    file2.close()

    geneslist = []
    with open('genes.txt', 'r') as file3:
        # with open('test.txt', 'r') as file:
        for line3 in file3:
            line3 = line3.strip()
            if line3:
                geneslist.append(line3)
    #print(len(geneslist))
    file3.close()

    #iterable = ["Beer", "Koe", "Kip", "Varken"]
    #print(list(itertools.combinations(iterable, 2)))

    combinations = []
    counter = 0
    for compound in compoundlist:
        for molecular_effect in molecular_effectslist:
            for gene in geneslist:
                counter += 1
                #combinations.append(compound + " " + molecular_effect
                #                    + " " + gene)
    #print(len(combinations))
    print(counter)





if __name__ == '__main__':
    obtain_combinations()