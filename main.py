turningpoints = []
angel = []
time = []
night = []
timecorrect = []
angelcorrect = []
nightcorrect = []
results = []
datalength = 41761

with open('horizons_jupiter_io.txt') as f:  # import angels from file to table
    for i in range(1, datalength):
        read = f.readline(i)
        angel.append(read[23:-1])
f.close()
for i in range(31, len(angel)):  # correct data in table, because it does not import as it should from the file
    angelcorrect.append(angel[i])
with open('horizons_jupiter_io.txt') as f:  # import time from file to table
    for i in range(1, datalength):
        read = f.readline(i)
        time.append(read[1:-14])
f.close()
for i in range(31, len(time)):  # correct data in table, because it does not import as it should from the file
    timecorrect.append(time[i])
with open('horizons_jupiter_io.txt') as f:  # import state of the day from file to table
    for i in range(1, datalength):
        read = f.readline(i)
        night.append(read[19:-12])
f.close()
for i in range(31, len(night)):  # correct data in table, because it does not import as it should from the file
    nightcorrect.append(night[i])
for i in range(0, len(angelcorrect) - 1):  # take all the angels around 90° (with are the turningpoints)
    if nightcorrect[i] == ' ':  # look up if it is night, so an observation could be successful with good weather
        if 89.9 < float(angelcorrect[i]) < 90.1:  # and save the location where it is in the table, created above
            turningpoints.append(i)
for i in range(0, len(turningpoints) - 1):  # take the location and look it up in the table for the time, created above
    results.append(timecorrect[turningpoints[i]])
print(results)  # print time of the turningpoints
