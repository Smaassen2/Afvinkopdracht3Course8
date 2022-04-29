from Bio import Entrez, Medline

def obtain_combinations():
    compoundlist = []
    with open('compounds2.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                compoundlist.append(line)
    file.close()

    molecular_effectslist = []
    with open('molecular_effects2.txt', 'r') as file2:
        for line2 in file2:
            line2 = line2.strip()
            if line2:
                molecular_effectslist.append(line2)
    file2.close()

    geneslist = []
    with open('genes2.txt', 'r') as file3:
        for line3 in file3:
            line3 = line3.strip()
            if line3:
                geneslist.append(line3)
    file3.close()

    return compoundlist, molecular_effectslist, geneslist

def search(compoundlist, molecular_effectslist, geneslist):

    highest_occurence = 0
    highest_occurence_combination = ""

    for compound in compoundlist:
        for molecular_effect in molecular_effectslist:
            for gene in geneslist:
                inputterms = compound + "+" + \
                            molecular_effect + "+" + gene
                #print(inputterms)
                Entrez.email = "A.N.Other@example.com"
                handle = Entrez.egquery(term=inputterms)
                record = Entrez.read(handle)
                for row in record["eGQueryResult"]:
                    if row["DbName"] == "pubmed":
                        amount_of_hits = int(row["Count"])
                        if amount_of_hits > 0:
                            print(inputterms + " --- " + str(amount_of_hits))

                        if amount_of_hits > highest_occurence:
                            highest_occurence = amount_of_hits
                            highest_occurence_combination = inputterms

                        elif amount_of_hits == highest_occurence:
                            highest_occurence_combination += " and " + inputterms

    print(highest_occurence_combination)
    print(highest_occurence)

if __name__ == '__main__':
    compoundlist, molecular_effectslist, geneslist = obtain_combinations()
    search(compoundlist, molecular_effectslist, geneslist)