# O-C Curve Analysis for Eclipsing Binary Systems
This project is designed to process and analyze data from eclipsing binary systems, focusing on variations in eclipse timing (O-C) over time. The results are visualized through plots that display the differences between observed and calculated eclipse times for both primary and secondary eclipses.

# Features
General Data Loading:

The script loads a CSV file (descarga.csv) containing general information about multiple binary systems, identified by their KIC (Kepler Input Catalog) number.
O-C File Processing:

A function is defined to load and process specific files for each system, containing O-C (Observed minus Calculated) data for eclipses.
The data is split into primary and secondary eclipses for detailed analysis.
O-C Plot Generation:

For each system, a plot is generated showing the O-C curves for both primary and secondary eclipses as a function of time (BJD - Barycentric Julian Date).
The plots are automatically saved as .png files, organized by the KIC identifier of the corresponding system.
Code Structure
Loading the General File:

The descarga.csv file is loaded at the start to obtain the KIC identifiers for all binary systems to be analyzed.
process_oc_file Function:

This function processes O-C data files, which contain eclipse timings. The data is filtered to separate primary eclipses from secondary ones.
Iteration and Processing:

The script iterates over each binary system listed in descarga.csv, searching for the corresponding O-C data files.
If the file is found, it is processed to extract and plot the O-C data.
Plot Generation:

The generated plots display the O-C variations over time, allowing for easy visualization of the data.
The images are saved in PNG format, with filenames that include the system's KIC identifier.
Execution
To run the code, ensure you have the following files and dependencies installed:

# Required Files:

descarga.csv: Contains the list of binary systems to be analyzed.
Individual O-C files for each system, named in the format [KIC].00.lc.etv.csv.
Dependencies:

Python 3.x
Pandas
Matplotlib
Glob
Usage
Place all required files in the same directory as the Python script.
Run the script. It will process the data and generate O-C plots for each binary system.
Contributions
Contributions to the project are welcome. If you have any suggestions or improvements, feel free to open a pull request or create an issue.
