import numpy as np

input_file = "horizons_results.txt"
output_file = "interpolated_angles.txt"

timestamps = []
angles = []

with open(input_file, "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 3:  # Ensure the line has enough parts
            try:
                timestamp = f"{parts[0]} {parts[1]}"  # Date and Time
                angle = float(parts[-1])  # Extract the last column (angle)
                timestamps.append(timestamp)
                angles.append(angle)
            except ValueError:
                continue  # Skip lines that do not contain valid numbers

timestamps = np.array(timestamps)
angles = np.array(angles)

# Find all intervals where the angle crosses 90° and interpolate
interpolated_results = ["Interpolated timestamps where angle is exactly 90°:\n"]

for i in range(len(angles) - 1):
    if (angles[i] < 90 and angles[i + 1] > 90) or (angles[i] > 90 and angles[i + 1] < 90):
        # Linear interpolation formula
        t1, t2 = timestamps[i], timestamps[i + 1]
        a1, a2 = angles[i], angles[i + 1]

        # Compute the fraction of the way between the two timestamps
        fraction = (90 - a1) / (a2 - a1)
        interpolated_time = f"Between {t1} and {t2}, interpolated at fraction {fraction:.4f}"

        interpolated_results.append(f"{interpolated_time}\n")

with open(output_file, "w") as file:
    file.writelines(interpolated_results)

print(f"Interpolated results saved to {output_file}")
