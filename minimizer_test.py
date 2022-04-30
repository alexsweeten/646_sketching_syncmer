from Bio import SeqIO
import screed

def parse_seq(filename):
    seq = ""
    for seq_record in SeqIO.parse(filename, "fasta"):
        seq = seq_record.seq
    return seq

def jaccard(set1,set2):
        union = set1.union(set2)
        intersection = set1.intersection(set2)
        return float(len(intersection)/len(union))

def containment(set1,set2):
        intersection = set1.intersection(set2)
        return float(len(intersection)/len(set1))

def compute_min_set(seq):
        rev=seq[::-1]

        rev=rev.replace("A","X")
        rev=rev.replace("T","A")
        rev=rev.replace("X","T")
        rev=rev.replace("C","X")
        rev=rev.replace("G","C")
        rev=rev.replace("X","G")

        Kmer=25
        M=15
        L=len(seq)

        minimizer_set = set()

        for i in range(0, L-Kmer+1):

                sub_f=seq[i:i+Kmer]
                sub_r=rev[L-Kmer-i:L-i]

                min="ZZZZZZZZZZZZZ"
                for j in range(0, Kmer-M+1):
                        sub2=sub_f[j:j+M]
                        if sub2 < min:
                                min=sub2
                        sub2=sub_r[j:j+M]
                        if sub2 < min:
                                min=sub2
                #print(sub_f,min)
                minimizer_set.add(min)
        return minimizer_set

def parse_seq(filename):
    seq = ""
    for seq_record in SeqIO.parse(filename, "fasta"):
        seq = seq_record.seq
    return seq

'''akker = parse_seq("simulated_original.fa")
akker_min = compute_min_set(akker)

akker_2 = parse_seq("simulated_90.fa")
akker_min_2 = compute_min_set(akker_2)
print(len(akker_min))
print(len(akker_min_2))

print(jaccard(akker_min,akker_min_2))'''
