import re
def tata_genes(file_path):
    gene_results = []
    tata_pattern = re.compile(r'TATA')
    file_path = r"C:\Users\张嘉芮1\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    with open(file_path, 'r') as file:
        gene = None
        seq = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if gene:
                    gene_results.append((gene, ''.join(seq)))
                parts = line[1:].split()
                gene = parts[0]
                gene = re.sub(r'_mRNA$', '', gene)
                seq = []
            else:
                seq.append(line)
        if gene:
            gene_results.append((gene, ''.join(seq)))    
    tata_genes = []
    for gene, seq in gene_results:
        if any(tata_pattern.search(seq) for _ in range(len(seq))):
            tata_genes.append([gene, seq])
    
    return tata_genes

def write_tata_genes(tata_genes, output_file):
    with open(output_file, 'w') as file:
        for gene,seq in tata_genes:
            file.write(f'>{gene}\n')
            file.write(seq + '\n')
file_path = r"C:\Users\张嘉芮1\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
tata_genes = tata_genes(file_path)
write_tata_genes(tata_genes, 'tata_genes.fa')