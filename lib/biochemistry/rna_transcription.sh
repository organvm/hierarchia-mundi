#!/usr/bin/env bash
# rna_transcription.sh
# The central dogma: DNA → RNA → Protein
# Information flows from storage to execution.
# (With exceptions. Biology always has exceptions.)

set -euo pipefail

# ============================================================
# STEP 1: TRANSCRIPTION (DNA → mRNA)
# ============================================================
# RNA polymerase reads the template strand 3'→5'
# and synthesizes mRNA 5'→3'.
#
# Codon table (mRNA → amino acid):
#   AUG = Met (START)
#   UUU/UUC = Phe
#   UAA/UAG/UGA = STOP
#   ...64 codons total → 20 amino acids + 3 stops
#
# The genetic code is (nearly) universal across all life on Earth.
# This is evidence of a single common ancestor.

echo "[TRANSCRIPTION] RNA polymerase binding to promoter"
echo "[TRANSCRIPTION] Unwinding DNA double helix"
echo "[TRANSCRIPTION] Synthesizing pre-mRNA from template strand"

# ============================================================
# STEP 2: RNA PROCESSING (pre-mRNA → mature mRNA)
# ============================================================
# In eukaryotes only. Prokaryotes skip this.
#
# - 5' cap: methylated guanine (protects from degradation)
# - 3' poly-A tail: ~200 adenines (stability and export signal)
# - Splicing: remove introns, join exons
#
# Alternative splicing: same gene → different proteins
# This is why humans have ~20,000 genes but ~100,000 proteins.
# The genome is a library. Splicing is the reader's interpretation.

echo "[PROCESSING] Adding 5' cap"
echo "[PROCESSING] Adding poly-A tail"
echo "[PROCESSING] Splicing: removing introns, joining exons"

# ============================================================
# STEP 3: TRANSLATION (mRNA → Protein)
# ============================================================
# The ribosome — a molecular factory made of RNA and protein —
# reads mRNA three nucleotides at a time (codons) and
# assembles the corresponding amino acid chain.
#
# tRNA molecules are the adaptors:
#   anticodon (reads mRNA) ←→ amino acid (loads into chain)
#
# Speed: ~20 amino acids per second in bacteria
# Accuracy: ~1 error per 10,000 codons
# Multiple ribosomes can read the same mRNA simultaneously (polysome)

echo "[TRANSLATION] Ribosome assembled at AUG start codon"
echo "[TRANSLATION] tRNA delivering amino acids"
echo "[TRANSLATION] Peptide chain elongating..."
echo "[TRANSLATION] Stop codon reached. Protein released."

# ============================================================
# THE EXCEPTIONS (Biology's favorite word)
# ============================================================
# - Retroviruses: RNA → DNA (reverse transcriptase). HIV does this.
# - Ribozymes: RNA that catalyzes reactions (RNA can be an enzyme).
# - Prions: Protein → Protein misfolding (no nucleic acid involved).
# - Epigenetics: Gene expression without DNA sequence change.
#
# The central dogma is a default, not a law.
# Life finds ways around every rule.

echo "[COMPLETE] Gene expressed. Protein folding in progress."
echo "[NOTE] Loading /lib/biochemistry/proteins.lib for folding..."
