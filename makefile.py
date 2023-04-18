# Calculate carbon footprint by linear regression on energy usage, server usage and hardware consumption
X = np.array([energy_usage, server_usage, hardware_consumption]).T
y = np.array([1.2, 1.5, 1.7, 2.0, 2.1])
model = LinearRegression().fit(X, y)

# Calculate carbon footprint of current software development project
current_project = [1200, 70, 25]
carbon_footprint = model.predict([current_project])
print(f"Carbon Footprint of current project: {carbon_footprint}")
