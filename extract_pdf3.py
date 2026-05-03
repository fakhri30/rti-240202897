#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader

filepath = r"c:\Users\LENOVO\OneDrive\Documents\rti-240202897\jurnal-ws\884-898-2-PB.pdf"

try:
    pdf = PdfReader(filepath)
    full_text = ""
    for i, page in enumerate(pdf.pages):
        try:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        except Exception as e:
            print(f"Error on page {i}: {e}")
    
    # Print in chunks to avoid encoding issues
    print(full_text[:6000])
    
except Exception as e:
    print(f"ERROR: {str(e)}")
