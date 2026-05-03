#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader
import re

pdf_folder = r"c:\Users\LENOVO\OneDrive\Documents\rti-240202897\jurnal-ws"
pdf_files = [
    "1608-Article Text-4049-4292-10.pdf",
    "4_paper+140 (1).pdf",
    "884-898-2-PB.pdf",
    "Analisis-Kualitas-Sistem-Informasi-Haji-Terpadu-Menggunakan-Metode-McCall.pdf",
    "hh,+FINISH+-+Edhy.pdf"
]

for filename in pdf_files:
    filepath = os.path.join(pdf_folder, filename)
    print(f"\n{'='*80}")
    print(f"FILE: {filename}")
    print('='*80)
    
    try:
        pdf = PdfReader(filepath)
        # Extract all text
        full_text = ""
        for page in pdf.pages:
            try:
                full_text += page.extract_text() or ""
            except:
                pass
        
        # Print first 5000 characters for manual analysis
        print(full_text[:5000])
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
