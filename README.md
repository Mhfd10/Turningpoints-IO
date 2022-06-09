# Turningpoints-IO
Calculation of Io's turning points using Nasa's Horizons System

To determine the speed of light, one can observe the points of inflection at different times and compare them with the calculation, which results in differences and one can determine the speed of light, e.g. Rømer's method. In order to know when to observe the turning points, I have written this short python script.
1. Take from NASA's Horizons system the data for "Observer-Primary-Target angle" and adjust the rest of the settings as you need them.
2. Delete the text before and after the data as in the example "example.txt"
3. Rename the file to "horizons_jupiter_io.txt".
4. Move the file into the project folder in which you also have "main.py"
5. Run the script and it will print out all observable times for the turning points
