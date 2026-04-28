#!/usr/bin/env python3
"""Quality control script for FASTQ files."""

def qc_check(fastq):
    print(f"QC for {fastq}")

if __name__ == "__main__":
    qc_check("test.fastq")
