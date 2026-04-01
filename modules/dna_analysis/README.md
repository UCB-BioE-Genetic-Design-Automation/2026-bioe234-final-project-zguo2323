# DNA Sequence Analysis Module

## Overview
This module provides four fundamental DNA sequence analysis tools accessible via an AI assistant
through the MCP (Model Context Protocol) framework. Each tool accepts a raw DNA sequence string
or a named resource (e.g. `pBR322`) and returns a biologically meaningful result.

---

## Tools

### `dna_gc_content`
Computes the fraction of G and C bases in a DNA sequence.

| | |
|---|---|
| **Input** | `seq` — DNA sequence or resource name |
| **Output** | `float` between 0.0 and 1.0 |

**Example:**
```
You: What is the GC content of ATGCATGC?
Gemini: The GC content of ATGCATGC is 0.5 (50%).
```

---

### `dna_find_motif`
Finds all positions (1-based) where a short DNA pattern occurs in a sequence.

| | |
|---|---|
| **Input** | `seq` — DNA sequence or resource name; `motif` — pattern to search for |
| **Output** | `list` of integer positions |

**Example:**
```
You: Where does GAATTC appear in ATGAATTCGATGAATTC?
Gemini: GAATTC appears at positions [4, 12].
```

---

### `dna_sequence_length`
Returns the total number of bases in a DNA sequence.

| | |
|---|---|
| **Input** | `seq` — DNA sequence or resource name |
| **Output** | `int` — number of bases |

**Example:**
```
You: How many base pairs does pBR322 have?
Gemini: pBR322 is 4361 base pairs long.
```

---

### `dna_nucleotide_frequency`
Counts the occurrences of each nucleotide (A, T, G, C) in a DNA sequence.

| | |
|---|---|
| **Input** | `seq` — DNA sequence or resource name |
| **Output** | `dict` with keys `A`, `T`, `G`, `C` |

**Example:**
```
You: What is the nucleotide composition of AAATTTGGGCCC?
Gemini: The sequence contains A: 3, T: 3, G: 3, C: 3.
```

---

## Available Resources

| Resource | Description |
|---|---|
| `pBR322` | Classic E. coli cloning vector, 4361 bp circular plasmid |

---

## How to Run

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Start the client:
   ```bash
   python client_gemini.py
   ```

3. Type a natural language request, for example:
   ```
   What is the GC content of pBR322?
   Find all ATG positions in pBR322.
   How long is ATGCATGCATGC?
   Count the nucleotides in AAATTTGGGCCC.
   ```

---

## How to Run Tests

```bash
pytest -vv -l modules/dna_analysis/tools/
```

---

## File Structure

```
modules/dna_analysis/
├── README.md
├── SKILL.md
├── dna_analysis_theory.md
├── data/
└── tools/
    ├── gc_content.py
    ├── gc_content.json
    ├── find_motif.py
    ├── find_motif.json
    ├── sequence_length.py
    ├── sequence_length.json
    ├── nucleotide_frequency.py
    ├── nucleotide_frequency.json
    ├── prompts.json
    ├── test_gc_content.py
    ├── test_find_motif.py
    ├── test_sequence_length.py
    └── test_nucleotide_frequency.py
```
