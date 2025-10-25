##Supersonic
Group members: Tamanna Shabnam (vfc208) Jie Zhou (zlh638) SHIH-HSUEH LEE (vxp299)

This repository contains:*

Data project
Model project
Exam project
All code can be run with a standard Anaconda Distribution for Python 3.13.

DATA PROJECT

Our data project is an investigation of inflation dynamics in Denmark. This project explores how consumer prices have evolved before, during, and after the COVID-19 pandemic. It analyzes the Consumer Price Index (CPI) and its components, focusing on headline, core, and disaggregated inflation measures. The analysis examines monthly and annual inflation trends, as well as international comparisons with other economies such as the United States and China.

The project further investigates how different product categories contributed to overall inflation and when the post-pandemic inflation surge came to an end. By adjusting for factors like energy and food prices, it highlights the key drivers behind price fluctuations in Denmark.

The ultimate goal of this project is to identify the main patterns and determinants of inflation, providing insight into the timing, sources, and persistence of the inflation surge in Denmark.

The results of the project can be seen from running dataproject.ipynb.

To succesfully run this file it is reguired to run the dataproject.py file.

The data for this assignment has been collected from official economic databases, primarily Statistics Denmark (StatBank) and the Federal Reserve Economic Data (FRED).The Statistics Denmark datasets include detailed information from PRIS113 and PRIS111, which provide monthly consumer price indices (CPI) for Denmark — both overall and by product categories. The FRED database supplies Harmonized Index of Consumer Prices (HICP) data for international comparison with countries such as Austria, the Euro Area, and the United States.

It is important to note that this data reflects the price levels available at the time of collection. Since inflation figures are regularly updated as new data is released, running the code at a later date may yield slightly different results. Therefore, we advise not to rerun the data download cells at the start of the notebook if you wish to reproduce the exact same figures and interpretations presented in this analysis.

For the purpose of this analysis, the data has been cleaned and preprocessed to handle any missing or inconsistent data.

Dependencies: In order to effectively execute the code, the specific dependencies must be installed:

pandas (data manipulation) numpy (numerical operations) matplotlib & seaborn (plotting) requests (downloading data via API) statsmodels (if needed for analysis) Any package specific to Denmark Statistics (e.g. dstapi or similar if available) Please ensure these dependencies are installed in your Python environment to enable the flawless running of the code.
