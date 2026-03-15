import pandas as pd
import matplotlib.pyplot as plt

# Simulated EDI transaction failure dataset
data = {
    "TradingPartner": ["A","B","A","C","B","A","C","B"],
    "DocType": ["850","810","850","856","810","850","856","810"],
    "Failures": [5,2,3,4,6,1,2,7],
    "Month": ["Jan","Jan","Feb","Feb","Mar","Mar","Mar","Apr"]
}

df = pd.DataFrame(data)

# Analyze total failures by trading partner
failures_by_partner = df.groupby("TradingPartner")["Failures"].sum()

print("Failures by Trading Partner:")
print(failures_by_partner)

# Plot failures
failures_by_partner.plot(kind="bar", title="EDI Failures by Trading Partner")
plt.show()
