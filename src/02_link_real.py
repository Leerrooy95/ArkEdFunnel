import pandas as pd
import sqlite3

conn = sqlite3.connect('out/real_ed_funnel.db')
df = pd.read_sql('SELECT * FROM hot_efas JOIN hssd_enroll USING (year)', conn)
conn.close()

df['deseg_risk'] = 1.5  # HSSD still under 1992 settlement
df['amplified_gap'] = df['gap'] * df['deseg_risk']
df['risk_score'] = (df['diverted_amt'] / 1e5) * (df['amplified_gap'] / 1e5)

df.to_csv('out/hssd_real_shortfall.csv', index=False)
print("\nREAL IMPACT (2025):")
print(df[['year', 'diverted_amt', 'amplified_gap', 'risk_score']])
