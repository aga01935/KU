#!/usr/bin/python
import code
import math
import cuts as ct
import ROOT as rt
from ROOT import TFile, TTree , TCanvas, TH1F, TList , TH2F ,TH3F ,TMath ,TF1, TStyle ,gStyle , TRefArray, TClonesArray, TObjArray, gPad, TPaveText, TLegend ,TString, TObject,gROOT,TFormula, TEllipse, TDirectory
from ROOT import TMath as mt
# this code creates the histograms from the analysis results and also applies some additional cuts 
# however I am still new to the pyroot so I might be defining histogram more than I needed 
# my goal was to create just one set of histogram and clear it after every time I store them in root file for different level of cuts
# Different directory are created to store all the histogram at different level of cuts


#Opening the file>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


file = TFile.Open("AnalysisResults.root")
list = TList()
list = file.Get("Polar/Helicity")
tree = list.FindObject("result")
tree2 = file.Get("tree2")

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
Master_Canvas = TCanvas("Master_Canvas","Master Canvas",600,300) # this is master canvas other will be cloned to this canvas
# master histograms here I will define the histograms 
  #master histograms for mass
fHistMass_MuPair = TH1F("fHistMass_MuPair","",100,0.8,2)
fHistMass_MuPair.SetXTitle("Mass of pa(GeV/C^2)#rightarrow")
fHistMass_MuPair.SetYTitle("Number of Events #rightarrow")
fHistMass_MuPair.GetYaxis().SetTitleOffset(1.4)
fHistMass_MuPair.SetLineWidth(2)
fHistMass_MuPair.SetLineColor(rt.kBlue)

  
  
  
phicanvas = Master_Canvas.Clone()
phicanvas.SetName("phicanvas")
phicanvas.cd()

func = TF1("func","pol2",0.5,1.5)



fHistDelPhi.SetDirectory(0)
func.SetLineColor(rt.kGreen)
func.Draw("SAME")

#this is where I start actually plotting
  # without cuts
    #mass
#file to fill the histograms after analysis
file2 = TFile("results.root","Recreate")
# directory is created to fill histograms without cuts
normal = TDirectory() 
normal = file2.mkdir("normal")

normal.cd()
Mass_0 = Master_Canvas.Clone()
Mass_0.SetName("Mass_")
fHistK = fHistMass_MuPair.Clone()
fHistK.SetName("fHistK")
Mass_0.cd()
tree.Draw("fM>>fHistK","","")
fHistK.SetDirectory(0)
Mass_0.Write()

Mass_1 = Master_Canvas.Clone()
Mass_1.SetName("Mass_1")
fHistMu = fHistMass_MuPair.Clone()
fHistMu.SetName("fHistMuon")
Mass_1.cd()
tree.Draw("fM>>fHistMuon","","")
fHistMu.SetDirectory(0)
Mass_1.Write()

 


###

elp = TEllipse(0,0,2,2)
elp.SetFillStyle(0)
elp.SetLineColor(rt.kRed)
elp.SetLineWidth(2)
gau = TF1("gau","gaus",-4,-10)
gau.SetLineWidth(3)
gau.SetLineColor(rt.kOrange)
gau2 = TF1("gau2","gaus",-2,0)
gau2.SetLineWidth(3)
gau2.SetLineColor(rt.kGreen)
gau3 = TF1("gau3","gaus(0)+gaus(3)",-12,2)
gau3.SetLineWidth(3)

#dirname.cd("../") takes me out of the directory 
normal.cd("../")


helicity = TDirectory() 
helicity = file2.mkdir("helicity")

helicity.cd()



#############################################################################################################
helicity.cd("../")
#helicity frame

collinsoper = TDirectory() 
collinsoper = file2.mkdir("collinsoper")

collinsoper.cd()
#plots after defining collinsoper frame



#############################################################################################################
collinsoper.cd("../")

#multiple folder can be added here
file2.Write()
#tree.delete()

file2.Close()

# Mass

#The lines below are so that pyroot do not exit on completing the analysis
vars = globals()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()


