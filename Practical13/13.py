# alignment.py
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

def read_blosum62(file_path):
    blosum62 = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
    amino_acids = lines[0].strip().split()
    for i in range(1, len(lines)):
        row = lines[i].strip().split()
        for j in range(1, len(row)):
            blosum62[(amino_acids[i-1], amino_acids[j-1])] = int(row[j])
    return blosum62

def calculate_score(seq1, seq2, blosum62):
    score = 0
    identical_count = 0
    for i in range(len(seq1)):
        pair = (seq1[i], seq2[i])
        score += blosum62.get(pair, 0)
        if seq1[i] == seq2[i]:
            identical_count += 1
    return score, identical_count / len(seq1) * 100

def main():
    seq1 = read_fasta('P04179_Human.fasta')
    seq2 = read_fasta('P09671_Mouse.fasta')
    random_seq = read_fasta('Random.fasta')
    blosum62 = read_blosum62('BLOSUM62.txt')
    
    print("Human vs Mouse:")
    score, identity = calculate_score(seq1, seq2, blosum62)
    print(f"Score: {score}, Identity: {identity:.2f}%")
    
    print("Human vs Random:")
    score, identity = calculate_score(seq1, random_seq, blosum62)
    print(f"Score: {score}, Identity: {identity:.2f}%")
    
    print("Mouse vs Random:")
    score, identity = calculate_score(seq2, random_seq, blosum62)
    print(f"Score: {score}, Identity: {identity:.2f}%")

if __name__ == "__main__":
    main()