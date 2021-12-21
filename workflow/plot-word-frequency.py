# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#
# Input & Output
#
input_file = sys.argv[1]
output_file = sys.argv[2]

#
# Read the input file
#
df = pd.read_csv(input_file)

df = df.sort_values(by="count", ascending=False)
df["rank"] = np.arange(df.shape[0])

#
# Plot
#
# %%
sns.set_style("white")
sns.set(font_scale=1.2)
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(4, 4.5))

ax = sns.scatterplot(data=df, x="rank", y="count", linewidth=0.1, s=5)

ax.set_ylabel("Count")
ax.set_xlabel("Rank")
ax.set_yscale("log")
ax.set_xscale("log")
sns.despine()
fig.savefig(output_file, bbox_inches="tight", dpi=300)
