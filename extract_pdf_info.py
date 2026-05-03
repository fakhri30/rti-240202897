#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from pypdf import PdfReader
import json

pdf_folder = r"c:\Users\LENOVO\OneDrive\Documents\rti-240202897\jurnal-ws"
pdf_files = [
    "1608-Article Text-4049-4292-10.pdf",
    "4_paper+140 (1).pdf",
    "884-898-2-PB.pdf",
    "Analisis-Kualitas-Sistem-Informasi-Haji-Terpadu-Menggunakan-Metode-McCall.pdf",
    "hh,+FINISH+-+Edhy.pdf"
]

results = []

for filename in pdf_files:
    filepath = os.path.join(pdf_folder, filename)
    print(f"\n{'='*80}")
    print(f"Processing: {filename}")
    print('='*80)
    
    try:
        pdf = PdfReader(filepath)
        # Get metadata
        metadata = pdf.metadata
        print(f"Metadata: {json.dumps(metadata, indent=2, default=str)}")
        
        # Extract text from first 2 pages
        text_content = ""
        for i, page in enumerate(pdf.pages[:2]):
            try:
                text_content += page.extract_text() or ""
            except:
                pass
            if i >= 1:  # Only first 2 pages
                break
        
        # Print first 1500 chars of extracted text
        print(f"\n--- EXTRACTED TEXT (First 1500 chars) ---")
        print(text_content[:1500])
        
        # Store for later analysis
        results.append({
            "filename": filename,
            "metadata": metadata,
            "extracted_text": text_content[:3000],  # Store more text for analysis
            "num_pages": len(pdf.pages)
        })
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        results.append({
            "filename": filename,
            "error": str(e)
        })

print(f"\n\n{'='*80}")
print("SUMMARY")
print('='*80)
print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
