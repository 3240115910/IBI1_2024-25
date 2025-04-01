import re

def get_spliced_genes(file_path, splice_sites):
    # 编译正则表达式以匹配剪接位点
    splice_pattern = re.compile(f'({splice_sites[0]})(.*?)({splice_sites[1]})')
    results = []
    
    with open(file_path, 'r') as file:
        gene_name = None
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if gene_name:
                    # 检查并存储上一个基因的剪接序列
                    spliced_seq = ''.join(sequence)
                    match = splice_pattern.search(spliced_seq)
                    if match:
                        spliced_seq = match.group(1) + match.group(2) + match.group(3)
                        tata_count = len(re.findall(r'TATA[AT]', spliced_seq))
                        results.append((gene_name, spliced_seq, tata_count))
                gene_name = line[1:]
                sequence = []
            else:
                sequence.append(line)
        
        # 检查并存储最后一个基因的剪接序列
        if gene_name:
            spliced_seq = ''.join(sequence)
            match = splice_pattern.search(spliced_seq)
            if match:
                spliced_seq = match.group(1) + match.group(2) + match.group(3)
                tata_count = len(re.findall(r'TATA[AT]', spliced_seq))
                results.append((gene_name, spliced_seq, tata_count))
    
    return results

def write_spliced_genes(spliced_genes, output_file):
    with open(output_file, 'w') as file:
        for gene_name, seq, tata_count in spliced_genes:
            file.write(f'>{gene_name}_TATA_{tata_count}\n')
            file.write(seq + '\n')

def main():
    splice_sites = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").upper()
    if splice_sites not in ['GTAG', 'GCAG', 'ATAC']:
        print("Invalid combination. Please choose GTAG, GCAG, or ATAC.")
        return
    
    file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = f'{splice_sites}_spliced_genes.fa'
    
    spliced_genes = get_spliced_genes(file_path, splice_sites)
    write_spliced_genes(spliced_genes, output_file)
    print(f"Spliced genes with TATA boxes have been written to {output_file}")

if __name__ == "__main__":
    main()