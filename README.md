# Turningpoints-IO
Calculation of Io's turning points using Nasa's Horizons System

To determine the speed of light, one can observe the inflection points at different times and compare them with the calculation, which results in differences and one can determine the speed of light, e.g. Rømer's method. To know when to observe the inflection points, I wrote this short Python script.
1. Make sure you have numpy installed
2. Take the data for "Observer-Primary-Target angle" from NASA's Horizons system and adjust the rest of the settings to your needs.
3. Put the file in your project folder.
4. Run the script and it will save all the observed times for the turnpoints as well as the linear interpolation in a separate file.
