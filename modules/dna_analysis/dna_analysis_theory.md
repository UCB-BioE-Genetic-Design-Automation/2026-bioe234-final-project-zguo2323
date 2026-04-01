# DNA Sequence Analysis — Theory Documentation

## Overview
DNA (deoxyribonucleic acid) is the molecule that carries genetic information in all living organisms.
It is composed of four nucleotide bases: **Adenine (A)**, **Thymine (T)**, **Guanine (G)**, and
**Cytosine (C)**. The sequence of these bases encodes the instructions for building and operating
a cell. Computational analysis of DNA sequences is a fundamental task in bioinformatics, enabling
researchers to characterize genomes, identify functional elements, and compare organisms.

---

## Tool 1 — GC Content

### Biological Background
GC content refers to the percentage of bases in a DNA sequence that are either Guanine (G) or
Cytosine (C). Because G pairs with C via three hydrogen bonds (compared to two for A-T pairs),
GC-rich regions are thermally more stable. This property has important implications for:

- **PCR and primer design** — primers with higher GC content have higher melting temperatures (Tm)
- **Genome characterization** — organisms vary widely in GC content (25%–75% across species)
- **Gene prediction** — coding regions often differ in GC content from non-coding regions

### Formula

$$\text{GC content} = \frac{G + C}{A + T + G + C}$$

A value of 0.5 (50%) means the sequence has equal proportions of GC and AT bases.
Values above 0.6 are considered GC-rich; values below 0.4 are AT-rich.

---

## Tool 2 — Motif Finding

### Biological Background
A **motif** is a short, recurring sequence pattern that often has biological significance.
Examples include:

- **Restriction enzyme recognition sites** — e.g. EcoRI recognizes `GAATTC`
- **Transcription factor binding sites** — proteins bind specific DNA sequences to regulate gene expression
- **Start codons** — `ATG` marks the beginning of a protein-coding region
- **Promoter elements** — e.g. the TATA box (`TATAAA`) initiates transcription

Identifying where a motif occurs in a genome helps researchers locate regulatory elements,
cloning sites, and other functional sequences.

### Method
A sliding window of length equal to the motif is moved one base at a time across the sequence.
At each position, the window is compared to the motif. All matching positions are reported
using **1-based indexing** (position 1 = first base), which is the standard in molecular biology.

---

## Tool 3 — Sequence Length

### Biological Background
The length of a DNA sequence (measured in **base pairs**, bp) is one of the most fundamental
descriptors of a genetic element. It determines:

- **Gene size** — average human gene spans ~27,000 bp
- **Plasmid size** — laboratory vectors like pBR322 are 4,361 bp
- **Genome size** — ranges from ~500,000 bp (some bacteria) to >100 billion bp (some plants)

Sequence length is also used to normalize other measurements (e.g. motif density = number
of hits / sequence length).

### Method
Sequence length is simply the count of nucleotide characters in the string after removing
whitespace and non-sequence characters.

---

## Tool 4 — Nucleotide Frequency

### Biological Background
Counting the individual occurrences of A, T, G, and C in a sequence reveals its **nucleotide
composition**. This is useful for:

- **Verifying GC content** — G + C counts should match the GC content calculation
- **Detecting bias** — some organisms show strong strand asymmetry (more G than C on one strand)
- **Codon usage analysis** — nucleotide composition influences which codons are preferred

By Chargaff's rules, in a double-stranded DNA molecule the amount of A equals T, and the
amount of G equals C. Deviations from this in a single-stranded sequence are expected and
biologically informative.

### Method
Each of the four bases is counted independently using exact string matching after converting
the sequence to uppercase. The result is returned as a dictionary with keys `A`, `T`, `G`, `C`.

---

## References
- Watson, J.D. & Crick, F.H.C. (1953). Molecular structure of nucleic acids. *Nature*, 171, 737–738.
- Chargaff, E. (1950). Chemical specificity of nucleic acids. *Experientia*, 6, 201–209.
- Lewin, B. (2004). *Genes IX*. Jones and Bartlett Publishers.
