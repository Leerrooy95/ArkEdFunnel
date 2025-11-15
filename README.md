# Arkansas Local: EFA Voucher Drain on Hot Springs School District

**Goal**: Prove that Education Freedom Accounts (EFAs) + desegregation transfer limits are starving Hot Springs School District (HSSD) of $1.7M+ in 2025.

**Entry Vector**: EFA approvals + HSSD budgets + deseg settlement history  
**Counties**: Hot Spring (primary), Saline (control)  
**Timeframe**: 2023–2025  
**Impact**: Public schools at risk of cuts; violates Lake View adequacy.

## Repo Structure
- `raw/` → original PDFs, CSVs (never edit)
- `src/` → Python scripts
- `out/` → graphs, CSVs, briefing PNGs
- `docs/` → data dictionary, methodology

## Run Pipeline
```bash
python3 src/01_ingest.py
python3 src/02_link.py
python3 src/03_viz.py
