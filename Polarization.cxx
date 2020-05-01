/**************************************************************************
 * Copyright(c) 1998-1999, ALICE Experiment at CERN, All rights reserved. *
 *                                                                        *
 * Author: The ALICE Off-line Project.                                    *
 * Contributors are mentioned in the code where appropriate.              *
 *                                                                        *
 * Permission to use, copy, modify and distribute this software and its   *
 * documentation strictly for non-commercial purposes is hereby granted   *
 * without fee, provided that the above copyright notice appears in all   *
 * copies and that both the copyright notice and this permission notice   *
 * appear in the supporting documentation. The authors make no claims     *
 * about the suitability of this software for any purpose. It is          *
 * provided "as is" without express or implied warranty.                  *
 **************************************************************************/

/* AliAnaysisTaskMyTask*/
// c++ headers
#include <iostream>
#include <string.h>

// root headers
#include "TH1I.h"
#include "TTree.h"
#include "TClonesArray.h"
#include "TParticle.h"
#include "TObjString.h"
#include "TFile.h"
#include "TDatabasePDG.h"
#include "TLorentzVector.h"

// aliroot headers
#include "AliAnalysisManager.h"
#include "AliInputEventHandler.h"
#include "AliESDEvent.h"
#include "AliAODEvent.h"
#include "AliMCEvent.h"
#include "AliAODVZERO.h"
#include "AliAODZDC.h"
#include "AliESDVZERO.h"
#include "AliESDZDC.h"
#include "AliPIDResponse.h"
#include "AliAODTrack.h"
#include "AliAODPid.h"
#include "AliAODVertex.h"
#include "AliESDVertex.h"
#include "AliMultiplicity.h"
#include "AliESDtrack.h"
#include "AliESDMuonTrack.h"
#include "AliAODMCParticle.h"
#include "AliMCParticle.h"
#include "AliCentrality.h"
#include "AliKFVertex.h"
#include "AliExternalTrackParam.h"
//#include "AliTriggerAnalysis.h"
#include "AliAODMCHeader.h"
#include "TChain.h"
#include "TH1F.h"
#include "TList.h"
#include "AliAnalysisTask.h"
#include "AliAODInputHandler.h"
#include "Polarization.h"
#include "AliPIDResponse.h"
#include "TMath.h"

class Polarization;    
using namespace std;            

ClassImp(Polarization) // classimp: necessary for root


Polarization::Polarization() : AliAnalysisTaskSE(), 
    fAOD(0), fOutputList(0), fHistPt(0) , fHistP_TPC(0), fTreeP_TPC(0),fPt(0),fM(0),fPt0(0),fPt1(0),fPIDResponse(0),fKaonSigma1(0),fKaonSigma0(0),fPiSigma1(0),fPiSigma0(0), fTPCcluster1(0), fEta1(0),fTPCcluster2(0), fEta2(0),fHistEtaCut(0),fHistITS(0), fHistChargeCut(0),fHistPtCut(0),fHistPairCut(0),fHistPIDCut(0),
    fHistFilterbitCut(0),fHistTriggerCut(0),fHistCounter(0),fDCAxy2(0),fDCAz2(0),fDCAxy1(0),fDCAz1(0) , fTriggerClass(0),fdEdX(0),fPd(0),fPp(0),fPtd(0),fZDCdata(0),fZNAenergy(0), fZNCenergy(0),fZDCAtime(0),fZDCCtime(0),fMuSigma0(0),fMuSigma1(0),fRabs1(0),fRabs2(0),fTheta(0),fHelicityTheta(0),fCollinTheta(0),fPhi(0),fHelicityPhi(0),fCollinPhi(0)
  {
    // default constructor, don't allocate memory here!
    // this is used by root for IO purposes, it needs to remain empty
  }
//_____________________________________________________________________________
Polarization::Polarization(const char* name) : AliAnalysisTaskSE(name),
    fAOD(0), fOutputList(0), fHistPt(0),fHistP_TPC(0), fTreeP_TPC(0),fPt(0),fM(0),fPt0(0),fPt1(0) ,fPIDResponse(0),fKaonSigma0(0),fKaonSigma1(0),fPiSigma0(0),
    fPiSigma1(0), fTPCcluster1(0), fEta1(0),fTPCcluster2(0), fEta2(0),fHistEtaCut(0),fHistITS(0), fHistChargeCut(0),fHistPtCut(0),fHistPairCut(0),fHistPIDCut(0),
    fHistFilterbitCut(0),fHistTriggerCut(0),fHistCounter(0) ,fDCAxy1(0),fDCAz1(0),fDCAxy2(0),fDCAz2(0),fTriggerClass(0),fdEdX(0),fPd(0),fPp(0),fPtd(0),fZDCdata(0), fZNAenergy(0), fZNCenergy(0),fZDCAtime(0),fZDCCtime(0),fMuSigma0(0),fMuSigma1(0),fRabs1(0), fRabs2(0),fTheta(0),fHelicityTheta(0),fCollinTheta(0),fPhi(0),fHelicityPhi(0),fCollinPhi(0)
  {
    cout<<"constructor"<<endl;
    
    // constructor
    DefineInput(0, TChain::Class());    // define the input of the analysis: in this case we take a 'chain' of events
                                        // this chain is created by the analysis manager, so no need to worry about it, 
                                        // it does its work automatically
    DefineOutput(1, TList::Class());    // define the ouptut of the analysis: in this case it's a list of histograms 
                                        // you can add more output objects by calling DefineOutput(2, classname::Class())
                                        // if you add more output objects, make sure to call PostData for all of them, and to
                                        // make changes to your AddTask macro!
   DefineOutput(2, TTree::Class());
  }
//_____________________________________________________________________________
Polarization::~Polarization()
 {
  // destructor
  if(fOutputList) 
    {
  
    delete fOutputList;     // at the end of your task, it is deleted from memory by calling this function
    }
 }
//_____________________________________________________________________________
void Polarization::UserCreateOutputObjects()
  {
    AliAnalysisManager *man = AliAnalysisManager::GetAnalysisManager();
    if (man) 
      {
        AliInputEventHandler* inputHandler = (AliInputEventHandler*)(man->GetInputEventHandler());
        if (inputHandler)   fPIDResponse = inputHandler->GetPIDResponse();
        if (!fPIDResponse) {
        cout<<"noPIDresopne"<<endl;
        return;
     }
   
  }
    
    
    fOutputList = new TList();          
    fOutputList->SetOwner(kTRUE);       // memory stuff: the list is owner of all objects it contains and will delete them
                                          // if requested (dont worry about this now)
  
      // example of a histogram
    fHistPt = new TH1F("fHistPt", "fHistPt", 100, 0, 10);       
    fOutputList->Add(fHistPt);  
    fHistCounter = new TH1I("fHistCounter","Histogram of Counter",100,0,100);  
    fOutputList->Add(fHistCounter);                              
    fHistP_TPC = new TH2F ("fHistP_TPC","fHistP_TPC",100,0,1,100,0,0.001);       // your histogram in the output file, add it to the list!
    fOutputList->Add(fHistP_TPC);
     
    fTreeP_TPC = new TTree("scatterplot","Momentum and TPC signal");
    fTreeP_TPC->Branch("fPt", &fPt, "fPt/F");
    fTreeP_TPC->Branch("fTheta", &fTheta, "fTheta/F");
    fTreeP_TPC->Branch("fHelicityTheta", &fHelicityTheta, "fHelicityTheta/F");
    fTreeP_TPC->Branch("fCollinTheta", &fCollinTheta, "fCollinTheta/F");
    
    fTreeP_TPC->Branch("fPhi", &fPhi, "fPhi/F");
    fTreeP_TPC->Branch("fHelicityPhi", &fHelicityPhi, "fHelicityPhi/F");
    fTreeP_TPC->Branch("fCollinPhi", &fCollinPhi, "fCollinPhi/F");
    
    fTreeP_TPC->Branch("fM", &fM, "fM/F");
    fTreeP_TPC->Branch("fPt0", &fPt0, "fPt0/F");
    fTreeP_TPC->Branch("fPt1", &fPt1, "fPt1/F"); 
   // fTreeP_TPC->Branch("fKaonSigma0", &fKaonSigma0, "fKaonSigma0/F");
    //fTreeP_TPC->Branch("fKaonSigma1", &fKaonSigma1, "fKaonSigma1/F");
  //   fTreeP_TPC->Branch("fPiSigma0", &fPiSigma0, "fPiSigma0/F");
   // fTreeP_TPC->Branch("fPiSigma1", &fPiSigma1, "fPiSigma1/F");
    fTreeP_TPC->Branch("fMuSigma0", &fMuSigma0, "fMuSigma0/F");
    fTreeP_TPC->Branch("fMuSigma1", &fMuSigma1, "fMuSigma1/F");
    //fTreeP_TPC->Branch("fTPCcluster1", &fTPCcluster1, "fTPCcluster1/F");
    fTreeP_TPC->Branch("fEta1", &fEta1, "fEta1/F");
  //  fTreeP_TPC->Branch("fTPCcluster2", &fTPCcluster2, "fTPCcluster2/F");
    fTreeP_TPC->Branch("fEta2", &fEta2, "fEta2/F");
    fTreeP_TPC->Branch("fDCAxy1", &fDCAxy1, "fDCAxy1/F");
     fTreeP_TPC->Branch("fDCAxy2", &fDCAxy2, "fDCAxy2/F");
    fTreeP_TPC->Branch("fDCAz1", &fDCAz1, "fDCAz1/F");
    fTreeP_TPC->Branch("fDCAz2", &fDCAz2, "fDCAz2/F");
    fTreeP_TPC->Branch("fTriggerClass", &fTriggerClass,"fTriggerClass/I");
    fTreeP_TPC->Branch("fPp", &fPp, "fPp/F");
    fTreeP_TPC->Branch("fPt0", &fPd, "fPd/F");
    fTreeP_TPC->Branch("fPtd", &fPtd, "fPtd/F");
   // fTreeP_TPC->Branch("fdEdX", &fdEdX, "fdEdX/F");
    fTreeP_TPC->Branch("fZNAenergy", &fZNAenergy, "fZNAenergy/F"); 
    fTreeP_TPC->Branch("fZNCenergy", &fZNCenergy, "fZNCenergy/F");
    fTreeP_TPC->Branch("fZDCAtime", &fZDCAtime, "fZDCAtime/F");
    fTreeP_TPC->Branch("fZDCCtime", &fZDCCtime, "fZDCCtime/F");
  //  fTreeP_TPC->Branch("fHistCounter", &fHistCounter, "fHistCounter/I");
    
    PostData(1, fOutputList);           
   
  
    PostData(2,fTreeP_TPC);
  }
//_____________________________________________________________________________
void Polarization::UserExec(Option_t *)
  {



 
     fAOD = dynamic_cast<AliAODEvent*>(InputEvent());    
     if(!fAOD) return;                                  
       
     fHistCounter->Fill(1);
       
     TString trigger = fAOD-> GetFiredTriggerClasses();
  //   if (trigger.Contains("CCUP8")) return; 
    // cout<< "trigger classes are " << trigger << endl; return;  
     if (!trigger.Contains("CMUP")) return;
     if (trigger.Contains("CMUP10")){
         fTriggerClass =10;
         }
     if (trigger.Contains("CMUP11")){
         fTriggerClass =11;
         } 
     if  (trigger.Contains("CMUP13")){
         fTriggerClass =13;
         }  
     if  (trigger.Contains("CMUP26")){
         fTriggerClass =26;
         }
     if  (trigger.Contains("CMUP6")){
         fTriggerClass =6;
         }    
    
      AliAODZDC *fZDCdata = fAOD->GetZDCData();
      fZNAenergy = fZDCdata->GetZNATowerEnergy()[0];
      fZNCenergy = fZDCdata->GetZNCTowerEnergy()[0];
      fZDCAtime = fZDCdata->GetZNATime();
      fZDCCtime = fZDCdata->GetZNCTime();
  //ZDC cuts but not applying here, planning to apply in the final result...
  //if(trigger.Contains("CCUP4-B"))fHistZDCCuts->Fill(1);
  /*if(fZNAenergy < 8200 && fZNCenergy < 8200) fHistZDCCuts->Fill(2);
  if(fZNAenergy < 683 && fZNCenergy < 683) fHistZDCCuts->Fill(3);
  if(fZDCAtime == 0 && fZDCCtime == 0) fHistZDCCuts->Fill(4);*/
  
  
     fHistCounter->Fill(2);            
     Int_t iTracks(fAOD->GetNumberOfTracks()); // see how many tracks there are in the event
     Int_t PairCounter = 0;
     Bool_t GoodTracks = kFALSE;
     Bool_t GoodTracks2 = kFALSE;
     AliAODTrack* savetrack1;
     AliAODTrack* savetrack2;
     for(Int_t i(0); i < iTracks; i++) 
      { 
        AliAODTrack* track = static_cast<AliAODTrack*>(fAOD->GetTrack(i));                // loop ove rall these tracks
        
        fRabs1 = track->GetRAtAbsorberEnd();
        
      //  if(!(track->TestFilterBit(1<<0))) continue;
        fHistCounter->Fill(2); 
        if(track->HasPointOnITSLayer(0) || track->HasPointOnITSLayer(1)) {GoodTracks = kTRUE;}
        
        else  {GoodTracks = kFALSE;}
        if (GoodTracks == kFALSE) fHistCounter->Fill(3);//continue; 
         
           
      
          if (track->Eta()>-2.5||track->Eta()<-4) fHistCounter->Fill(4);//continue;
          if (17.5>fRabs1||fRabs1>89.5) fHistCounter->Fill(5);//continue;
          
          
          
        
        
        
        
      //  if(track->GetTPCNcls() < 60)continue;
       
   //     fHistP_TPC-> Fill(track->P(),track->GetTPCsignal());
   
          fdEdX =track->GetTPCsignal();
          fPtd  = track->Pt();
          fPd  =  TMath::Sqrt(track->Pt()*track->Pt()+track->Pz()*track->Pz());              
        for (Int_t j=i+1 ; j<iTracks ; j++) {
            AliAODTrack* track2 = static_cast<AliAODTrack*>(fAOD->GetTrack(j));
            fRabs2 = track2->GetRAtAbsorberEnd();
            
           /// if(!(track2->TestFilterBit(1<<0))) continue;
          //  fHistCounter->Fill(5);
            if(track2->HasPointOnITSLayer(0) || track2->HasPointOnITSLayer(1)) {GoodTracks2 = kTRUE;}
            else { GoodTracks2 = kFALSE ;}
            if (GoodTracks2 == kFALSE)   fHistCounter-> Fill(6);// continue;
            //  
            if (track2->Eta()>-2.5||track2->Eta()<-4) fHistCounter->Fill(7);//continue;
            
         //   if(track2->GetTPCNcls() < 60)continue;
            fHistCounter->Fill(8);
            PairCounter = PairCounter+1;  
            savetrack1 = track;
            savetrack2 = track2;
            if (PairCounter>1) break;     
            
         
          
          
            }
       //end of for loop j tracks*/
       //fTreeP_TPC ->Fill();
      }//end of for loop i tracks
      //Selecting tracks with only 1 pair of tracks
      if (PairCounter!=1)  return;
      fHistCounter->Fill(9);
     
     
     
      Double_t dca[2] = {0.0,0.0}, cov[3] = {0.0,0.0,0.0};
      AliAODTrack* track1_clone=(AliAODTrack*)savetrack1->Clone("track1_clone");
      AliAODVertex *fAODVertex = fAOD->GetPrimaryVertex();
      if(!track1_clone->PropagateToDCA(fAODVertex,fAOD->GetMagneticField(),300.,dca,cov)) { 
       dca[0] = -999 ;
       dca[1] = -999 ;
       }
      fDCAxy1= dca[0];
      fDCAz1=  dca[1];
      delete track1_clone;
      AliAODTrack* track2_clone=(AliAODTrack*)savetrack2->Clone("track2_clone");
       if(!track2_clone->PropagateToDCA(fAODVertex,fAOD->GetMagneticField(),300.,dca,cov)){ 
       dca [0] = -999 ;
       dca [1] = -999 ;
       }
      fDCAxy2= dca[0];      
      fDCAz2= dca[1];
      delete track2_clone;
      // if(TMath::Abs(dca[1]) > 2) continue;
      //Charge Cut 
     
      if (savetrack1->Charge() * savetrack2->Charge()>= 0) return;
      
      fHistCounter->Fill(10);   
      fPiSigma0=fPIDResponse->NumberOfSigmasTPC(savetrack1, AliPID::kPion);
      fPiSigma1=fPIDResponse->NumberOfSigmasTPC(savetrack2, AliPID::kPion);
      fKaonSigma0=fPIDResponse->NumberOfSigmasTPC(savetrack1, AliPID::kKaon);
      fKaonSigma1=fPIDResponse->NumberOfSigmasTPC(savetrack2, AliPID::kKaon);
      fMuSigma0=fPIDResponse->NumberOfSigmasTPC(savetrack1, AliPID::kMuon);
      fMuSigma1=fPIDResponse->NumberOfSigmasTPC(savetrack2, AliPID::kMuon);
      
  
  
    //if (fKaonSigma0*fKaonSigma0+fKaonSigma1*fKaonSigma1>16) return;
   //   if ((fPiSigma0*fPiSigma0+fPiSigma1*fPiSigma1)<25) return;
      fHistCounter->Fill(11);
      TLorentzVector d1;
      TLorentzVector d2; 
      d1.SetPtEtaPhiM(savetrack1->Pt(),savetrack1->Eta(),savetrack1->Phi(),0.4396);
      d2.SetPtEtaPhiM(savetrack2->Pt(),savetrack2->Eta(),savetrack2->Phi(),0.4396);
      fPt0 = d1.Pt();
      fPt1 = d2.Pt();
     
     
           
      // cout<<"mass of track"<< track->M()<<endl; 
      TLorentzVector p = d1+d2;
      fPt = p.Pt();
      fM =  p.M(); 
      if (p.Rapidity()>-2.5||p.Rapidity()<-4.0) return;//fHistCounter->Fill(15);  
      if (fPt>0.25) fHistCounter->Fill(16);
      
      fPp  = TMath::Sqrt(p.Pt()*p.Pt()+p.Pz()*p.Pz());
      fTPCcluster1 = savetrack1->GetTPCNcls();
      fEta1 = savetrack1->Eta();
      fTPCcluster2 = savetrack2->GetTPCNcls();
      fEta2 = savetrack2->Eta();
      fTreeP_TPC ->Fill();                                // continue until all the tracks are processed
      PostData(1, fOutputList);                           // stream the results the analysis of this event to
      PostData (2,fTreeP_TPC);                            // the output manager which will take care of writing
                                                          // it to a file
  
      }
//_____________________________________________________________________________
void Polarization::Terminate(Option_t *)
  {
    // terminate
   // called at the END of the analysis (when all events are processed)
  }
  //_____________________________________________________________________________
