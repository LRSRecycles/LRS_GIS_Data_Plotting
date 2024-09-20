# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Downloads/LRS_PROD (1).csv' 
data = pd.read_csv(file_path)
print(data.columns)

# Drop rows with missing (NaN) values in 'CM04_LONG' and 'CM04_LATT'
data = data.dropna(subset=['CM04_LONG', 'CM04_LATT'])

# Extract latitude and longitude from the data
longitudes = data['CM04_LONG']
latitudes = data['CM04_LATT']

# Check if both longitudes and latitudes have the same length
print(f"Number of longitudes: {len(longitudes)}, Number of latitudes: {len(latitudes)}")

# Ensure the polygon is closed by adding the first point at the end if necessary
if longitudes.iloc[0] != longitudes.iloc[-1] or latitudes.iloc[0] != latitudes.iloc[-1]:
   	longitudes = list(longitudes)
    latitudes = list(latitudes)
    longitudes.append(longitudes[0])
   	latitudes.append(latitudes[0])

# Create a plot of the GPS points and form a polygon by connecting them
plt.figure(figsize=(8, 6))
plt.plot(longitudes, latitudes, marker='o', linestyle='-', color='b', label='GPS Points Line')
plt.fill(longitudes, latitudes, alpha=0.2, color='blue', label='Filled Polygon')

#Labeling the plot
plt.title('Polygon formed by GPS Points')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
