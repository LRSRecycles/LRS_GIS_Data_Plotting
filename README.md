CONTENTS

1. Code Explanation 
2. How to handle issues 
3. Future planning

Explanation: The code begins by importing two necessary libraries:

pandas: Used for data manipulation and analysis.
matplotlib.pyplot: A plotting library for creating visualizations like line graphs and polygons.

# Load the CSV file
file_path = 'Downloads/LRS_PROD (1).csv' 
data = pd.read_csv(file_path)
Explanation: The pandas.read_csv() function reads the CSV file 'Downloads/LRS_PROD (1).csv' into a DataFrame named data. This file is expected to contain GPS data, including longitudes and latitudes necessary for plotting a polygon.

# Checking for columns
print(data.columns)
Explanation: This line prints the column names of the DataFrame data to verify that the expected columns (such as CM04_LONG and CM04_LATT) exist.

# Drop rows with missing (NaN) values in 'CM04_LONG' and 'CM04_LATT'
data = data.dropna(subset=['CM04_LONG', 'CM04_LATT'])
Explanation: This step removes rows where either the CM04_LONG (longitude) or CM04_LATT (latitude) columns have missing or NaN values. This ensures that only valid GPS points are used in the plot.

# Extract latitude and longitude from the data
longitudes = data['CM04_LONG']
latitudes = data['CM04_LATT']
Explanation: Here, two variables longitudes and latitudes are created to store the longitude and latitude values from the DataFrame for use in the plot.

# Check if both longitudes and latitudes have the same length
print(f"Number of longitudes: {len(longitudes)} Number of latitudes: {len(latitudes)}")
Explanation: This line checks if the longitudes and latitudes arrays have the same number of points by printing their lengths. If they are not the same length, plotting will fail, so this is an important check.

# Ensure the polygon is closed by adding the first point at the end if necessary
if longitudes.iloc[0] != longitudes.iloc[-1] or latitudes.iloc[0] != latitudes.iloc[-1]:
    longitudes = list(longitudes)
    latitudes = list(latitudes)
    longitudes.append(longitudes[0])
    latitudes.append(latitudes[0])
Explanation: This part of the code ensures that the polygon is closed (i.e., the last point connects to the first point). If the first and last points are not the same, they are added to the end of the list to form a closed shape.

# Create a plot of the GPS points and form a polygon by connecting them
plt.figure(figsize=(8, 6))
plt.plot(longitudes, latitudes, marker='o', linestyle='-', color='b', label='GPS Points Line')
plt.fill(longitudes, latitudes, alpha=0.2, color='blue', label='Filled Polygon')
Explanation: This section uses matplotlib to create a figure and plot the GPS points as a polygon.
plt.plot() draws the line connecting the points.
plt.fill() fills the area inside the polygon with a light blue color.

# Labeling the plot
plt.title('Polygon formed by GPS Points')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.legend()
Explanation: The plot is given a title and labeled axes (Longitude and Latitude). A grid is added for reference, and a legend is created to show the labels for the line and the filled polygon.

# Show the plot
plt.show()
Explanation: Finally, plt.show() renders the plot.

# ISSUE HANDLING

# Why the Polygon is Not Showing:

Data Issues: If there are no valid longitude and latitude points after dropping the missing values, the plot will not display. The data check for this should be added.


Data Checks I am Currently Working On:

Handling Missing Values: Dropping any rows where either longitude or latitude is missing.
Data Validation: Checking if the number of points is sufficient to form a polygon.
Closing the Polygon: Ensuring the polygon is closed by appending the first point to the end of the list.

# FUTURE PLANNING

# What Extra Needs to be Done in Power BI Using ArcGIS (Once bugs are fixed):
In Power BI, using ArcGIS to map GPS data would require the following steps:

-Ensure that the GPS data being passed to Power BI is free from missing values and is formatted correctly.
-In Power BI, the ArcGIS visual can be used to map the longitude and latitude data.
-Configure layers for polygons in ArcGIS to visualize the shapes formed by the GPS points.
-ArcGIS in Power BI allows for more interactive mapping, where users can zoom in/out and explore geographical data.
