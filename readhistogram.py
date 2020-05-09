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
  
  
n_bin = 80
bin_min =2
bin_max =6

bin_width = 80-2/6

bw = str(bin_width)

ytitle = "Number of Events/"+ bw + " GeV/C #rightarrow"
 
fHistMass_MuPair = TH1F("fHistMass_MuPair","",n_bin,bin_min,bin_max)
fHistMass_MuPair.SetXTitle("Invariant mass of #mu^+mu^- pair(GeV/C^2)#rightarrow")
fHistMass_MuPair.SetYTitle("Number of Events/0.050 GeV/C #rightarrow")
fHistMass_MuPair.GetYaxis().SetTi=.kBlue)




file2 = TFile("results.root","Recreate")
# directory is created to fill histograms without cuts
normal = TDirectory() 
normal = file2.mkdir("normal")


normal.cd()

#cos theta

MuonPair[15]=TH1F()
Master_Canvas[15] = TCanvas()
char *histname = new char[15]
char *histname = new cutlist[15]
int nbins=80,nfiles=15;
float xmin=2,xmax=6;
for (int i=0;i<nfiles;i++)
  sprintf(histname,"histo%d",i)
  Master_Canvas = TCanvas(histname,"",600,300)
  MuonPair[i] = new TH1F(histname,"",nbins,xmin,xmax)
  tree.Draw("fM>>MuonPair[i]",cutlist,"")#need to define the cut parameter which will be on cos theta  
  MuonPair[i].SetDirectory(0)
  Master_Canvas[i].Write()
  
  
  

#cos phi

MuonPair[25]=TH1F()
Master_Canvas[25] = TCanvas()
char *histname = new char[15]
char *histname = new cutlist[15]
int nbins=80,nfiles=15;
float xmin=2,xmax=6;
for (int i=0;i<nfiles;i++)
  sprintf(histname,"histo%d",i)
  Master_Canvas = TCanvas(histname,"",600,300)
  MuonPair[i] = new TH1F(histname,"",nbins,xmin,xmax)
  Master_Canvas[i].cd()
  tree.Draw("fM>>MuonPair[i]",cutlist,"")#need to define the cut parameter which will be on cos theta  
  MuonPair[i].SetDirectory(0)
  Master_Canvas[i].Write()  

normal.cd("../") 






helicity.cd()

#cos theta

MuonPair_helicity[15]=TH1F()
Master_Canvas_helicity[15] = TCanvas()
char *histname_helicity = new char[15]
#name of the histograms will be fille here


char *histname_helicity = new cutlist[15]
int nbins=80,nfiles=15;
float xmin=2,xmax=6;
for (int i=0;i<nfiles;i++)
  sprintf(histname,"histo%d",i)
  Master_Canvas_helicity = TCanvas(histname_helicity,"",600,300)
  MuonPair[i] = new TH1F(histname,"",nbins,xmin,xmax)
  tree.Draw("fM>>MuonPair[i]",cutlist,"")#need to define the cut parameter which will be on cos theta  
  MuonPair_helicity[i].SetDirectory(0)
  Master_Canvas_helicity[i].Write()
  
  
  

#cos phi

MuonPair[25]=TH1F()
Master_Canvas[25] = TCanvas()
char *histname = new char[15]
char *histname = new cutlist[15]
int nbins=80,nfiles=15;
float xmin=2,xmax=6;
for (int i=0;i<nfiles;i++)
  sprintf(histname,"histo%d",i)
  Master_Canvas = TCanvas(histname,"",600,300)
  MuonPair[i] = new TH1F(histname,"",nbins,xmin,xmax)
  Master_Canvas[i].cd()
  tree.Draw("fM>>MuonPair[i]",cutlist,"")#need to define the cut parameter which will be on cos theta  
  MuonPair[i].SetDirectory(0)
  Master_Canvas[i].Write()  

helicity.cd("../") 

















  
  



#this is where I start actually plotting
  # without cuts
    #mass
#file to fill the histograms after analysis
"""file2 = TFile("results.root","Recreate")
# directory is created to fill histograms without cuts
normal = TDirectory() 
normal = file2.mkdir("normal")

normal.cd()
Mass_Costheta1 = Master_Canvas.Clone()
Mass_Costheta1.SetName("Mass_Costheta1")
fHistCostheta_Muon1 = fHistMass_MuPair.Clone()
fHistCostheta_Muon1.SetName("fHistCostheta_Muon1")
Mass_Costheta1.cd()
tree.Draw("fM>>fHistCostheta_Muon1","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon1.SetDirectory(0)
Mass_Costheta1.Write()





Mass_Costheta2 = Master_Canvas.Clone()
Mass_Costheta2.SetName("Mass_Costheta2")
fHistCostheta_Muon2 = fHistMass_MuPair.Clone()
fHistCostheta_Muon2.SetName("fHistCostheta_Muon2")
Mass_Costheta2.cd()
tree.Draw("fM>>fHistCostheta_Muon2","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon2.SetDirectory(0)
Mass_Costheta2.Write()


Mass_Costheta3 = Master_Canvas.Clone()
Mass_Costheta3.SetName("Mass_Costheta3")
fHistCostheta_Muon3 = fHistMass_MuPair.Clone()
fHistCostheta_Muon3.SetName("fHistCostheta_Muon3")
Mass_Costheta3.cd()
tree.Draw("fM>>fHistCostheta_Muon3","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon3.SetDirectory(0)
Mass_Costheta3.Write()





Mass_Costheta4 = Master_Canvas.Clone()
Mass_Costheta4.SetName("Mass_Costheta4")
fHistCostheta_Muon4 = fHistMass_MuPair.Clone()
fHistCostheta_Muon4.SetName("fHistCostheta_Muon4")
Mass_Costheta4.cd()
tree.Draw("fM>>fHistCostheta_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon4.SetDirectory(0)
Mass_Costheta4.Write()





Mass_Costheta4 = Master_Canvas.Clone()
Mass_Costheta4.SetName("Mass_Costheta4")
fHistCostheta_Muon4 = fHistMass_MuPair.Clone()
fHistCostheta_Muon4.SetName("fHistCostheta_Muon4")
Mass_Costheta4.cd()
tree.Draw("fM>>fHistCostheta_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon4.SetDirectory(0)
Mass_Costheta4.Write()



Mass_Costheta5 = Master_Canvas.Clone()
Mass_Costheta5.SetName("Mass_Costheta5")
fHistCostheta_Muon5 = fHistMass_MuPair.Clone()
fHistCostheta_Muon5.SetName("fHistCostheta_Muon5")
Mass_Costheta5.cd()
tree.Draw("fM>>fHistCostheta_Muon5","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon5.SetDirectory(0)
Mass_Costheta5.Write()





Mass_Costheta6 = Master_Canvas.Clone()
Mass_Costheta6.SetName("Mass_Costheta6")
fHistCostheta_Muon6 = fHistMass_MuPair.Clone()
fHistCostheta_Muon6.SetName("fHistCostheta_Muon6")
Mass_Costheta6.cd()
tree.Draw("fM>>fHistCostheta_Muon6","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon6.SetDirectory(0)
Mass_Costheta6.Write()






Mass_Costheta7 = Master_Canvas.Clone()
Mass_Costheta7.SetName("Mass_Costheta7")
fHistCostheta_Muon7 = fHistMass_MuPair.Clone()
fHistCostheta_Muon7.SetName("fHistCostheta_Muon7")
Mass_Costheta7.cd()
tree.Draw("fM>>fHistCostheta_Muon7","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon7.SetDirectory(0)
Mass_Costheta7.Write()




Mass_Costheta8 = Master_Canvas.Clone()
Mass_Costheta8.SetName("Mass_Costheta8")
fHistCostheta_Muon8 = fHistMass_MuPair.Clone()
fHistCostheta_Muon8.SetName("fHistCostheta_Muon8")
Mass_Costheta8.cd()
tree.Draw("fM>>fHistCostheta_Muon8","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon8.SetDirectory(0)
Mass_Costheta8.Write()



Mass_Costheta9 = Master_Canvas.Clone()
Mass_Costheta9.SetName("Mass_Costheta9")
fHistCostheta_Muon9 = fHistMass_MuPair.Clone()
fHistCostheta_Muon9.SetName("fHistCostheta_Muon9")
Mass_Costheta9.cd()
tree.Draw("fM>>fHistCostheta_Muon9","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon9.SetDirectory(0)
Mass_Costheta9.Write()


Mass_Costheta10 = Master_Canvas.Clone()
Mass_Costheta10.SetName("Mass_Costheta10")
fHistCostheta_Muon10 = fHistMass_MuPair.Clone()
fHistCostheta_Muon10.SetName("fHistCostheta_Muon10")
Mass_Costheta10.cd()
tree.Draw("fM>>fHistCostheta_Muon10","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon10.SetDirectory(0)
Mass_Costheta10.Write()





Mass_Costheta11 = Master_Canvas.Clone()
Mass_Costheta11.SetName("Mass_Costheta11")
fHistCostheta_Muon11 = fHistMass_MuPair.Clone()
fHistCostheta_Muon11.SetName("fHistCostheta_Muon11")
Mass_Costheta11.cd()
tree.Draw("fM>>fHistCostheta_Muon11","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon11.SetDirectory(0)
Mass_Costheta11.Write()






Mass_Costheta12 = Master_Canvas.Clone()
Mass_Costheta12.SetName("Mass_Costheta12")
fHistCostheta_Muon12 = fHistMass_MuPair.Clone()
fHistCostheta_Muon12.SetName("fHistCostheta_Muon12")
Mass_Costheta12.cd()
tree.Draw("fM>>fHistCostheta_Muon12","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon12.SetDirectory(0)
Mass_Costheta12.Write()


Mass_Costheta13 = Master_Canvas.Clone()
Mass_Costheta13.SetName("Mass_Costheta13")
fHistCostheta_Muon13 = fHistMass_MuPair.Clone()
fHistCostheta_Muon13.SetName("fHistCostheta_Muon13")
Mass_Costheta13.cd()
tree.Draw("fM>>fHistCostheta_Muon13","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon13.SetDirectory(0)
Mass_Costheta13.Write()





Mass_Costheta14 = Master_Canvas.Clone()
Mass_Costheta14.SetName("Mass_Costheta14")
fHistCostheta_Muon14 = fHistMass_MuPair.Clone()
fHistCostheta_Muon14.SetName("fHistCostheta_Muon14")
Mass_Costheta14.cd()
tree.Draw("fM>>fHistCostheta_Muon14","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon14.SetDirectory(0)
Mass_Costheta14.Write()









Mass_Costheta15 = Master_Canvas.Clone()
Mass_Costheta15.SetName("Mass_Costheta15")
fHistCostheta_Muon15 = fHistMass_MuPair.Clone()
fHistCostheta_Muon15.SetName("fHistCostheta_Muon15")
Mass_Costheta15.cd()
tree.Draw("fM>>fHistCostheta_Muon15","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon15.SetDirectory(0)
Mass_Costheta15.Write()





Mass_Costheta16 = Master_Canvas.Clone()
Mass_Costheta16.SetName("Mass_Costheta16")
fHistCostheta_Muon16 = fHistMass_MuPair.Clone()
fHistCostheta_Muon16.SetName("fHistCostheta_Muon16")
Mass_Costheta16.cd()
tree.Draw("fM>>fHistCostheta_Muon16","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon16.SetDirectory(0)
Mass_Costheta16.Write()






Mass_Costheta17 = Master_Canvas.Clone()
Mass_Costheta17.SetName("Mass_Costheta17")
fHistCostheta_Muon17 = fHistMass_MuPair.Clone()
fHistCostheta_Muon17.SetName("fHistCostheta_Muon17")
Mass_Costheta17.cd()
tree.Draw("fM>>fHistCostheta_Muon17","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon17.SetDirectory(0)
Mass_Costheta17.Write()




Mass_Costheta18 = Master_Canvas.Clone()
Mass_Costheta18.SetName("Mass_Costheta18")
fHistCostheta_Muon18 = fHistMass_MuPair.Clone()
fHistCostheta_Muon18.SetName("fHistCostheta_Muon18")
Mass_Costheta18.cd()
tree.Draw("fM>>fHistCostheta_Muon18","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon18.SetDirectory(0)
Mass_Costheta18.Write()


Mass_Costheta19 = Master_Canvas.Clone()
Mass_Costheta19.SetName("Mass_Costheta19")
fHistCostheta_Muon19 = fHistMass_MuPair.Clone()
fHistCostheta_Muon19.SetName("fHistCostheta_Muon19")
Mass_Costheta19.cd()
tree.Draw("fM>>fHistCostheta_Muon19","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon19.SetDirectory(0)
Mass_Costheta19.Write()



Mass_Costheta20 = Master_Canvas.Clone()
Mass_Costheta20.SetName("Mass_Costheta20")
fHistCostheta_Muon20 = fHistMass_MuPair.Clone()
fHistCostheta_Muon20.SetName("fHistCostheta_Muon20")
Mass_Costheta20.cd()
tree.Draw("fM>>fHistCostheta_Muon20","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon20.SetDirectory(0)
Mass_Costheta20.Write()



Mass_Costheta21 = Master_Canvas.Clone()
Mass_Costheta21.SetName("Mass_Costheta21")
fHistCostheta_Muon21 = fHistMass_MuPair.Clone()
fHistCostheta_Muon21.SetName("fHistCostheta_Muon21")
Mass_Costheta21.cd()
tree.Draw("fM>>fHistCostheta_Muon21","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon21.SetDirectory(0)
Mass_Costheta21.Write()





Mass_Costheta22 = Master_Canvas.Clone()
Mass_Costheta22.SetName("Mass_Costheta22")
fHistCostheta_Muon22 = fHistMass_MuPair.Clone()
fHistCostheta_Muon22.SetName("fHistCostheta_Muon22")
Mass_Costheta22.cd()
tree.Draw("fM>>fHistCostheta_Muon22","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon22.SetDirectory(0)
Mass_Costheta22.Write()


Mass_Costheta23 = Master_Canvas.Clone()
Mass_Costheta23.SetName("Mass_Costheta23")
fHistCostheta_Muon23 = fHistMass_MuPair.Clone()
fHistCostheta_Muon23.SetName("fHistCostheta_Muon23")
Mass_Costheta23.cd()
tree.Draw("fM>>fHistCostheta_Muon23","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon23.SetDirectory(0)
Mass_Costheta23.Write()







Mass_Costheta24 = Master_Canvas.Clone()
Mass_Costheta24.SetName("Mass_Costheta24")
fHistCostheta_Muon24 = fHistMass_MuPair.Clone()
fHistCostheta_Muon24.SetName("fHistCostheta_Muon24")
Mass_Costheta24.cd()
tree.Draw("fM>>fHistCostheta_Muon24","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon24.SetDirectory(0)
Mass_Costheta24.Write()



Mass_Costheta25 = Master_Canvas.Clone()
Mass_Costheta25.SetName("Mass_Costheta25")
fHistCostheta_Muon25 = fHistMass_MuPair.Clone()
fHistCostheta_Muon25.SetName("fHistCostheta_Muon25")
Mass_Costheta25.cd()
tree.Draw("fM>>fHistCostheta_Muon25","","")#need to define the cut parameter which will be on cos theta
fHistCostheta_Muon25.SetDirectory(0)
Mass_Costheta25.Write()












Mass_CosPhi1 = Master_Canvas.Clone()
Mass_CosPhi1.SetName("Mass_CosPhi1")
fHistCosPhi_Muon1 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon1.SetName("fHistCosPhi_Muon1")
Mass_CosPhi1.cd()
tree.Draw("fM>>fHistCosPhi_Muon1","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon1.SetDirectory(0)
Mass_CosPhi1.Write()





Mass_CosPhi2 = Master_Canvas.Clone()
Mass_CosPhi2.SetName("Mass_CosPhi2")
fHistCosPhi_Muon2 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon2.SetName("fHistCosPhi_Muon2")
Mass_CosPhi2.cd()
tree.Draw("fM>>fHistCosPhi_Muon2","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon2.SetDirectory(0)
Mass_CosPhi2.Write()


Mass_CosPhi3 = Master_Canvas.Clone()
Mass_CosPhi3.SetName("Mass_CosPhi3")
fHistCosPhi_Muon3 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon3.SetName("fHistCosPhi_Muon3")
Mass_CosPhi3.cd()
tree.Draw("fM>>fHistCosPhi_Muon3","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon3.SetDirectory(0)
Mass_CosPhi3.Write()





Mass_CosPhi4 = Master_Canvas.Clone()
Mass_CosPhi4.SetName("Mass_CosPhi4")
fHistCosPhi_Muon4 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon4.SetName("fHistCosPhi_Muon4")
Mass_CosPhi4.cd()
tree.Draw("fM>>fHistCosPhi_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon4.SetDirectory(0)
Mass_CosPhi4.Write()





Mass_CosPhi4 = Master_Canvas.Clone()
Mass_CosPhi4.SetName("Mass_CosPhi4")
fHistCosPhi_Muon4 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon4.SetName("fHistCosPhi_Muon4")
Mass_CosPhi4.cd()
tree.Draw("fM>>fHistCosPhi_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon4.SetDirectory(0)
Mass_CosPhi4.Write()



Mass_CosPhi5 = Master_Canvas.Clone()
Mass_CosPhi5.SetName("Mass_CosPhi5")
fHistCosPhi_Muon5 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon5.SetName("fHistCosPhi_Muon5")
Mass_CosPhi5.cd()
tree.Draw("fM>>fHistCosPhi_Muon5","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon5.SetDirectory(0)
Mass_CosPhi5.Write()





Mass_CosPhi6 = Master_Canvas.Clone()
Mass_CosPhi6.SetName("Mass_CosPhi6")
fHistCosPhi_Muon6 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon6.SetName("fHistCosPhi_Muon6")
Mass_CosPhi6.cd()
tree.Draw("fM>>fHistCosPhi_Muon6","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon6.SetDirectory(0)
Mass_CosPhi6.Write()






Mass_CosPhi7 = Master_Canvas.Clone()
Mass_CosPhi7.SetName("Mass_CosPhi7")
fHistCosPhi_Muon7 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon7.SetName("fHistCosPhi_Muon7")
Mass_CosPhi7.cd()
tree.Draw("fM>>fHistCosPhi_Muon7","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon7.SetDirectory(0)
Mass_CosPhi7.Write()




Mass_CosPhi8 = Master_Canvas.Clone()
Mass_CosPhi8.SetName("Mass_CosPhi8")
fHistCosPhi_Muon8 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon8.SetName("fHistCosPhi_Muon8")
Mass_CosPhi8.cd()
tree.Draw("fM>>fHistCosPhi_Muon8","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon8.SetDirectory(0)
Mass_CosPhi8.Write()



Mass_CosPhi9 = Master_Canvas.Clone()
Mass_CosPhi9.SetName("Mass_CosPhi9")
fHistCosPhi_Muon9 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon9.SetName("fHistCosPhi_Muon9")
Mass_CosPhi9.cd()
tree.Draw("fM>>fHistCosPhi_Muon9","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon9.SetDirectory(0)
Mass_CosPhi9.Write()


Mass_CosPhi10 = Master_Canvas.Clone()
Mass_CosPhi10.SetName("Mass_CosPhi10")
fHistCosPhi_Muon10 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon10.SetName("fHistCosPhi_Muon10")
Mass_CosPhi10.cd()
tree.Draw("fM>>fHistCosPhi_Muon10","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon10.SetDirectory(0)
Mass_CosPhi10.Write()





Mass_CosPhi11 = Master_Canvas.Clone()
Mass_CosPhi11.SetName("Mass_CosPhi11")
fHistCosPhi_Muon11 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon11.SetName("fHistCosPhi_Muon11")
Mass_CosPhi11.cd()
tree.Draw("fM>>fHistCosPhi_Muon11","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon11.SetDirectory(0)
Mass_CosPhi11.Write()






Mass_CosPhi12 = Master_Canvas.Clone()
Mass_CosPhi12.SetName("Mass_CosPhi12")
fHistCosPhi_Muon12 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon12.SetName("fHistCosPhi_Muon12")
Mass_CosPhi12.cd()
tree.Draw("fM>>fHistCosPhi_Muon12","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon12.SetDirectory(0)
Mass_CosPhi12.Write()


Mass_CosPhi13 = Master_Canvas.Clone()
Mass_CosPhi13.SetName("Mass_CosPhi13")
fHistCosPhi_Muon13 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon13.SetName("fHistCosPhi_Muon13")
Mass_CosPhi13.cd()
tree.Draw("fM>>fHistCosPhi_Muon13","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon13.SetDirectory(0)
Mass_CosPhi13.Write()





Mass_CosPhi14 = Master_Canvas.Clone()
Mass_CosPhi14.SetName("Mass_CosPhi14")
fHistCosPhi_Muon14 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon14.SetName("fHistCosPhi_Muon14")
Mass_CosPhi14.cd()
tree.Draw("fM>>fHistCosPhi_Muon14","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon14.SetDirectory(0)
Mass_CosPhi14.Write()









Mass_CosPhi15 = Master_Canvas.Clone()
Mass_CosPhi15.SetName("Mass_CosPhi15")
fHistCosPhi_Muon15 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon15.SetName("fHistCosPhi_Muon15")
Mass_CosPhi15.cd()
tree.Draw("fM>>fHistCosPhi_Muon15","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon15.SetDirectory(0)
Mass_CosPhi15.Write()





Mass_CosPhi16 = Master_Canvas.Clone()
Mass_CosPhi16.SetName("Mass_CosPhi16")
fHistCosPhi_Muon16 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon16.SetName("fHistCosPhi_Muon16")
Mass_CosPhi16.cd()
tree.Draw("fM>>fHistCosPhi_Muon16","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon16.SetDirectory(0)
Mass_CosPhi16.Write()






Mass_CosPhi17 = Master_Canvas.Clone()
Mass_CosPhi17.SetName("Mass_CosPhi17")
fHistCosPhi_Muon17 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon17.SetName("fHistCosPhi_Muon17")
Mass_CosPhi17.cd()
tree.Draw("fM>>fHistCosPhi_Muon17","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon17.SetDirectory(0)
Mass_CosPhi17.Write()




Mass_CosPhi18 = Master_Canvas.Clone()
Mass_CosPhi18.SetName("Mass_CosPhi18")
fHistCosPhi_Muon18 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon18.SetName("fHistCosPhi_Muon18")
Mass_CosPhi18.cd()
tree.Draw("fM>>fHistCosPhi_Muon18","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon18.SetDirectory(0)
Mass_CosPhi18.Write()


Mass_CosPhi19 = Master_Canvas.Clone()
Mass_CosPhi19.SetName("Mass_CosPhi19")
fHistCosPhi_Muon19 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon19.SetName("fHistCosPhi_Muon19")
Mass_CosPhi19.cd()
tree.Draw("fM>>fHistCosPhi_Muon19","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon19.SetDirectory(0)
Mass_CosPhi19.Write()



Mass_CosPhi20 = Master_Canvas.Clone()
Mass_CosPhi20.SetName("Mass_CosPhi20")
fHistCosPhi_Muon20 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon20.SetName("fHistCosPhi_Muon20")
Mass_CosPhi20.cd()
tree.Draw("fM>>fHistCosPhi_Muon20","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon20.SetDirectory(0)
Mass_CosPhi20.Write()



Mass_CosPhi21 = Master_Canvas.Clone()
Mass_CosPhi21.SetName("Mass_CosPhi21")
fHistCosPhi_Muon21 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon21.SetName("fHistCosPhi_Muon21")
Mass_CosPhi21.cd()
tree.Draw("fM>>fHistCosPhi_Muon21","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon21.SetDirectory(0)
Mass_CosPhi21.Write()





Mass_CosPhi22 = Master_Canvas.Clone()
Mass_CosPhi22.SetName("Mass_CosPhi22")
fHistCosPhi_Muon22 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon22.SetName("fHistCosPhi_Muon22")
Mass_CosPhi22.cd()
tree.Draw("fM>>fHistCosPhi_Muon22","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon22.SetDirectory(0)
Mass_CosPhi22.Write()


Mass_CosPhi23 = Master_Canvas.Clone()
Mass_CosPhi23.SetName("Mass_CosPhi23")
fHistCosPhi_Muon23 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon23.SetName("fHistCosPhi_Muon23")
Mass_CosPhi23.cd()
tree.Draw("fM>>fHistCosPhi_Muon23","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon23.SetDirectory(0)
Mass_CosPhi23.Write()







Mass_CosPhi24 = Master_Canvas.Clone()
Mass_CosPhi24.SetName("Mass_CosPhi24")
fHistCosPhi_Muon24 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon24.SetName("fHistCosPhi_Muon24")
Mass_CosPhi24.cd()
tree.Draw("fM>>fHistCosPhi_Muon24","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon24.SetDirectory(0)
Mass_CosPhi24.Write()



Mass_CosPhi25 = Master_Canvas.Clone()
Mass_CosPhi25.SetName("Mass_CosPhi25")
fHistCosPhi_Muon25 = fHistMass_MuPair.Clone()
fHistCosPhi_Muon25.SetName("fHistCosPhi_Muon25")
Mass_CosPhi25.cd()
tree.Draw("fM>>fHistCosPhi_Muon25","","")#need to define the cut parameter which will be on cos theta
fHistCosPhi_Muon25.SetDirectory(0)
Mass_CosPhi25.Write()





























### this is the sample ellipse which I will use to circle the area I am interested ielp = TEllipse(0,0,elp.SetFillStyle(
elp.SetLineColor(rt.kRed)
elp.SetLineWidth(2)

#dirname.cd("../") takes me out of the directory 
normal.cd("../")


helicity = TDirectory() 
helicity = file2.mkdir("helicity")

helicity.cd()





Mass_HeliCity_Costheta1 = Master_Canvas.Clone()
Mass_HeliCity_Costheta1.SetName("Mass_HeliCity_Costheta1")
fHistHeliCity_Costheta_Muon1 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon1.SetName("fHistHeliCity_Costheta_Muon1")
Mass_HeliCity_Costheta1.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon1","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon1.SetDirectory(0)
Mass_HeliCity_Costheta1.Write()





Mass_HeliCity_Costheta2 = Master_Canvas.Clone()
Mass_HeliCity_Costheta2.SetName("Mass_HeliCity_Costheta2")
fHistHeliCity_Costheta_Muon2 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon2.SetName("fHistHeliCity_Costheta_Muon2")
Mass_HeliCity_Costheta2.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon2","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon2.SetDirectory(0)
Mass_HeliCity_Costheta2.Write()


Mass_HeliCity_Costheta3 = Master_Canvas.Clone()
Mass_HeliCity_Costheta3.SetName("Mass_HeliCity_Costheta3")
fHistHeliCity_Costheta_Muon3 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon3.SetName("fHistHeliCity_Costheta_Muon3")
Mass_HeliCity_Costheta3.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon3","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon3.SetDirectory(0)
Mass_HeliCity_Costheta3.Write()





Mass_HeliCity_Costheta4 = Master_Canvas.Clone()
Mass_HeliCity_Costheta4.SetName("Mass_HeliCity_Costheta4")
fHistHeliCity_Costheta_Muon4 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon4.SetName("fHistHeliCity_Costheta_Muon4")
Mass_HeliCity_Costheta4.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon4.SetDirectory(0)
Mass_HeliCity_Costheta4.Write()





Mass_HeliCity_Costheta4 = Master_Canvas.Clone()
Mass_HeliCity_Costheta4.SetName("Mass_HeliCity_Costheta4")
fHistHeliCity_Costheta_Muon4 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon4.SetName("fHistHeliCity_Costheta_Muon4")
Mass_HeliCity_Costheta4.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon4.SetDirectory(0)
Mass_HeliCity_Costheta4.Write()



Mass_HeliCity_Costheta5 = Master_Canvas.Clone()
Mass_HeliCity_Costheta5.SetName("Mass_HeliCity_Costheta5")
fHistHeliCity_Costheta_Muon5 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon5.SetName("fHistHeliCity_Costheta_Muon5")
Mass_HeliCity_Costheta5.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon5","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon5.SetDirectory(0)
Mass_HeliCity_Costheta5.Write()





Mass_HeliCity_Costheta6 = Master_Canvas.Clone()
Mass_HeliCity_Costheta6.SetName("Mass_HeliCity_Costheta6")
fHistHeliCity_Costheta_Muon6 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon6.SetName("fHistHeliCity_Costheta_Muon6")
Mass_HeliCity_Costheta6.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon6","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon6.SetDirectory(0)
Mass_HeliCity_Costheta6.Write()






Mass_HeliCity_Costheta7 = Master_Canvas.Clone()
Mass_HeliCity_Costheta7.SetName("Mass_HeliCity_Costheta7")
fHistHeliCity_Costheta_Muon7 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon7.SetName("fHistHeliCity_Costheta_Muon7")
Mass_HeliCity_Costheta7.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon7","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon7.SetDirectory(0)
Mass_HeliCity_Costheta7.Write()




Mass_HeliCity_Costheta8 = Master_Canvas.Clone()
Mass_HeliCity_Costheta8.SetName("Mass_HeliCity_Costheta8")
fHistHeliCity_Costheta_Muon8 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon8.SetName("fHistHeliCity_Costheta_Muon8")
Mass_HeliCity_Costheta8.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon8","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon8.SetDirectory(0)
Mass_HeliCity_Costheta8.Write()



Mass_HeliCity_Costheta9 = Master_Canvas.Clone()
Mass_HeliCity_Costheta9.SetName("Mass_HeliCity_Costheta9")
fHistHeliCity_Costheta_Muon9 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon9.SetName("fHistHeliCity_Costheta_Muon9")
Mass_HeliCity_Costheta9.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon9","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon9.SetDirectory(0)
Mass_HeliCity_Costheta9.Write()


Mass_HeliCity_Costheta10 = Master_Canvas.Clone()
Mass_HeliCity_Costheta10.SetName("Mass_HeliCity_Costheta10")
fHistHeliCity_Costheta_Muon10 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon10.SetName("fHistHeliCity_Costheta_Muon10")
Mass_HeliCity_Costheta10.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon10","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon10.SetDirectory(0)
Mass_HeliCity_Costheta10.Write()





Mass_HeliCity_Costheta11 = Master_Canvas.Clone()
Mass_HeliCity_Costheta11.SetName("Mass_HeliCity_Costheta11")
fHistHeliCity_Costheta_Muon11 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon11.SetName("fHistHeliCity_Costheta_Muon11")
Mass_HeliCity_Costheta11.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon11","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon11.SetDirectory(0)
Mass_HeliCity_Costheta11.Write()






Mass_HeliCity_Costheta12 = Master_Canvas.Clone()
Mass_HeliCity_Costheta12.SetName("Mass_HeliCity_Costheta12")
fHistHeliCity_Costheta_Muon12 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon12.SetName("fHistHeliCity_Costheta_Muon12")
Mass_HeliCity_Costheta12.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon12","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon12.SetDirectory(0)
Mass_HeliCity_Costheta12.Write()


Mass_HeliCity_Costheta13 = Master_Canvas.Clone()
Mass_HeliCity_Costheta13.SetName("Mass_HeliCity_Costheta13")
fHistHeliCity_Costheta_Muon13 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon13.SetName("fHistHeliCity_Costheta_Muon13")
Mass_HeliCity_Costheta13.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon13","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon13.SetDirectory(0)
Mass_HeliCity_Costheta13.Write()





Mass_HeliCity_Costheta14 = Master_Canvas.Clone()
Mass_HeliCity_Costheta14.SetName("Mass_HeliCity_Costheta14")
fHistHeliCity_Costheta_Muon14 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon14.SetName("fHistHeliCity_Costheta_Muon14")
Mass_HeliCity_Costheta14.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon14","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon14.SetDirectory(0)
Mass_HeliCity_Costheta14.Write()









Mass_HeliCity_Costheta15 = Master_Canvas.Clone()
Mass_HeliCity_Costheta15.SetName("Mass_HeliCity_Costheta15")
fHistHeliCity_Costheta_Muon15 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon15.SetName("fHistHeliCity_Costheta_Muon15")
Mass_HeliCity_Costheta15.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon15","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon15.SetDirectory(0)
Mass_HeliCity_Costheta15.Write()





Mass_HeliCity_Costheta16 = Master_Canvas.Clone()
Mass_HeliCity_Costheta16.SetName("Mass_HeliCity_Costheta16")
fHistHeliCity_Costheta_Muon16 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon16.SetName("fHistHeliCity_Costheta_Muon16")
Mass_HeliCity_Costheta16.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon16","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon16.SetDirectory(0)
Mass_HeliCity_Costheta16.Write()






Mass_HeliCity_Costheta17 = Master_Canvas.Clone()
Mass_HeliCity_Costheta17.SetName("Mass_HeliCity_Costheta17")
fHistHeliCity_Costheta_Muon17 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon17.SetName("fHistHeliCity_Costheta_Muon17")
Mass_HeliCity_Costheta17.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon17","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon17.SetDirectory(0)
Mass_HeliCity_Costheta17.Write()




Mass_HeliCity_Costheta18 = Master_Canvas.Clone()
Mass_HeliCity_Costheta18.SetName("Mass_HeliCity_Costheta18")
fHistHeliCity_Costheta_Muon18 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon18.SetName("fHistHeliCity_Costheta_Muon18")
Mass_HeliCity_Costheta18.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon18","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon18.SetDirectory(0)
Mass_HeliCity_Costheta18.Write()


Mass_HeliCity_Costheta19 = Master_Canvas.Clone()
Mass_HeliCity_Costheta19.SetName("Mass_HeliCity_Costheta19")
fHistHeliCity_Costheta_Muon19 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon19.SetName("fHistHeliCity_Costheta_Muon19")
Mass_HeliCity_Costheta19.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon19","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon19.SetDirectory(0)
Mass_HeliCity_Costheta19.Write()



Mass_HeliCity_Costheta20 = Master_Canvas.Clone()
Mass_HeliCity_Costheta20.SetName("Mass_HeliCity_Costheta20")
fHistHeliCity_Costheta_Muon20 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon20.SetName("fHistHeliCity_Costheta_Muon20")
Mass_HeliCity_Costheta20.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon20","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon20.SetDirectory(0)
Mass_HeliCity_Costheta20.Write()



Mass_HeliCity_Costheta21 = Master_Canvas.Clone()
Mass_HeliCity_Costheta21.SetName("Mass_HeliCity_Costheta21")
fHistHeliCity_Costheta_Muon21 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon21.SetName("fHistHeliCity_Costheta_Muon21")
Mass_HeliCity_Costheta21.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon21","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon21.SetDirectory(0)
Mass_HeliCity_Costheta21.Write()





Mass_HeliCity_Costheta22 = Master_Canvas.Clone()
Mass_HeliCity_Costheta22.SetName("Mass_HeliCity_Costheta22")
fHistHeliCity_Costheta_Muon22 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon22.SetName("fHistHeliCity_Costheta_Muon22")
Mass_HeliCity_Costheta22.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon22","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon22.SetDirectory(0)
Mass_HeliCity_Costheta22.Write()


Mass_HeliCity_Costheta23 = Master_Canvas.Clone()
Mass_HeliCity_Costheta23.SetName("Mass_HeliCity_Costheta23")
fHistHeliCity_Costheta_Muon23 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon23.SetName("fHistHeliCity_Costheta_Muon23")
Mass_HeliCity_Costheta23.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon23","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon23.SetDirectory(0)
Mass_HeliCity_Costheta23.Write()







Mass_HeliCity_Costheta24 = Master_Canvas.Clone()
Mass_HeliCity_Costheta24.SetName("Mass_HeliCity_Costheta24")
fHistHeliCity_Costheta_Muon24 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon24.SetName("fHistHeliCity_Costheta_Muon24")
Mass_HeliCity_Costheta24.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon24","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon24.SetDirectory(0)
Mass_HeliCity_Costheta24.Write()



Mass_HeliCity_Costheta25 = Master_Canvas.Clone()
Mass_HeliCity_Costheta25.SetName("Mass_HeliCity_Costheta25")
fHistHeliCity_Costheta_Muon25 = fHistMass_MuPair.Clone()
fHistHeliCity_Costheta_Muon25.SetName("fHistHeliCity_Costheta_Muon25")
Mass_HeliCity_Costheta25.cd()
tree.Draw("fM>>fHistHeliCity_Costheta_Muon25","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_Costheta_Muon25.SetDirectory(0)
Mass_HeliCity_Costheta25.Write()












Mass_HeliCity_CosPhi1 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi1.SetName("Mass_HeliCity_CosPhi1")
fHistHeliCity_CosPhi_Muon1 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon1.SetName("fHistHeliCity_CosPhi_Muon1")
Mass_HeliCity_CosPhi1.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon1","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon1.SetDirectory(0)
Mass_HeliCity_CosPhi1.Write()





Mass_HeliCity_CosPhi2 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi2.SetName("Mass_HeliCity_CosPhi2")
fHistHeliCity_CosPhi_Muon2 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon2.SetName("fHistHeliCity_CosPhi_Muon2")
Mass_HeliCity_CosPhi2.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon2","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon2.SetDirectory(0)
Mass_HeliCity_CosPhi2.Write()


Mass_HeliCity_CosPhi3 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi3.SetName("Mass_HeliCity_CosPhi3")
fHistHeliCity_CosPhi_Muon3 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon3.SetName("fHistHeliCity_CosPhi_Muon3")
Mass_HeliCity_CosPhi3.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon3","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon3.SetDirectory(0)
Mass_HeliCity_CosPhi3.Write()





Mass_HeliCity_CosPhi4 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi4.SetName("Mass_HeliCity_CosPhi4")
fHistHeliCity_CosPhi_Muon4 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon4.SetName("fHistHeliCity_CosPhi_Muon4")
Mass_HeliCity_CosPhi4.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon4.SetDirectory(0)
Mass_HeliCity_CosPhi4.Write()





Mass_HeliCity_CosPhi4 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi4.SetName("Mass_HeliCity_CosPhi4")
fHistHeliCity_CosPhi_Muon4 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon4.SetName("fHistHeliCity_CosPhi_Muon4")
Mass_HeliCity_CosPhi4.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon4.SetDirectory(0)
Mass_HeliCity_CosPhi4.Write()



Mass_HeliCity_CosPhi5 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi5.SetName("Mass_HeliCity_CosPhi5")
fHistHeliCity_CosPhi_Muon5 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon5.SetName("fHistHeliCity_CosPhi_Muon5")
Mass_HeliCity_CosPhi5.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon5","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon5.SetDirectory(0)
Mass_HeliCity_CosPhi5.Write()





Mass_HeliCity_CosPhi6 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi6.SetName("Mass_HeliCity_CosPhi6")
fHistHeliCity_CosPhi_Muon6 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon6.SetName("fHistHeliCity_CosPhi_Muon6")
Mass_HeliCity_CosPhi6.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon6","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon6.SetDirectory(0)
Mass_HeliCity_CosPhi6.Write()






Mass_HeliCity_CosPhi7 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi7.SetName("Mass_HeliCity_CosPhi7")
fHistHeliCity_CosPhi_Muon7 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon7.SetName("fHistHeliCity_CosPhi_Muon7")
Mass_HeliCity_CosPhi7.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon7","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon7.SetDirectory(0)
Mass_HeliCity_CosPhi7.Write()




Mass_HeliCity_CosPhi8 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi8.SetName("Mass_HeliCity_CosPhi8")
fHistHeliCity_CosPhi_Muon8 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon8.SetName("fHistHeliCity_CosPhi_Muon8")
Mass_HeliCity_CosPhi8.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon8","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon8.SetDirectory(0)
Mass_HeliCity_CosPhi8.Write()



Mass_HeliCity_CosPhi9 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi9.SetName("Mass_HeliCity_CosPhi9")
fHistHeliCity_CosPhi_Muon9 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon9.SetName("fHistHeliCity_CosPhi_Muon9")
Mass_HeliCity_CosPhi9.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon9","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon9.SetDirectory(0)
Mass_HeliCity_CosPhi9.Write()


Mass_HeliCity_CosPhi10 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi10.SetName("Mass_HeliCity_CosPhi10")
fHistHeliCity_CosPhi_Muon10 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon10.SetName("fHistHeliCity_CosPhi_Muon10")
Mass_HeliCity_CosPhi10.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon10","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon10.SetDirectory(0)
Mass_HeliCity_CosPhi10.Write()





Mass_HeliCity_CosPhi11 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi11.SetName("Mass_HeliCity_CosPhi11")
fHistHeliCity_CosPhi_Muon11 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon11.SetName("fHistHeliCity_CosPhi_Muon11")
Mass_HeliCity_CosPhi11.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon11","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon11.SetDirectory(0)
Mass_HeliCity_CosPhi11.Write()






Mass_HeliCity_CosPhi12 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi12.SetName("Mass_HeliCity_CosPhi12")
fHistHeliCity_CosPhi_Muon12 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon12.SetName("fHistHeliCity_CosPhi_Muon12")
Mass_HeliCity_CosPhi12.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon12","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon12.SetDirectory(0)
Mass_HeliCity_CosPhi12.Write()


Mass_HeliCity_CosPhi13 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi13.SetName("Mass_HeliCity_CosPhi13")
fHistHeliCity_CosPhi_Muon13 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon13.SetName("fHistHeliCity_CosPhi_Muon13")
Mass_HeliCity_CosPhi13.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon13","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon13.SetDirectory(0)
Mass_HeliCity_CosPhi13.Write()





Mass_HeliCity_CosPhi14 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi14.SetName("Mass_HeliCity_CosPhi14")
fHistHeliCity_CosPhi_Muon14 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon14.SetName("fHistHeliCity_CosPhi_Muon14")
Mass_HeliCity_CosPhi14.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon14","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon14.SetDirectory(0)
Mass_HeliCity_CosPhi14.Write()









Mass_HeliCity_CosPhi15 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi15.SetName("Mass_HeliCity_CosPhi15")
fHistHeliCity_CosPhi_Muon15 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon15.SetName("fHistHeliCity_CosPhi_Muon15")
Mass_HeliCity_CosPhi15.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon15","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon15.SetDirectory(0)
Mass_HeliCity_CosPhi15.Write()





Mass_HeliCity_CosPhi16 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi16.SetName("Mass_HeliCity_CosPhi16")
fHistHeliCity_CosPhi_Muon16 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon16.SetName("fHistHeliCity_CosPhi_Muon16")
Mass_HeliCity_CosPhi16.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon16","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon16.SetDirectory(0)
Mass_HeliCity_CosPhi16.Write()






Mass_HeliCity_CosPhi17 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi17.SetName("Mass_HeliCity_CosPhi17")
fHistHeliCity_CosPhi_Muon17 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon17.SetName("fHistHeliCity_CosPhi_Muon17")
Mass_HeliCity_CosPhi17.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon17","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon17.SetDirectory(0)
Mass_HeliCity_CosPhi17.Write()




Mass_HeliCity_CosPhi18 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi18.SetName("Mass_HeliCity_CosPhi18")
fHistHeliCity_CosPhi_Muon18 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon18.SetName("fHistHeliCity_CosPhi_Muon18")
Mass_HeliCity_CosPhi18.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon18","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon18.SetDirectory(0)
Mass_HeliCity_CosPhi18.Write()


Mass_HeliCity_CosPhi19 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi19.SetName("Mass_HeliCity_CosPhi19")
fHistHeliCity_CosPhi_Muon19 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon19.SetName("fHistHeliCity_CosPhi_Muon19")
Mass_HeliCity_CosPhi19.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon19","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon19.SetDirectory(0)
Mass_HeliCity_CosPhi19.Write()



Mass_HeliCity_CosPhi20 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi20.SetName("Mass_HeliCity_CosPhi20")
fHistHeliCity_CosPhi_Muon20 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon20.SetName("fHistHeliCity_CosPhi_Muon20")
Mass_HeliCity_CosPhi20.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon20","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon20.SetDirectory(0)
Mass_HeliCity_CosPhi20.Write()



Mass_HeliCity_CosPhi21 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi21.SetName("Mass_HeliCity_CosPhi21")
fHistHeliCity_CosPhi_Muon21 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon21.SetName("fHistHeliCity_CosPhi_Muon21")
Mass_HeliCity_CosPhi21.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon21","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon21.SetDirectory(0)
Mass_HeliCity_CosPhi21.Write()





Mass_HeliCity_CosPhi22 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi22.SetName("Mass_HeliCity_CosPhi22")
fHistHeliCity_CosPhi_Muon22 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon22.SetName("fHistHeliCity_CosPhi_Muon22")
Mass_HeliCity_CosPhi22.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon22","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon22.SetDirectory(0)
Mass_HeliCity_CosPhi22.Write()


Mass_HeliCity_CosPhi23 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi23.SetName("Mass_HeliCity_CosPhi23")
fHistHeliCity_CosPhi_Muon23 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon23.SetName("fHistHeliCity_CosPhi_Muon23")
Mass_HeliCity_CosPhi23.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon23","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon23.SetDirectory(0)
Mass_HeliCity_CosPhi23.Write()







Mass_HeliCity_CosPhi24 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi24.SetName("Mass_HeliCity_CosPhi24")
fHistHeliCity_CosPhi_Muon24 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon24.SetName("fHistHeliCity_CosPhi_Muon24")
Mass_HeliCity_CosPhi24.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon24","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon24.SetDirectory(0)
Mass_HeliCity_CosPhi24.Write()



Mass_HeliCity_CosPhi25 = Master_Canvas.Clone()
Mass_HeliCity_CosPhi25.SetName("Mass_HeliCity_CosPhi25")
fHistHeliCity_CosPhi_Muon25 = fHistMass_MuPair.Clone()
fHistHeliCity_CosPhi_Muon25.SetName("fHistHeliCity_CosPhi_Muon25")
Mass_HeliCity_CosPhi25.cd()
tree.Draw("fM>>fHistHeliCity_CosPhi_Muon25","","")#need to define the cut parameter which will be on cos theta
fHistHeliCity_CosPhi_Muon25.SetDirectory(0)
Mass_HeliCity_CosPhi25.Write()

#############################################################################################################
helicity.cd("../")
#helicity frame

collinsoper = TDirectory() 
collinsoper = file2.mkdir("collinsoper")

collinsoper.cd()
#plots after defining collinsoper frame






Mass_Collin_Soper_Costheta1 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta1.SetName("Mass_Collin_Soper_Costheta1")
fHistCollin_Soper_Costheta_Muon1 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon1.SetName("fHistCollin_Soper_Costheta_Muon1")
Mass_Collin_Soper_Costheta1.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon1","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon1.SetDirectory(0)
Mass_Collin_Soper_Costheta1.Write()





Mass_Collin_Soper_Costheta2 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta2.SetName("Mass_Collin_Soper_Costheta2")
fHistCollin_Soper_Costheta_Muon2 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon2.SetName("fHistCollin_Soper_Costheta_Muon2")
Mass_Collin_Soper_Costheta2.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon2","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon2.SetDirectory(0)
Mass_Collin_Soper_Costheta2.Write()


Mass_Collin_Soper_Costheta3 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta3.SetName("Mass_Collin_Soper_Costheta3")
fHistCollin_Soper_Costheta_Muon3 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon3.SetName("fHistCollin_Soper_Costheta_Muon3")
Mass_Collin_Soper_Costheta3.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon3","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon3.SetDirectory(0)
Mass_Collin_Soper_Costheta3.Write()





Mass_Collin_Soper_Costheta4 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta4.SetName("Mass_Collin_Soper_Costheta4")
fHistCollin_Soper_Costheta_Muon4 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon4.SetName("fHistCollin_Soper_Costheta_Muon4")
Mass_Collin_Soper_Costheta4.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon4.SetDirectory(0)
Mass_Collin_Soper_Costheta4.Write()





Mass_Collin_Soper_Costheta4 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta4.SetName("Mass_Collin_Soper_Costheta4")
fHistCollin_Soper_Costheta_Muon4 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon4.SetName("fHistCollin_Soper_Costheta_Muon4")
Mass_Collin_Soper_Costheta4.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon4.SetDirectory(0)
Mass_Collin_Soper_Costheta4.Write()



Mass_Collin_Soper_Costheta5 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta5.SetName("Mass_Collin_Soper_Costheta5")
fHistCollin_Soper_Costheta_Muon5 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon5.SetName("fHistCollin_Soper_Costheta_Muon5")
Mass_Collin_Soper_Costheta5.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon5","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon5.SetDirectory(0)
Mass_Collin_Soper_Costheta5.Write()





Mass_Collin_Soper_Costheta6 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta6.SetName("Mass_Collin_Soper_Costheta6")
fHistCollin_Soper_Costheta_Muon6 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon6.SetName("fHistCollin_Soper_Costheta_Muon6")
Mass_Collin_Soper_Costheta6.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon6","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon6.SetDirectory(0)
Mass_Collin_Soper_Costheta6.Write()






Mass_Collin_Soper_Costheta7 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta7.SetName("Mass_Collin_Soper_Costheta7")
fHistCollin_Soper_Costheta_Muon7 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon7.SetName("fHistCollin_Soper_Costheta_Muon7")
Mass_Collin_Soper_Costheta7.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon7","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon7.SetDirectory(0)
Mass_Collin_Soper_Costheta7.Write()




Mass_Collin_Soper_Costheta8 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta8.SetName("Mass_Collin_Soper_Costheta8")
fHistCollin_Soper_Costheta_Muon8 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon8.SetName("fHistCollin_Soper_Costheta_Muon8")
Mass_Collin_Soper_Costheta8.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon8","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon8.SetDirectory(0)
Mass_Collin_Soper_Costheta8.Write()



Mass_Collin_Soper_Costheta9 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta9.SetName("Mass_Collin_Soper_Costheta9")
fHistCollin_Soper_Costheta_Muon9 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon9.SetName("fHistCollin_Soper_Costheta_Muon9")
Mass_Collin_Soper_Costheta9.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon9","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon9.SetDirectory(0)
Mass_Collin_Soper_Costheta9.Write()


Mass_Collin_Soper_Costheta10 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta10.SetName("Mass_Collin_Soper_Costheta10")
fHistCollin_Soper_Costheta_Muon10 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon10.SetName("fHistCollin_Soper_Costheta_Muon10")
Mass_Collin_Soper_Costheta10.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon10","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon10.SetDirectory(0)
Mass_Collin_Soper_Costheta10.Write()





Mass_Collin_Soper_Costheta11 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta11.SetName("Mass_Collin_Soper_Costheta11")
fHistCollin_Soper_Costheta_Muon11 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon11.SetName("fHistCollin_Soper_Costheta_Muon11")
Mass_Collin_Soper_Costheta11.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon11","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon11.SetDirectory(0)
Mass_Collin_Soper_Costheta11.Write()






Mass_Collin_Soper_Costheta12 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta12.SetName("Mass_Collin_Soper_Costheta12")
fHistCollin_Soper_Costheta_Muon12 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon12.SetName("fHistCollin_Soper_Costheta_Muon12")
Mass_Collin_Soper_Costheta12.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon12","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon12.SetDirectory(0)
Mass_Collin_Soper_Costheta12.Write()


Mass_Collin_Soper_Costheta13 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta13.SetName("Mass_Collin_Soper_Costheta13")
fHistCollin_Soper_Costheta_Muon13 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon13.SetName("fHistCollin_Soper_Costheta_Muon13")
Mass_Collin_Soper_Costheta13.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon13","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon13.SetDirectory(0)
Mass_Collin_Soper_Costheta13.Write()





Mass_Collin_Soper_Costheta14 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta14.SetName("Mass_Collin_Soper_Costheta14")
fHistCollin_Soper_Costheta_Muon14 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon14.SetName("fHistCollin_Soper_Costheta_Muon14")
Mass_Collin_Soper_Costheta14.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon14","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon14.SetDirectory(0)
Mass_Collin_Soper_Costheta14.Write()









Mass_Collin_Soper_Costheta15 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta15.SetName("Mass_Collin_Soper_Costheta15")
fHistCollin_Soper_Costheta_Muon15 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon15.SetName("fHistCollin_Soper_Costheta_Muon15")
Mass_Collin_Soper_Costheta15.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon15","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon15.SetDirectory(0)
Mass_Collin_Soper_Costheta15.Write()





Mass_Collin_Soper_Costheta16 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta16.SetName("Mass_Collin_Soper_Costheta16")
fHistCollin_Soper_Costheta_Muon16 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon16.SetName("fHistCollin_Soper_Costheta_Muon16")
Mass_Collin_Soper_Costheta16.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon16","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon16.SetDirectory(0)
Mass_Collin_Soper_Costheta16.Write()






Mass_Collin_Soper_Costheta17 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta17.SetName("Mass_Collin_Soper_Costheta17")
fHistCollin_Soper_Costheta_Muon17 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon17.SetName("fHistCollin_Soper_Costheta_Muon17")
Mass_Collin_Soper_Costheta17.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon17","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon17.SetDirectory(0)
Mass_Collin_Soper_Costheta17.Write()




Mass_Collin_Soper_Costheta18 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta18.SetName("Mass_Collin_Soper_Costheta18")
fHistCollin_Soper_Costheta_Muon18 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon18.SetName("fHistCollin_Soper_Costheta_Muon18")
Mass_Collin_Soper_Costheta18.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon18","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon18.SetDirectory(0)
Mass_Collin_Soper_Costheta18.Write()


Mass_Collin_Soper_Costheta19 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta19.SetName("Mass_Collin_Soper_Costheta19")
fHistCollin_Soper_Costheta_Muon19 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon19.SetName("fHistCollin_Soper_Costheta_Muon19")
Mass_Collin_Soper_Costheta19.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon19","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon19.SetDirectory(0)
Mass_Collin_Soper_Costheta19.Write()



Mass_Collin_Soper_Costheta20 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta20.SetName("Mass_Collin_Soper_Costheta20")
fHistCollin_Soper_Costheta_Muon20 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon20.SetName("fHistCollin_Soper_Costheta_Muon20")
Mass_Collin_Soper_Costheta20.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon20","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon20.SetDirectory(0)
Mass_Collin_Soper_Costheta20.Write()



Mass_Collin_Soper_Costheta21 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta21.SetName("Mass_Collin_Soper_Costheta21")
fHistCollin_Soper_Costheta_Muon21 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon21.SetName("fHistCollin_Soper_Costheta_Muon21")
Mass_Collin_Soper_Costheta21.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon21","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon21.SetDirectory(0)
Mass_Collin_Soper_Costheta21.Write()





Mass_Collin_Soper_Costheta22 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta22.SetName("Mass_Collin_Soper_Costheta22")
fHistCollin_Soper_Costheta_Muon22 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon22.SetName("fHistCollin_Soper_Costheta_Muon22")
Mass_Collin_Soper_Costheta22.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon22","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon22.SetDirectory(0)
Mass_Collin_Soper_Costheta22.Write()


Mass_Collin_Soper_Costheta23 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta23.SetName("Mass_Collin_Soper_Costheta23")
fHistCollin_Soper_Costheta_Muon23 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon23.SetName("fHistCollin_Soper_Costheta_Muon23")
Mass_Collin_Soper_Costheta23.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon23","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon23.SetDirectory(0)
Mass_Collin_Soper_Costheta23.Write()







Mass_Collin_Soper_Costheta24 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta24.SetName("Mass_Collin_Soper_Costheta24")
fHistCollin_Soper_Costheta_Muon24 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon24.SetName("fHistCollin_Soper_Costheta_Muon24")
Mass_Collin_Soper_Costheta24.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon24","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon24.SetDirectory(0)
Mass_Collin_Soper_Costheta24.Write()



Mass_Collin_Soper_Costheta25 = Master_Canvas.Clone()
Mass_Collin_Soper_Costheta25.SetName("Mass_Collin_Soper_Costheta25")
fHistCollin_Soper_Costheta_Muon25 = fHistMass_MuPair.Clone()
fHistCollin_Soper_Costheta_Muon25.SetName("fHistCollin_Soper_Costheta_Muon25")
Mass_Collin_Soper_Costheta25.cd()
tree.Draw("fM>>fHistCollin_Soper_Costheta_Muon25","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_Costheta_Muon25.SetDirectory(0)
Mass_Collin_Soper_Costheta25.Write()












Mass_Collin_Soper_CosPhi1 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi1.SetName("Mass_Collin_Soper_CosPhi1")
fHistCollin_Soper_CosPhi_Muon1 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon1.SetName("fHistCollin_Soper_CosPhi_Muon1")
Mass_Collin_Soper_CosPhi1.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon1","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon1.SetDirectory(0)
Mass_Collin_Soper_CosPhi1.Write()





Mass_Collin_Soper_CosPhi2 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi2.SetName("Mass_Collin_Soper_CosPhi2")
fHistCollin_Soper_CosPhi_Muon2 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon2.SetName("fHistCollin_Soper_CosPhi_Muon2")
Mass_Collin_Soper_CosPhi2.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon2","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon2.SetDirectory(0)
Mass_Collin_Soper_CosPhi2.Write()


Mass_Collin_Soper_CosPhi3 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi3.SetName("Mass_Collin_Soper_CosPhi3")
fHistCollin_Soper_CosPhi_Muon3 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon3.SetName("fHistCollin_Soper_CosPhi_Muon3")
Mass_Collin_Soper_CosPhi3.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon3","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon3.SetDirectory(0)
Mass_Collin_Soper_CosPhi3.Write()





Mass_Collin_Soper_CosPhi4 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi4.SetName("Mass_Collin_Soper_CosPhi4")
fHistCollin_Soper_CosPhi_Muon4 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon4.SetName("fHistCollin_Soper_CosPhi_Muon4")
Mass_Collin_Soper_CosPhi4.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon4.SetDirectory(0)
Mass_Collin_Soper_CosPhi4.Write()





Mass_Collin_Soper_CosPhi4 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi4.SetName("Mass_Collin_Soper_CosPhi4")
fHistCollin_Soper_CosPhi_Muon4 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon4.SetName("fHistCollin_Soper_CosPhi_Muon4")
Mass_Collin_Soper_CosPhi4.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon4","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon4.SetDirectory(0)
Mass_Collin_Soper_CosPhi4.Write()



Mass_Collin_Soper_CosPhi5 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi5.SetName("Mass_Collin_Soper_CosPhi5")
fHistCollin_Soper_CosPhi_Muon5 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon5.SetName("fHistCollin_Soper_CosPhi_Muon5")
Mass_Collin_Soper_CosPhi5.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon5","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon5.SetDirectory(0)
Mass_Collin_Soper_CosPhi5.Write()





Mass_Collin_Soper_CosPhi6 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi6.SetName("Mass_Collin_Soper_CosPhi6")
fHistCollin_Soper_CosPhi_Muon6 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon6.SetName("fHistCollin_Soper_CosPhi_Muon6")
Mass_Collin_Soper_CosPhi6.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon6","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon6.SetDirectory(0)
Mass_Collin_Soper_CosPhi6.Write()






Mass_Collin_Soper_CosPhi7 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi7.SetName("Mass_Collin_Soper_CosPhi7")
fHistCollin_Soper_CosPhi_Muon7 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon7.SetName("fHistCollin_Soper_CosPhi_Muon7")
Mass_Collin_Soper_CosPhi7.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon7","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon7.SetDirectory(0)
Mass_Collin_Soper_CosPhi7.Write()




Mass_Collin_Soper_CosPhi8 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi8.SetName("Mass_Collin_Soper_CosPhi8")
fHistCollin_Soper_CosPhi_Muon8 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon8.SetName("fHistCollin_Soper_CosPhi_Muon8")
Mass_Collin_Soper_CosPhi8.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon8","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon8.SetDirectory(0)
Mass_Collin_Soper_CosPhi8.Write()



Mass_Collin_Soper_CosPhi9 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi9.SetName("Mass_Collin_Soper_CosPhi9")
fHistCollin_Soper_CosPhi_Muon9 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon9.SetName("fHistCollin_Soper_CosPhi_Muon9")
Mass_Collin_Soper_CosPhi9.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon9","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon9.SetDirectory(0)
Mass_Collin_Soper_CosPhi9.Write()


Mass_Collin_Soper_CosPhi10 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi10.SetName("Mass_Collin_Soper_CosPhi10")
fHistCollin_Soper_CosPhi_Muon10 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon10.SetName("fHistCollin_Soper_CosPhi_Muon10")
Mass_Collin_Soper_CosPhi10.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon10","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon10.SetDirectory(0)
Mass_Collin_Soper_CosPhi10.Write()





Mass_Collin_Soper_CosPhi11 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi11.SetName("Mass_Collin_Soper_CosPhi11")
fHistCollin_Soper_CosPhi_Muon11 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon11.SetName("fHistCollin_Soper_CosPhi_Muon11")
Mass_Collin_Soper_CosPhi11.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon11","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon11.SetDirectory(0)
Mass_Collin_Soper_CosPhi11.Write()






Mass_Collin_Soper_CosPhi12 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi12.SetName("Mass_Collin_Soper_CosPhi12")
fHistCollin_Soper_CosPhi_Muon12 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon12.SetName("fHistCollin_Soper_CosPhi_Muon12")
Mass_Collin_Soper_CosPhi12.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon12","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon12.SetDirectory(0)
Mass_Collin_Soper_CosPhi12.Write()


Mass_Collin_Soper_CosPhi13 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi13.SetName("Mass_Collin_Soper_CosPhi13")
fHistCollin_Soper_CosPhi_Muon13 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon13.SetName("fHistCollin_Soper_CosPhi_Muon13")
Mass_Collin_Soper_CosPhi13.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon13","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon13.SetDirectory(0)
Mass_Collin_Soper_CosPhi13.Write()





Mass_Collin_Soper_CosPhi14 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi14.SetName("Mass_Collin_Soper_CosPhi14")
fHistCollin_Soper_CosPhi_Muon14 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon14.SetName("fHistCollin_Soper_CosPhi_Muon14")
Mass_Collin_Soper_CosPhi14.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon14","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon14.SetDirectory(0)
Mass_Collin_Soper_CosPhi14.Write()









Mass_Collin_Soper_CosPhi15 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi15.SetName("Mass_Collin_Soper_CosPhi15")
fHistCollin_Soper_CosPhi_Muon15 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon15.SetName("fHistCollin_Soper_CosPhi_Muon15")
Mass_Collin_Soper_CosPhi15.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon15","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon15.SetDirectory(0)
Mass_Collin_Soper_CosPhi15.Write()





Mass_Collin_Soper_CosPhi16 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi16.SetName("Mass_Collin_Soper_CosPhi16")
fHistCollin_Soper_CosPhi_Muon16 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon16.SetName("fHistCollin_Soper_CosPhi_Muon16")
Mass_Collin_Soper_CosPhi16.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon16","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon16.SetDirectory(0)
Mass_Collin_Soper_CosPhi16.Write()






Mass_Collin_Soper_CosPhi17 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi17.SetName("Mass_Collin_Soper_CosPhi17")
fHistCollin_Soper_CosPhi_Muon17 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon17.SetName("fHistCollin_Soper_CosPhi_Muon17")
Mass_Collin_Soper_CosPhi17.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon17","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon17.SetDirectory(0)
Mass_Collin_Soper_CosPhi17.Write()




Mass_Collin_Soper_CosPhi18 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi18.SetName("Mass_Collin_Soper_CosPhi18")
fHistCollin_Soper_CosPhi_Muon18 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon18.SetName("fHistCollin_Soper_CosPhi_Muon18")
Mass_Collin_Soper_CosPhi18.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon18","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon18.SetDirectory(0)
Mass_Collin_Soper_CosPhi18.Write()


Mass_Collin_Soper_CosPhi19 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi19.SetName("Mass_Collin_Soper_CosPhi19")
fHistCollin_Soper_CosPhi_Muon19 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon19.SetName("fHistCollin_Soper_CosPhi_Muon19")
Mass_Collin_Soper_CosPhi19.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon19","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon19.SetDirectory(0)
Mass_Collin_Soper_CosPhi19.Write()



Mass_Collin_Soper_CosPhi20 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi20.SetName("Mass_Collin_Soper_CosPhi20")
fHistCollin_Soper_CosPhi_Muon20 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon20.SetName("fHistCollin_Soper_CosPhi_Muon20")
Mass_Collin_Soper_CosPhi20.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon20","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon20.SetDirectory(0)
Mass_Collin_Soper_CosPhi20.Write()



Mass_Collin_Soper_CosPhi21 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi21.SetName("Mass_Collin_Soper_CosPhi21")
fHistCollin_Soper_CosPhi_Muon21 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon21.SetName("fHistCollin_Soper_CosPhi_Muon21")
Mass_Collin_Soper_CosPhi21.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon21","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon21.SetDirectory(0)
Mass_Collin_Soper_CosPhi21.Write()





Mass_Collin_Soper_CosPhi22 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi22.SetName("Mass_Collin_Soper_CosPhi22")
fHistCollin_Soper_CosPhi_Muon22 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon22.SetName("fHistCollin_Soper_CosPhi_Muon22")
Mass_Collin_Soper_CosPhi22.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon22","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon22.SetDirectory(0)
Mass_Collin_Soper_CosPhi22.Write()


Mass_Collin_Soper_CosPhi23 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi23.SetName("Mass_Collin_Soper_CosPhi23")
fHistCollin_Soper_CosPhi_Muon23 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon23.SetName("fHistCollin_Soper_CosPhi_Muon23")
Mass_Collin_Soper_CosPhi23.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon23","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon23.SetDirectory(0)
Mass_Collin_Soper_CosPhi23.Write()







Mass_Collin_Soper_CosPhi24 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi24.SetName("Mass_Collin_Soper_CosPhi24")
fHistCollin_Soper_CosPhi_Muon24 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon24.SetName("fHistCollin_Soper_CosPhi_Muon24")
Mass_Collin_Soper_CosPhi24.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon24","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon24.SetDirectory(0)
Mass_Collin_Soper_CosPhi24.Write()



Mass_Collin_Soper_CosPhi25 = Master_Canvas.Clone()
Mass_Collin_Soper_CosPhi25.SetName("Mass_Collin_Soper_CosPhi25")
fHistCollin_Soper_CosPhi_Muon25 = fHistMass_MuPair.Clone()
fHistCollin_Soper_CosPhi_Muon25.SetName("fHistCollin_Soper_CosPhi_Muon25")
Mass_Collin_Soper_CosPhi25.cd()
tree.Draw("fM>>fHistCollin_Soper_CosPhi_Muon25","","")#need to define the cut parameter which will be on cos theta
fHistCollin_Soper_CosPhi_Muon25.SetDirectory(0)
Mass_Collin_Soper_CosPhi25.Write()"""

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


