import numpy as np
import datetime

input_file = "horizons_results.txt"
output_file = "filtered_interpolated_angles.txt"

timestamps, angles = [], []

# Read and process the file
with open(input_file, "r") as file:
    for line in file:
        if "$$SOE" in line:
            break  # Start processing after this
    for line in file:
        if "$$EOE" in line:
            break  # Stop processing at end of data

        parts = line.strip().split()
        if len(parts) < 3:
            continue  # Skip invalid lines

        try:
            timestamp = datetime.datetime.strptime(f"{parts[0]} {parts[1]}", "%Y-%b-%d %H:%M")
            angle = float(parts[-1])
            timestamps.append(timestamp)
            angles.append(angle)
        except ValueError:
            continue  # Skip lines with invalid data

timestamps, angles = np.array(timestamps), np.array(angles)

if len(angles) == 0:
    print("No valid data was read. Check the input file format.")
    exit()

print(f"Read {len(angles)} valid data points.")

# Find interpolated timestamps where the angle crosses 90°
interpolated_results = ["Filtered interpolated timestamps where angle is exactly 90°:\n"]
for i in range(len(angles) - 1):
    if (angles[i] < 90 < angles[i + 1]) or (angles[i] > 90 > angles[i + 1]):
        fraction = (90 - angles[i]) / (angles[i + 1] - angles[i])
        interpolated_time = timestamps[i] + (timestamps[i + 1] - timestamps[i]) * fraction
        interpolated_results.append(f"{interpolated_time}\n")

with open(output_file, "w") as file:
    file.writelines(interpolated_results)

print(f"Results saved to {output_file}")
