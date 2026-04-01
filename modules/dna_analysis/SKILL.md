# dna_analysis — Skill Guidance for Gemini

## What this module does
This module provides basic DNA sequence analysis tools. Given a raw DNA sequence or a named
resource, it can compute GC content, locate motifs, measure sequence length, and count
individual nucleotide occurrences. All tools accept standard ATGC sequences in uppercase
or lowercase.

## Available resources
| Resource name | Description |
|---------------|-------------|
| `pBR322`      | Classic E. coli cloning vector, 4361 bp circular plasmid. |

## Tools and when to use them

### `dna_gc_content`
Computes the fraction of G and C bases in a sequence. Returns a float between 0.0 and 1.0.
- Trigger phrases: "GC content", "GC fraction", "GC percentage", "how GC-rich"
- Parameter notes: `seq` accepts a resource name or raw sequence string
- Output notes: multiply by 100 to express as a percentage (e.g. 0.5 → 50%)

### `dna_find_motif`
Finds all positions where a short DNA pattern appears in a larger sequence.
Returns a list of 1-based start positions. Returns an empty list if not found.
- Trigger phrases: "find motif", "where does X appear", "positions of", "search for pattern"
- Parameter notes: `seq` is the sequence to search; `motif` is the pattern (not resolved as a resource)
- Output notes: positions are 1-based (first base = position 1); overlapping matches are included

### `dna_sequence_length`
Returns the total number of bases in a sequence.
- Trigger phrases: "how long", "length", "how many base pairs", "how many bases", "size of"
- Parameter notes: `seq` accepts a resource name or raw sequence string
- Output notes: result is an integer count of bases

### `dna_nucleotide_frequency`
Counts the number of A, T, G, and C bases in a sequence.
Returns a dictionary with keys "A", "T", "G", "C".
- Trigger phrases: "nucleotide frequency", "nucleotide composition", "count bases", "how many A/T/G/C"
- Parameter notes: `seq` accepts a resource name or raw sequence string
- Output notes: only standard bases are counted; ambiguous bases are ignored

## Interpreting results
- GC content above 0.6 (60%) is considered GC-rich; below 0.4 (40%) is AT-rich.
- An empty motif search result means the pattern does not exist in the sequence.
- Nucleotide counts should sum to the total sequence length for standard ATGC sequences.
