import pandas as pd
import sqlite3

# REAL DATA FROM 2024-25 EFA REPORT
efa_real = pd.DataFrame({
    'year': [2025],
    'hot_spring_efas': [49],
    'diverted_amt': [161146],
    'source': ['St. Johns + Calvary']
})

# HSSD enrollment (real from ADE 2024: ~4,750)
enroll_real = pd.DataFrame({
    'year': [2025],
    'students': [4750],
    'efa_loss_pct': [1.03],  # 49 / 4750
    'per_pupil': [7771],
    'gap': [161146]
})

# Save to DB
conn = sqlite3.connect('out/real_ed_funnel.db')
efa_real.to_sql('hot_efas', conn, if_exists='replace', index=False)
enroll_real.to_sql('hssd_enroll', conn, if_exists='replace', index=False)
conn.close()

print("REAL DATA SAVED: $161,146 diverted from HSSD in 2024-25")
print("Next: python src/02_link_real.py")
