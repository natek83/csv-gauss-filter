csv-gauss-filter.py

This filter will smooth out local variations between cells due to long term
trim noise but can't be used to interpolate or form regression lines to 
follow overall trends/patterns, using a wide radius will tend to bring all
cells towards a global average and would then have to be trimmed out again

Save the script in a working directory and save a .csv file of your fuel or
ve table cells named fuel.csv, then run the script.  I run it through the
spyder ide which has a nice "Variable explorer" tab to display the different
tables with color gradation and then tweak the filter parameters until I get
good results.  The default parameters work well for a 32x32 table.  Use a
smaller radius for smaller tables.
