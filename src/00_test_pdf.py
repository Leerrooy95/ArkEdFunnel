import pdfplumber

print("OPENING REAL ARKANSAS EFA REPORT...\n")

with pdfplumber.open("raw/2024-25_Arkansas_Education_Freedom_Accounts_Program_Annual_Report_100125_OSCPE.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    
    print("FIRST 500 CHARACTERS:")
    print("-" * 60)
    print(text[:500])
    print("-" * 60)
    
    lines = text.lower().split("\n")
    
    # Hot Spring search
    hot_lines = [line.strip() for line in lines if "hot spring" in line or "hssd" in line or "hot springs" in line]
    print("\nHOT SPRING / HSSD MENTIONS:")
    if hot_lines:
        for line in hot_lines[:10]:
            print("→", line)
    else:
        print("→ None found — data likely in tables.")
    
    # Key EFA stats
    stats = [line for line in lines if any(k in line for k in ["participants", "enrolled", "funded", "2024-25", "total", "account"])]
    print("\nKEY EFA NUMBERS:")
    for line in stats[:8]:
        print("→", line.strip())
