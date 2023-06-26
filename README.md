# easy kmer
### What is K-mer?
K-mers are short substrings of DNA or RNA sequences that are used to analyze patterns and characteristics. They provide insights into repetitive elements, conserved regions, and sequence motifs. K-mers are valuable tools in bioinformatics for tasks like sequence analysis and genome assembly, revealing important information about the structure and function of genetic material.

### easy-kmer
easy-kmer is a lightweight Python library for working with k-mers in bioinformatics. It provides simple and intuitive methods to extract k-mers from DNA or RNA sequences, count their occurrences, find the most frequent k-mers, and compute the reverse complement of a sequence.

### Install
You can install easy_kmer using pip:
```bash:install.sh
pip install easy-kmer
```

### Example 
KMer(sequence (str): The DNA or RNA sequence, k (int): The length of the k-mers) : Constructor for the KMer class. It takes two parameters.<br>
Here's an example of how to use easy_kmer:
```python:example.py
from easy_kmer import Kmer
sequence = "ATCGATCGATCG"

k = 3

kmers = Kmer(sequence, k).get_kmers()
print(kmers)
>>> ['ATC', 'TCG', 'CGA', 'GAT', 'ATC', 'TCG', 'CGA', 'GAT', 'ATC', 'TCG']

kmer_counts = Kmer(sequence, k).count_kmers()
print(kmer_counts)
>>> {'ATC': 3, 'TCG': 3, 'CGA': 2, 'GAT': 2}

top_kmers = Kmer(sequence, k).most_frequent_kmers(5)
print(top_kmers)
>>> [('ATC', 3), ('TCG', 3), ('CGA', 2), ('GAT', 2)]

reverse_complement = Kmer(sequence, k).reverse_complement()
print(reverse_complement)
>>> CGATCGATCGAT
```

- get_kmers() : Retrieves all the k-mers in the sequence.

- count_kmers() : Counts the occurrences of each k-mer in the sequence and returns a dictionary where the keys are the k-mers and the values are the counts.

- most_frequent_kmers(top_n=None) : Returns a list of the most frequent k-mers in the sequence, sorted in descending order of frequency. The top_n parameter can be used to limit the number of top k-mers returned.

- reverse_complement() : Computes the reverse complement of the sequence. It replaces each base (A, T, C, G) with its complement (T, A, G, C) and then reverses the resulting string.
