#!/usr/bin/python
#include<stdio.h>
import code
import math
import cuts as ct
import ROOT as rt
from ROOT import TFile, TTree , TCanvas, TH1F, TList , TH2F ,TH3F ,TMath ,TF1, TStyle ,gStyle , TRefArray, TClonesArray, TObjArray, gPad, TPaveText, TLegend ,TString, TObject,gROOT,TFormula, TEllipse, TDirectory,TLorentzVector
from ROOT import TMath as mt
from datetime import date
# this code creates the histograms from the analysis results and also applies some additional cuts 
# however I am still new to the pyroot so I might be defining histogram more than I needed 
# my goal was to create just one set of histogram and clear it after every time I store them in root file for different level of cuts
# Different directory are created to store all the histogram at different level of cuts


#Opening the file>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
filename = "PolarizationSample"
infilename =filename+".root"
file = TFile.Open(infilename)
#file = TFile.Open("AnalysisResults.root")
list = TList()
list = file.Get("Polar")
tree = list.FindObject("result")
daughter = TLorentzVector()
#daughter = 
#tree2 = file.Get("tree2")

#tree2.AddFriend(tree)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
text = TPaveText(.05,.1,.95,.8)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#this is to use to run in batch mode  to avoid printing all the plots
gROOT.SetBatch(rt.kTRUE)
#this create the master canvas color and the entries to print
#gStyle.SetCanvasColor(22)
gStyle.SetOptStat("e")


#master canvas






Date = date.today()
date_today = filename+str(Date)+".root"
#print date_today

file2 = TFile(date_today,"Recreate")
# directory is created to fill histograms without cuts
# way to create a string as a variable

reference_frame = ["normal", "collinsoper","helicity"]



nframe = 0

while  nframe<len(reference_frame):
  folder = reference_frame[nframe]
  
  vars()[folder] = TDirectory()
  
  #folder = TDirectory()

  folder = file2.mkdir(reference_frame[nframe])
  
  
  folder.cd()
  costheta_binmax= 0.6
  costheta_binmin=-0.6
  costheta_bin1 = 100
  costheta_bin2 = 17
  # histogram = TH1F(hist,"",n_bin,xmin,xmax)
  hist_costheta =  TH1F("hist_costheta","",costheta_bin1,costheta_binmax,costheta_binmin)
  
  hist_costheta2 =  TH1F("hist_costheta2", "purityHv3",costheta_bin2,costheta_binmax,costheta_binmin)
  ytitle_costheta = "cos(#theta_{gen && rec on same bin})/cos(#theta_{generated})"
  xtitle_costheta = " cos(#theta_{generated})"
    
  hist_costheta.SetXTitle(xtitle_costheta)
  hist_costheta.SetYTitle(ytitle_costheta)
  hist_costheta.GetYaxis().SetTitleOffset(1.4)
  hist_costheta.GetYaxis().CenterTitle()
  hist_costheta.GetXaxis().CenterTitle()
    
  hist_costheta2.SetXTitle(xtitle_costheta)
  hist_costheta2.SetYTitle(ytitle_costheta)
  hist_costheta2.GetYaxis().SetTitleOffset(1.4)
  hist_costheta2.GetYaxis().CenterTitle()
  hist_costheta2.GetXaxis().CenterTitle()
  
  hist_costheta3 =  TH2F("hist_costheta2", "fBinMigrationHelicityH",25,-1,1,25,-1,1)
  
  xtitle_costheta3 = " cos(#theta_{generated})"
  ytitle_costheta3 = "cos(#theta_{reconstructed}"
  
  hist_costheta3.SetXTitle(xtitle_costheta3)
  hist_costheta3.SetYTitle(ytitle_costheta3)
  hist_costheta3.GetYaxis().SetTitleOffset(1.4)
  hist_costheta3.GetYaxis().CenterTitle()
  hist_costheta3.GetXaxis().CenterTitle()
  
  
  #angular_canvas = "canvas_{}".format(reference_frame[nframe])
  canvasname = "canvas_{}".format(reference_frame[nframe])
  
  ang_canvas1 = TCanvas(canvasname+"1","",600,300)
  ang_canvas1.cd()
  hist_costheta.Write()
  ang_canvas2 = TCanvas(canvasname+"2","",600,300)
  ang_canvas2.cd()
  hist_costheta2.Write()
  ang_canvas3 = TCanvas(canvasname+"3","",600,300)
  ang_canvas3.cd()
  hist_costheta3.Write()
  
 # canvas = TCanvas(hist,"",600,300)
  #tree.Draw("fcostheta>>")
  
  #cos theta
  #MuonPair_normal[15]
  
  #MuonPair_normal = TH1F()
  #Master_Canvas_normal= TCanvas()
  #histname_normal = []
 # cutlist_name = "cutlist_"+ reference_frame[nframe]
  cutlist_name = "cutlist_{}".format(reference_frame[nframe])
  
  
  
  #hist_name = "histname_"+reference_frame[nframe]
  hist_name = "histname_{}".format(reference_frame[nframe])
  #cutlist_name = [] #char[15]
  

  
  #nbins = 80 
  nfiles = len(hist_name)
  xmin=2.0
  xmax=6.0
  n_bin = 80
  i =0
 
  
  master_canvas = []
 # print vars()
  
  
  
  histograms = [] 
  #print vars()
  
  while i<nfiles:
    
    hist = TString()
  #  hist = hist_name + "_"+ str(i)
    hist = "{}_{}".format(hist_name,i)
    #print i
    #print hist 
    
   # i=i+1
    canvas = TCanvas(hist,"",600,300)
    histogram = TH1F(hist,"",n_bin,xmin,xmax)
    
    
  
    bin_width = (xmax-xmin)/n_bin
  
  
  
    #ytitle = "Number of Events/"+ str(bin_width) + " GeV/C #rightarrow"
    ytitle = "Number of Events/{}GeV/C #rightarrow".format(bin_width)
    
    histogram.SetXTitle("Invariant mass of #mu^+mu^- pair(GeV/C^2)#rightarrow")
    histogram.SetYTitle(ytitle)
    histogram.GetYaxis().SetTitleOffset(1.4)
    histogram.GetYaxis().CenterTitle()
    histogram.GetXaxis().CenterTitle()
    
    
  
  
    master_canvas.append(canvas)
    histograms.append(histogram)
    
    #tree.Draw("fM>>MuonPair[i]_normal",cutlist_normal[i],"")#need to define the cut parameter which will be on cos theta  
    master_canvas[i].cd()
    histograms[i].Draw()
    histograms[i].SetDirectory(0)
    master_canvas[i].Write()
    
    
    i= i+1
    #histogram.clear()
    #canvas.clear()
  folder.cd("../")
  nframe = nframe+1  
  
  #cos phi







file2.Write()
#tree.delete()

file2.Close()

# Mass

#The lines below are so that pyroot do not exit on completing the analysis
vars = globals()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()


