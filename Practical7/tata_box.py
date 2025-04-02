import re
# To start a function.
def tata_genes(file_path):
    #Create an empty list
    #To research the TATAWAW
    #To tell the computer the position of the file
    gene_results = []
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    file_path = r"C:\Users\张嘉芮1\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    #read the file line by line   
    with open(file_path, 'r') as file:
        gene = None
        seq = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):#To make sure whether it is a new gene.
                if gene:
                    gene_results.append((gene, ''.join(seq)))
                #To output the results which have name and the sequence.
                parts = line[1:].split()
                gene = parts[0]
                gene = re.sub(r'_mRNA$', '', gene)
                seq = []
            else:
                seq.append(line)
        if gene:
            gene_results.append((gene, ''.join(seq)))    
    tata_genes = []
    #Screening genes containing TATAWAW
    for gene, seq in gene_results:
         if tata_pattern.search(seq):
            tata_genes.append([gene, seq])
    
    return tata_genes
# write new FASTA file.
def write_tata_genes(tata_genes, output_file):
    with open(output_file, 'w') as file:
        for gene,seq in tata_genes:
            file.write(f'>{gene}\n')
            file.write(seq + '\n')
file_path = r"C:\Users\张嘉芮1\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
tata_genes = tata_genes(file_path)
write_tata_genes(tata_genes, 'tata_genes.fa')