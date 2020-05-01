#!/usr/bin/python
import code
import ROOT as rt
from ROOT import TFile, TTree , TCanvas, TH1F, TList , TH2F ,TMath ,TF1, TStyle ,gStyle , TRefArray, TClonesArray, TObjArray, gPad , TLegend ,TString
file = TFile.Open("Incohernt_Phi_PID.root")
#list = file.Get("")
PhiMass = TCanvas("PhiMass","Phi_Mass",600,300,700,527)
Sigma_Radius = TCanvas("Sigma_Radius","Sigma_Radius",600,300)
SigmavsSigma = TCanvas("SigmavsSigma","SigmaVsSigama",600,300)
dEdX = TCanvas("dEdX","dEdX",600,300)
test = TCanvas("test","dEdX",600,300)
list = TList()
list = file.Get("UPCPhiTaskTest/UPCPhiWithTrigger")
tree = list.FindObject("scatterplot")
#MassPlot for Incoherent Candidates
HighPt_Mass = TH1F("HighPt_Mass","Mass Dist of Inco #Phi with TOF",100, 0 ,10)

HighPt_Mass.SetFillStyle(4050)
HighPt_Mass.SetYTitle("Number of Events")
HighPt_Mass.SetXTitle("Phi Mass(MeV/C^2)")
HighPt_Mass.SetTitleOffset(1.5, "Y")
HighPt_Mass.SetTitleOffset(1.3, "X")
HighPt_Mass.SetLineColor(rt.kGreen)
HighPt_Mass.SetMarkerStyle(rt.kCircle)
HighPt_Mass.SetLineWidth(2)
HighPt_Mass.SetOption("E1")
Pt_mass = HighPt_Mass.Clone()
Pt_mass.SetLineColor(rt.kRed)
Pt_mass.SetLineWidth(4)
#Mass Plot for Coherent Candidates
LowPt_Mass =  TH1F("LowPt_Mass","Mass Dist of Incoherent #Phi without TOF info",100, 0 ,2)
#HighPt_Mass2 = LowPt_Mass.Clone()
LowPt_Mass.SetMarkerStyle(rt.kCircle)
LowPt_Mass.SetLineColor(rt.kBlue)
LowPt_Mass.SetLineWidth(2)
LowPt_Mass.SetOption("E1")
#Scatter Plots
SigmavSigma =  TH2F("SigmavSigma","Scatterplot of Sigma of Track 1 vs Track 2 ",1000,-50,50,1000, -50 ,50)
SigmavSigma.SetYTitle("#sigma of Kaons")
SigmavSigma.SetXTitle("#sigma of Kaons")
SigmavSigma.SetTitleOffset(1.5, "Y")
SigmavSigma.SetTitleOffset(1.3, "X") 
SigmavSigma.SetMarkerStyle(3)

SigmaRadius =  TH2F("SigmaRadius","Scatterplot of Sigma of track 1 and 2",500,0,100,500,0 ,100)

SigmaRadius.SetYTitle("#sqrt{#sigma^{2}_{#pi} + #sigma_{#pi}^{2}}")
SigmaRadius.SetXTitle("Momentum of Particle(GeV/C)")
SigmaRadius.SetTitleOffset(1.5, "Y")
SigmaRadius.SetTitleOffset(1.3, "X")

dEdXvsP1 =  TH2F("dEdXvsP1"," TOF Kaon n#sigma vs Momentum of Daughter particle",500,0 ,2,500,0,200)
dEdXvsP1.SetYTitle("Track 1 n#sigma")
dEdXvsP1.SetXTitle("Momentum of track 1(GeV/C)")
dEdXvsP1.SetTitleOffset(1.5, "Y")
dEdXvsP1.SetTitleOffset(1.3, "X")
dEdXvsP1.SetMarkerStyle(rt.kCircle)
 
 
dEdXvsP2=  TH2F("dEdXvsP2","TOF n#sigma vs Momentum of Daughter particle",500, 0,2,500,0,200)
dEdXvsP2.SetYTitle("Track 2 n#sigma")
dEdXvsP2.SetXTitle("Momentum of track2 Particle(GeV/C)")
dEdXvsP2.SetTitleOffset(1.5, "Y")
dEdXvsP2.SetTitleOffset(1.3, "X")
dEdXvsP2.SetMarkerStyle(rt.kCircle)

#These will defing that color of the canvas and the information to show in histogram
gStyle.SetCanvasColor(0);
gStyle.SetOptStat("e")


## I will define cuts Here
MassCut = TString() 
PtCut  =  TString()
KSigmaTPC_Cut = TString()
KSigmaTOF_Cut = TString()
KSigmaTOF_Cut2 = TString()
PiSigmaTPC_Cut = TString()
PiSigmaTOF_Cut = TString()
KSigmaTPC_TOF = TString()
ElSigmaTPC_Cut = TString()
MuSigmaTPC_Cut = TString()
DCAxyCut = TString()
DCAzCut  = TString()
DaughterPcut = TString()
DaughterPcuthigh =TString()
DaughterPcut2 = TString()
DaughterPcuthigh2 =TString()
Or = TString()
TriggerCut = TString()
n = TString()
Or = "||"
n = "&&"
PtCut = "fPt>0.5"
KSigmaTPC_Cut =" (fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1)<4 "
KSigmaTOF_Cut ="(fKaonSigmaTOF0*fKaonSigmaTOF0 + fKaonSigmaTOF1*fKaonSigmaTOF1)<4"
KSigmaTOF_Cut2 ="(fKaonSigmaTOF0*fKaonSigmaTOF0 + fKaonSigmaTOF1*fKaonSigmaTOF1)>4"
PiSigmaTPC_Cut = " (fPiSigma0>2 && fPiSigma1>2)"
PiSigmaTOF_Cut ="(fPiSigmaTOF0>2 && fPiSigmaTOF0>2) "
DaughterPcut = "fPd0<0.9&& fPd1<0.9"
DaughterPcuthigh ="fPd0>0.4&&fPd0<1&&fPd1>0.4 &&fPd1<1"
DaughterPcut2 = "fPd0<0.9 && fPd1<0.9"
DaughterPcuthigh2 ="fPd0>0.4 &&fPd0<1 &&fPd1>0.4 &&fPd1<1"
DCAxyCut = "(TMath::Abs(fDCAxy1) < 2) && (TMath::Abs(fDCAxy2) < 2)"
DCAzCut ="(TMath::Abs(fDCAz1) < 2) && (TMath::Abs(fDCAz2) < 2)"
TriggerCut="fTriggerClass==8"
KSigmaTPC_TOF = "(fKaonSigma0*fKaonSigma0+fKaonSigmaTOF0*fKaonSigmaTOF0)<2 && "
ElSigmaTPC_Cut =  " (fElSigma0*fElSigma0 + fElSigma1*fElSigma1)<2" 
#ElSigmaTPC_Cut =  " (fElSigma0>0.001 && fElSigma1 >0.001)"
MuSigmaTPC_Cut = " (fMuSigma0*fMuSigma0 + fMuSigma1*fMuSigma1)<2"

MassCut = "((fPiSigma0*fPiSigma0 + fPiSigma1*fPiSigma1>16)&&(fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1<4)&& fPt>0.2 && (fKaonSigmaTOF0*fKaonSigmaTOF0 + fKaonSigmaTOF1*fKaonSigmaTOF1<4)&& fTriggerClass==9 && fPd0>0.4 &&fPd1>0.4) || ((fPiSigma0*fPiSigma0 + fPiSigma1*fPiSigma1>25)&&(fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1<4)&&fPt>0.2 && fPd0<0.4 &&fPd1<0.4&& fTriggerClass==9 )"#"fPt>0.2&&fdEdX0>100 && fdEdX1>100 && (TMath:
#MassCut_LowPt = TString("")

#MassCut_LowPt = "(fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1<2)&& fPt <0.2 && fPd0<0.4 &&fPd1<0.4 && fTriggerClass==9 && (TMath::Abs(fDCAz1) < 2) && (TMath::Abs(fDCAz2) < 2) "  
#TMath:Abs(fDCAxy1) < 2) && (TMath::Abs(fDCAxy2) < 2) "
#&&(fKaonSigma0*fKaonSigma0+fKaonSigma1*fKaonSigma1)<4 && fPd0<0.4 && fPd1<0.4 
gPad.SetTopMargin(0.02)
gPad.SetRightMargin(0.02)
gPad.SetBottomMargin(0.1)
gPad.SetLeftMargin(0.11)

# Functions

gau = TF1("gau","gaus",0.98,1.1)
gau2 = TF1("gau2","gaus",1.2,1.3)
pigau = TF1("pigau","gaus",1.2,1.5)
#gau = TF1("gau","[0]*exp(-0.5*((x-[1])/[2])^2)",0.95,1.05) 
ep = TF1("ep","[0]*expo",1.1,1.3)
poly= TF1("poly","pol2",0.95,1.5)
tp = TF1("tp","gaus(0)",0,1.2)


#tp.Draw()
#Drawing Histograms
PhiMass.Divide(2,1)
PhiMass.cd(1) 
#pt cut with tof information "("+PtCut+n+KSigmaTPC_Cut+n+TriggerCut+n+PiSigmaTPC_Cut+n+DaughterPcut+")"+Or+"("+"fPt>1"+n+PiSigmaTOF_Cut+n+TriggerCut+n+KSigmaTOF_Cut+n+DaughterPcuthigh+")"
tree.Draw("fM >> HighPt_mass", "("+TriggerCut+n+KSigmaTPC_Cut+n+PiSigmaTPC_Cut+n+DaughterPcut+n+PtCut+")"+Or+"("+"fPt>1"+n+PiSigmaTOF_Cut+n+TriggerCut+n+KSigmaTOF_Cut+n+DaughterPcuthigh+")","e")   
tree.Draw("fM >> Pt_mass", "("+TriggerCut+n+KSigmaTPC_Cut+n+PiSigmaTPC_Cut+n+DaughterPcut2+n+"fPt>0.2"+")"+Or+"("+PiSigmaTOF_Cut+n+"fPt>0.2"+n+TriggerCut+n+KSigmaTOF_Cut+n+DaughterPcuthigh+")","SAME")  
#Fitting Histograms 

HighPt_Mass.Fit("gau","QR") 

HighPt_Mass.Fit("ep","QR+")

#m = gau.GetParameter(1)
#s = gau.GetParameter(2)
#p = ep.GetParameter(2)
#q = poly.GetParameter(0)
#w = poly.GetParameter(1)
#y = poly.GetParameter(2)
#print m , s , p
#) 
#Combined = TF1("Combined","[0]* exp(-0.5*((x-[1])/[2])^2)+[3]*exp(-[4]*x)",0.9,1.2) 
Combined = TF1("Combined","gaus(0)+ expo(3)",0.98,1.3) 

Combined.SetLineWidth(2)
Combined.SetLineColor(rt.kBlack)
Combined.SetParameter(1,gau.GetParameter(1))
Combined.SetParameter(2,gau.GetParameter(2))
Combined.SetParameter(4,ep.GetParameter(1))

#Combined.SetParameter(4,w)
#Combined.SetParameter(3,q)
#Combined.SetParameter(5,y)
#Defining Legend to add Text in histograms
legend = TLegend(0.4,0.7,0.9,0.9)
#legend.SetHeader("The Legend Title","C") # option "C" allows to center the header
#legend.AddEntry(None,{tp.GetChisquare},"f")
legend.AddEntry("tp","Gaussian with exponential and Polynomical background","l")
legend.AddEntry("HighPt_Mass",MassCut[0:16],"e2p")


#Fitting with Combined Function
HighPt_Mass.Fit("Combined","QR+")
#legend.Draw()
#legend.Print()
#d = Combined.GetChisquare()+Combined.GetNDF()
#d = c.GetChisquare()/c.GetNDF()
#r = TString(" ")
#r = str(d)
#print r
#legend.AddEntry(None,r,"ep")
#legend.AddEntry(None,{r},"f")
#LowPt_Mass.Draw()
gau4 = TF1("gau4","gaus",0.98,1.1)
gau4.FixParameter(0,Combined.GetParameter(0))
gau4.FixParameter(1,Combined.GetParameter(1))
gau4.FixParameter(2,Combined.GetParameter(2))
m = Combined.GetParameter(1)
s = Combined.GetParameter(2)
a = m - 2*s
b = m + 2*s
ep4 = TF1("ep4","expo",0.98,1.1)
ep4.FixParameter(0,Combined.GetParameter(3))
ep4.FixParameter(1,Combined.GetParameter(4))
yeild = (gau4.Integral(a,b)-ep4.Integral(a,b))*100/5
print "the yeild is " ,a,b, yeild, gau4.GetParameter(0)
PhiMass.cd(2)
tree.SetMarkerStyle(3)
#canvas.SetColor(rt.Black) 
tree.SetMarkerColor(rt.kRed)
tree.Draw("fM >>LowPt_Mass",TriggerCut+n+KSigmaTPC_Cut+n+ElSigmaTPC_Cut+n+PiSigmaTPC_Cut+n+DaughterPcut+n+PtCut,"e")
#+n+"fKaonSigmaTOF0<-800"+n+"fKaonSigmaTOF1<-800"+")"+Or+"("+TriggerCut+n+KSigmaTOF_Cut+n+PiSigmaTOF_Cut+n+"fPt>1"+n+DaughterPcuthigh2+")","e")
#tree.Draw("fElM >> HighPt_Mass2",TriggerCut+n+KSigmaTPC_Cut+n+PiSigmaTPC_Cut+n+DaughterPcut2+n+"fPt>0.2","SAME")
#"fPt<0.1 && fPd0<0.4 && fPd1<0.4 &&(fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1)<4 && (TMath::Abs(fDCAxy1) < 2) && (TMath::Abs(fDCAxy2) < 2)"
#tree.Draw("fElM >>LowPt_Mass",MuSigmaTPC_Cut,"")



#LowPt_Mass.SetMarkerStyle(rt.kCircle)

#LowPt_Mass.Fit("gaus","B")

#print "chi square for low fit " , gaus.GetChisquare() ,gaus.GetNDF()
#Sigma_Radius.cd()
#tree.Draw("sqrt(fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1):sqrt(fPiSigma0*fPiSigma0 + fPiSigma1 * fPiSigma1) >> SigmaRadius",MassCut,"COLZ")#, "(fPiSigma0*fPiSigma0 + fPiSigma1 * fPiSigma1>25)")#&&(fKaonSigma0*fKaonSigma0 + fKaonSigma1*fKaonSigma1<25)")
#SigmavsSigma.cd()
#tree.Draw("fKaonSigmaTOF0:fKaonSigma0>>SigmavSigma","","COLZ")

dEdX.Divide(2,1)
dEdX.cd(1)
tree.Draw("fdEdX1:fPd1>>dEdXvsP1",PiSigmaTPC_Cut,"COLZ") 

dEdX.cd(2)
tree.Draw("fdEdX1:fPd1>>dEdXvsP2","","COLZ")
#canvas4.SaveAs("dE/dx.png")
#test.cd()
#gau4.Draw()
#Sigma.Fill(fKaonSigma0,fKaonSigma1)
#Sigma.Draw()
#HighPt_Mass.Draw()
#canvas.cd(3)
#fSigma.Draw()
vars = globals()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()

