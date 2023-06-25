from easy_kmer import Kmer

sequence = "ATCGATCGATCG"
k = 3

kmers = Kmer(sequence, k).get_kmers()
print(kmers)

kmer_counts = Kmer(sequence, k).count_kmers()
print(kmer_counts)

top_kmers = Kmer(sequence, k).most_frequent_kmers(5)
print(top_kmers)

reverse_complement = Kmer(sequence, k).reverse_complement()
print(reverse_complement)
