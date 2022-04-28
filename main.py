from Bio import Entrez, Medline

def obtain_combinations():
    compoundlist = []
    with open('compounds.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                compoundlist.append(line)
    file.close()

    molecular_effectslist = []
    with open('molecular_effects.txt', 'r') as file2:
        for line2 in file2:
            line2 = line2.strip()
            if line2:
                molecular_effectslist.append(line2)
    file2.close()

    geneslist = []
    with open('genes.txt', 'r') as file3:
        for line3 in file3:
            line3 = line3.strip()
            if line3:
                geneslist.append(line3)
    file3.close()

    for compound in compoundlist:
        for molecular_effect in molecular_effectslist:
            for gene in geneslist:
                inputterm = compound + "+" + \
                            molecular_effect + "+" + gene
                print(inputterm)
                Entrez.email = "A.N.Other@example.com"
                handle = Entrez.egquery(term=inputterm)
                record = Entrez.read(handle)
                for row in record["eGQueryResult"]:
                    if row["DbName"] == "pubmed":
                        amount_of_hits = int(row["Count"])
                        if amount_of_hits > 0:
                            print(str(amount_of_hits) + " articles found")
                            print(inputterm)
                            exit()

if __name__ == '__main__':
    obtain_combinations()