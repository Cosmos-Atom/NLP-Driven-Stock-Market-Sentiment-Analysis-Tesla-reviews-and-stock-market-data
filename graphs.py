import matplotlib.pyplot as plt
import pandas as pd

# Data for dates and normalized sentiment scores
data = {
    "Date": [
        "11/24/2024", "11/23/2024", "11/22/2024", "11/21/2024", "11/20/2024",
        "11/19/2024", "11/18/2024", "11/17/2024", "11/16/2024", "11/15/2024",
        "11/14/2024", "11/13/2024", "11/12/2024", "11/11/2024", "11/10/2024",
        "11/09/2024", "11/08/2024", "11/07/2024", "11/06/2024", "11/05/2024",
        "11/04/2024", "11/03/2024", "11/02/2024", "11/01/2024", "10/31/2024",
        "10/30/2024", "10/29/2024", "10/28/2024", "10/27/2024", "10/26/2024"
    ],
    "Normalized Sentiment Score": [
        4.117378559, 3.448506384, 3.276886473, 3.403916726, 3.566129662,
        3.363169144, 3.851444519, 2.384450191, 2.915679775, 3.473519414,
        3.329143742, 2.352979886, 2.932321541, 2.707811256, 3.303525626,
        3.604944767, 4.463171486, 2.602597127, 2.778465073, 3.146696453,
        4.936073421, 3.89110458, 0, 4.068854766, 2.263621135,
        3.112102192, 3.001672877, 2.93464199, 4.629661307, 5
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert dates to datetime format and sort in ascending order
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date", ascending=False)

# Reverse x-axis manually
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Normalized Sentiment Score"], marker='o', linestyle='-', color='g', label='Normalized Sentiment Scores')
plt.gca().invert_xaxis()  # Reverse the x-axis
plt.title("Normalized Sentiment Scores Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Normalized Sentiment Score (0-5)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
