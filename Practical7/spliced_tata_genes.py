import re

def find_genes_with_tata_and_genes(file_path, start_genes, end_genes):
    # Add a function to screen genes.
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    genes_pattern = re.compile(f'{start_genes}.*?{end_genes}', re.DOTALL)
    
    results = []
    tata_count_total = 0 
    # Record the total number of TATA boxes in all screened genes
    file_path = r"C:\Users\张嘉芮1\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    with open(file_path, 'r') as file:
        gene_name = None
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if gene_name:
                    # Store the sequence information of the previous gene
                    seq = ''.join(sequence)
                    if genes_pattern.search(seq) and tata_pattern.search(seq):
                        tata_count = len(re.findall(r'TATA[AT]A[AT]', seq))
                        tata_count_total += tata_count
                        results.append((gene_name, seq, tata_count))
                #Extract gene names
                gene_name = line[1:].split()[0]   
                sequence = []
            else:
                sequence.append(line)
        
        #Check and store information
        if gene_name:
            seq = ''.join(sequence)
            if genes_pattern.search(seq) and tata_pattern.search(seq):
                tata_count = len(re.findall(r'TATA[AT]A[AT]', seq))
                tata_count_total += tata_count
                results.append((gene_name, seq, tata_count))
    #return list of eligible genes and total number of TATA boxes.
    return results, tata_count_total
#Add another function
#Write the gene name and the number of TATA boxes.
#Write the gene sequence.
def write_genes_with_tata_and_boundary(genes, output_file):
    with open(output_file, 'w') as file:
        for gene_name, seq, tata_count in genes:
            file.write(f'>{gene_name}_TATA_{tata_count}\n')
            file.write(seq + '\n')
#Input the splice donnor/acceptor combination
#Check the input whether in these three types
def main():
    splice_sites = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").upper()
    if splice_sites not in ['GTAG', 'GCAG', 'ATAC']:
        print("Invalid combination. Please choose GTAG, GCAG, or ATAC.")
        return
    #input file path
    #output file name
    #Use the function to filter genes and obtain the results along with the total number of TATA boxes.
    #Write the selected genes into the output file.
    file_path = r"C:\Users\张嘉芮1\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = f'{splice_sites}_tata_genes.fa'
    
    start_boundary = splice_sites[:2]
    end_boundary = splice_sites[2:]
    
    genes, tata_count_total = find_genes_with_tata_and_genes(file_path, start_boundary, end_boundary)
    write_genes_with_tata_and_boundary(genes, output_file)
    
    print(f"Total number of TATA boxes in the filtered genes: {tata_count_total}")
    print(f"Genes with TATA boxes and {splice_sites} boundaries have been written to {output_file}")
#Main program entrance
if __name__ == "__main__":
    main()