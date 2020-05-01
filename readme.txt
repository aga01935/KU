Date 5/1/2020............

These Analysis Codes are based on ALICE analysis tutorial
https://alice-doc.github.io/alice-analysis-tutorial/analysis/welcome.html

##### Purpose of this analysis to reproduce the result using this analysis note "2020-04-21-analysisnoteAfterARC.pdf" ########







The main analysis code is on Polarization.cxx
This code will apply basic cuts and save the required parameters in tree branch 
main goal is to trim and save the required parameters 



This code will run on Grid and output "AnalysisResults.root" file 

Histogram will be creadted using pyroot codes which is composed of 3 files



readhistogramtest.py----> 
  -This contains main analysis codes, it will access the AnalysisResult.root and perform additional analyis if required,fit using funtions defined in          "fitter.py" 
  
  -it will create "results.root" file with histograms 

cuts.py-----> additional cuts is defined on this file in terms of strings

fitter.py--> file with the functions with fit parameter



