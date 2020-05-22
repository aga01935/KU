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
//#include "AliPIDResponse.h"
#include "AliAODTrack.h"
#include "AliAODPid.h"
#include "AliAODVertex.h"
#include "AliESDVertex.h"
#include "AliMultiplicity.h"
//#include "AliESDtrack.h"
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
#include "AliMuonTrackCuts.h"
#include "AliAODVertex.h"




class Polarization;    
using namespace std;            

ClassImp(Polarization) // classimp: necessary for root


Polarization::Polarization() : AliAnalysisTaskSE(), 
    fAOD(0), fOutputList(0), fTree(0),fMass_mumu_Pair(0),fHistCounter(0),fDCAxy1(0),fDCAxy2(0),fDCAz1(0),fDCAz2(0) , fTriggerClass(0),fZDCdata(0),fZNAenergy(0), fZNCenergy(0),fZDCAtime(0),fZDCCtime(0),fRabs1(0),fRabs2(0),fTheta(0),fHelicityTheta(0),fCollinTheta(0),fPhi(0),fHelicityPhi(0),fCollinPhi(0), daughter1(0.,0.,0.,0.), daughter2(0.,0.,0.,0.) , parent(0.,0.,0.,0.), fHistRunCounter(0),fRunNumber(0),fHistCMUPTriggers(0),fHistCMUP6Triggers(0),fHistCMUP10Triggers(0),fHistCMUP11Triggers(0),fHistCMUP13Triggers(0),fHistCMUP26Triggers(0),fCharge_Track1(0),fCharge_Track2(0),fMuonTrackCuts(0x0),fgoodtracks(0)
  {
    // default constructor, don't allocate memory here!
    // this is used by root for IO purposes, it needs to remain empty
  }
//_____________________________________________________________________________
Polarization::Polarization(const char* name) : AliAnalysisTaskSE(name),
    fAOD(0), fOutputList(0), fTree(0),fMass_mumu_Pair(0),fHistCounter(0) ,fDCAxy1(0),fDCAz1(0),fDCAxy2(0),fDCAz2(0),fTriggerClass(0),fZDCdata(0), fZNAenergy(0), fZNCenergy(0),fZDCAtime(0),fZDCCtime(0),fRabs1(0), fRabs2(0),fTheta(0),fHelicityTheta(0),fCollinTheta(0),fPhi(0),fHelicityPhi(0),fCollinPhi(0), daughter1(0.,0.,0.,0.), daughter2(0.,0.,0.,0.) , parent(0.,0.,0.,0.), fHistRunCounter(0),fRunNumber(0),fHistCMUPTriggers(0),fHistCMUP6Triggers(0),fHistCMUP10Triggers(0),fHistCMUP11Triggers(0),fHistCMUP13Triggers(0),fHistCMUP26Triggers(0),fCharge_Track1(0),fCharge_Track2(0),fMuonTrackCuts(0x0),fgoodtracks(0)
{
    
    
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
      
   if(fMuonTrackCuts) 
      {
  
      delete fMuonTrackCuts;     // at the end of your task, it is deleted from memory by calling this function
      }
      
      
 }





//_____________________________________________________________________________
void Polarization::UserCreateOutputObjects()
  {
 /*   AliAnalysisManager *man = AliAnalysisManager::GetAnalysisManager();
    if (man) 
      {
        AliInputEventHandler* inputHandler = (AliInputEventHandler*)(man->GetInputEventHandler());
        if (inputHandler)   fPIDResponse = inputHandler->GetPIDResponse();
        if (!fPIDResponse) {
        cout<<"noPIDresopne"<<endl;
        return;
     }
   
  }*/
  
  // these are form evgeny it is implemented in multiple muon analysis so I plan to implement it. The only problem I faced is that my code could not find the AliMuonTrackCuts header file even after updating my AliPhysics, I fixed by copying the header files to my working directory
  
    fMuonTrackCuts = new AliMuonTrackCuts("StdMuonCuts", "StdMuonCuts");
    fMuonTrackCuts->SetFilterMask(AliMuonTrackCuts::kMuEta | AliMuonTrackCuts::kMuPdca | AliMuonTrackCuts::kMuMatchLpt);	
    fMuonTrackCuts->SetAllowDefaultParams(kTRUE);
    fMuonTrackCuts->Print("mask");
    
    
    fOutputList = new TList();          
    fOutputList->SetOwner(kTRUE);       // memory stuff: the list is owner of all objects it contains and will delete them
                                          // if requested (dont worry about this now)
  
     
    fHistCounter = new TH1I("fHistCounter","Histogram of Counter",40,0,40);
      
    fOutputList->Add(fHistCounter);                              
    fHistRunCounter = new TH1D("fHistRunCounter","Counter", 70000, 240000.5, 310000.5);
    fOutputList->Add(fHistRunCounter);
   
   
    fHistCMUPTriggers= (TH1D*)fHistRunCounter->Clone("fHistCMUPTriggers");
    fHistCMUP6Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP6Triggers");
    fHistCMUP10Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP10Triggers");
    fHistCMUP11Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP11Triggers");
    fHistCMUP13Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP13Triggers");
    fHistCMUP26Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP26Triggers");
    fOutputList->Add(fHistCMUPTriggers); 
    fOutputList->Add(fHistCMUP6Triggers);
    fOutputList->Add(fHistCMUP10Triggers);
    fOutputList->Add(fHistCMUP11Triggers);
    fOutputList->Add(fHistCMUP13Triggers);
    fOutputList->Add(fHistCMUP26Triggers);
        
        
   //Defining the tree branches to fill therequired information.
   //
   
   
   
    fTree = new TTree("result","Momentum and TPC signal");
    
    
    fTree->Branch("daughter1","TLorentzVector",&daughter1);
    fTree->Branch("daughter2","TLorentzVector",&daughter2);
    fTree->Branch("parent","TLorentzVector",&parent);
    
    fTree->Branch("fTheta", &fTheta, "fTheta/F");
    fTree->Branch("fHelicityTheta", &fHelicityTheta, "fHelicityTheta/F");
    fTree->Branch("fCollinTheta", &fCollinTheta, "fCollinTheta/F");
    
    fTree->Branch("fPhi", &fPhi, "fPhi/F");
    fTree->Branch("fHelicityPhi", &fHelicityPhi, "fHelicityPhi/F");
    fTree->Branch("fCollinPhi", &fCollinPhi, "fCollinPhi/F");
    
    fTree->Branch("fMass_mumu_Pair", &fMass_mumu_Pair, "fMass_mumu_Pair/F");
    
    
    
    
  
    fTree->Branch("fDCAxy1", &fDCAxy1, "fDCAxy1/F");
    fTree->Branch("fDCAxy2", &fDCAxy2, "fDCAxy2/F");
    fTree->Branch("fDCAz1", &fDCAz1, "fDCAz1/F");
    fTree->Branch("fDCAz2", &fDCAz2, "fDCAz2/F");
    fTree->Branch("fTriggerClass", &fTriggerClass,"fTriggerClass/I");
    fTree->Branch("fZNAenergy", &fZNAenergy, "fZNAenergy/F"); 
    fTree->Branch("fZNCenergy", &fZNCenergy, "fZNCenergy/F");
    fTree->Branch("fZDCAtime", &fZDCAtime, "fZDCAtime/F");
    fTree->Branch("fZDCCtime", &fZDCCtime, "fZDCCtime/F");
    
    fTree->Branch("fCharge_Track1", &fCharge_Track1,"fCharge_Track1/I");
    fTree->Branch("fCharge_Track2", &fCharge_Track2,"fCharge_Track2/I");
    fTree->Branch("fRunNumber", &fRunNumber,"fRunNumber/I");
    fTree->Branch("fgoodtracks", &fgoodtracks,"fgoodtracks/I");
    

    
    PostData(1, fOutputList);           
   
  
    PostData(2,fTree);
  }
//_____________________________________________________________________________





void Polarization::UserExec(Option_t *)
  {



 
     fAOD = dynamic_cast<AliAODEvent*>(InputEvent());    
     if(!fAOD) return;                                  
     fRunNumber = fAOD ->GetRunNumber();  
     AliVVZERO *fV0data = fAOD->GetVZEROData();
     AliVAD *fADdata = fAOD->GetADData();
     AliVVZERO *dataVZERO = dynamic_cast<AliVVZERO*>(fAOD->GetVZEROData());
     
     
     
   //  Int_t //bincounter =0;
     
     
     fHistCounter->Fill(0);
     fHistCounter->GetXaxis()->SetBinLabel(1,"Events");
    // //bincounter++;
       
    
   
   
   
     TString trigger = fAOD-> GetFiredTriggerClasses();
    
     if (!trigger.Contains("CMUP"))  return;
     
     
     fHistCMUPTriggers->Fill(fRunNumber);
     
     
     
     fHistCounter->Fill(1);
     fHistCounter->GetXaxis()->SetBinLabel(2,"CMUP_Trigger");
     
  
     if (trigger.Contains("CMUP10")){
            fTriggerClass =10; fHistCounter->Fill(30);
            fHistCounter->GetXaxis()->SetBinLabel(31,"CMUP10");
            fHistCMUP10Triggers->Fill(fRunNumber);
             
                              }
     if (trigger.Contains("CMUP11")){
         fTriggerClass =11;
         fHistCounter->Fill(31);
         fHistCounter->GetXaxis()->SetBinLabel(32,"CMUP11");
         fHistCMUP11Triggers->Fill(fRunNumber); 
         } 
         
     if  (trigger.Contains("CMUP13")){
         fTriggerClass =13; fHistCounter->Fill(32);
         fHistCounter->GetXaxis()->SetBinLabel(33,"CMUP13");
         
         fHistCMUP13Triggers->Fill(fRunNumber);
         }  
     if  (trigger.Contains("CMUP26")){
         fTriggerClass =26; fHistCounter->Fill(33);
         fHistCounter->GetXaxis()->SetBinLabel(34,"CMUP26");
         fHistCMUP26Triggers->Fill(fRunNumber);
         
         }
     if  (trigger.Contains("CMUP6")){
         fTriggerClass =6; fHistCounter->Fill(34);
         fHistCounter->GetXaxis()->SetBinLabel(35,"CMUP6");
         fHistCMUPTriggers->Fill(fRunNumber);
         }  
         
         
         
         
         
    Int_t fV0Adecision = fV0data->GetV0ADecision();
    Int_t fV0Cdecision = fV0data->GetV0CDecision();
    if( fV0Adecision != 0 || fV0Cdecision != 0) return;
    fHistCounter->Fill(2);
       fHistCounter->GetXaxis()->SetBinLabel(3,"V0Decision");
     
    
    
    Int_t fADAdecision = fADdata->GetADADecision();
    Int_t fADCdecision = fADdata->GetADCDecision();
    if( fADAdecision != 0 || fADCdecision != 0) return;
    fHistCounter->Fill(3);
    fHistCounter->GetXaxis()->SetBinLabel(4,"AD decision");
      
    Bool_t fV0Hits[64];
    Int_t fV0TotalNCells = 0;
    for(Int_t iV0Hits = 0; iV0Hits < 64; iV0Hits++) {
       
        fV0Hits[iV0Hits] = dataVZERO->GetBBFlag(iV0Hits);
          
          if(fV0Hits[iV0Hits] == kTRUE) {
                // if(iV0Hits < 32) fV0TotalNCells += fV0Hits[iV0Hits];
                if(iV0Hits < 32) fV0TotalNCells += 1;
          }
          // std::cout << "fV0Hits[iV0Hits = " << iV0Hits << ", fRunNum=" << fRunNum << "] = " << fV0Hits[iV0Hits] << endl;
          // std::cout << "fV0TotalNCells (fRunNum = " << fRunNum << ") = " << fV0TotalNCells << endl;
    }
    
    if(fV0TotalNCells>2) return;
    
    fHistCounter->Fill(4);
    fHistCounter->GetXaxis()->SetBinLabel(5,"fV0TotalNCells<2"); 
             
    // cout<<trigger<<endl;     
    
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
  
  
    // fHistCounter->Fill(2);            
     Int_t iTracks(fAOD->GetNumberOfTracks()); // see how many tracks there are in the event
     Int_t PairCounter = 0;   // coun the number of pairs 
     
     AliAODTrack* savetrack1;
     AliAODTrack* savetrack2;
     
    
    
     for(Int_t i(0); i < iTracks; i++) 
      { 
        AliAODTrack* track = static_cast<AliAODTrack*>(fAOD->GetTrack(i));                // loop ove rall these tracks
        
        fRabs1 = track->GetRAtAbsorberEnd();
        if(!track->IsMuonTrack()) continue;
              fHistCounter->Fill(5);
              fHistCounter->GetXaxis()->SetBinLabel(6,"MuonTrack");
              ////bincounter++;
              
              
              
              if(fMuonTrackCuts->IsSelected(track)) {cout<<"found some tracks"<<endl; fgoodtracks = 1;}
            //  if(!fMuonTrackCuts->IsSelected(track)) cout<<"there is no good tracks"<<endl; fgoodtracks =-999;
               
              fHistCounter->Fill(6);
              fHistCounter->GetXaxis()->SetBinLabel(7,"GoodMuonTrack");
             // //bincounter++;      
        
          
          
        
           
                  
          for (Int_t j=i+1 ; j<iTracks ; j++) {
            //cout<<"entering track loops"<<endl;
              AliAODTrack* track2 = static_cast<AliAODTrack*>(fAOD->GetTrack(j));
            
              
              fRabs2 = track2->GetRAtAbsorberEnd();
              
           
              
                        
      
        
        
        
        
              
            
              
         
              if (track->Pt()>1) continue;
              
              if (track2->Pt()>1) continue;  
              
              fHistCounter->Fill(7);
              fHistCounter->GetXaxis()->SetBinLabel(8,"Pt_track<1");
             // //bincounter++;
              //cout<< track2->Pt()<<endl;
        
              
              
              if (track->Eta()>-2.5||track->Eta()<-4) continue; //fHistCounter->Fill(4);//continue;
              if (track2->Eta()>-2.5||track2->Eta()<-4) continue;
              fHistCounter->Fill(8);
              fHistCounter->GetXaxis()->SetBinLabel(9,"eta_250_400");
             
             
              if (17.5>fRabs1||fRabs1>89.5) continue;//fHistCounter->Fill(5);//continue;
              if (17.5>fRabs2||fRabs2>89.5) continue;
              fHistCounter->Fill(9);
              fHistCounter->GetXaxis()->SetBinLabel(10,"Rabs175_895");
          
            
             
             //some debuggers  to make sure the cut is working as I am little concerned they might not work
              if (track->Pt()>1) cout<<"pt cut in track 1 not working"<<endl;
              if (track2->Pt()>1) cout<<"pt cut in track 2 not working"<<endl;
              if(17.5>fRabs2) cout<<"rabs cut not working on track 2"<<endl;
              if(89.5<fRabs2) cout<<"rabs cut not working on track 2"<<endl;
              if(-2.5<track2->Eta()) cout<<"eta cut not working"<<endl;
              if(-4>track2->Eta()) cout<<"eta cut not working on track 2"<<endl;
              if(17.5>fRabs1) cout<<"rabs cut not working on track 2"<<endl;
              if(89.5<fRabs1) cout<<"rabs cut not working on track 2"<<endl;
              if(-2.5<track->Eta()) cout<<"eta cut not working"<<endl;
              if(-4>track->Eta()) cout<<"eta cut not working on track 2"<<endl; 
           
             
             
             
              //fHistCounter->Fill(8);
              PairCounter = PairCounter+1;  
              savetrack1 = track;
              savetrack2 = track2;
             
             // i am braking it to make so that code do not run if pair is more than 1..
             // it makes code run faster 
          //    if (PairCounter>1) break;     
            //  if (PairCounter>2)break;
             
            
              }
       //end of for loop j tracks*/
      // //bincounter_preserve = //bincounter;
      // //bincounter = //bincounter_diffuse;
      }//end of for loop i tracks
      //Selecting tracks with only 1 pair of tracks
    //  //bincounter = //bincounter_preserve;
     
      if (PairCounter!=1)  return;
      
      fHistCounter->Fill(10);
      fHistCounter->GetXaxis()->SetBinLabel(11,"Single_Pair");
         
     
     
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
  /*   //i am not using this cut as pdca cut is applied in 
      if(TMath::Abs(dca[1]) > 2) return;
      
      
      //Charge Cut 
     fHistCounter->Fill(7);
     
     fHistCounter->Fill(//bincounter);
     fHistCounter->GetXaxis()->SetBinLabel(//bincounter+1,"dca<2");
     //bincounter++;
      
      */
      if (savetrack1->Charge() * savetrack2->Charge()>= 0) return;
      
      
      
     fHistCounter->Fill(11);
     fHistCounter->GetXaxis()->SetBinLabel(12,"OP_Charge");
    
      TLorentzVector d1;
      TLorentzVector d2; 
      d1.SetPtEtaPhiM(savetrack1->Pt(),savetrack1->Eta(),savetrack1->Phi(),TDatabasePDG::Instance()->GetParticle(13)->Mass());
      d2.SetPtEtaPhiM(savetrack2->Pt(),savetrack2->Eta(),savetrack2->Phi(),TDatabasePDG::Instance()->GetParticle(13)->Mass());
     
      daughter1=d1;
      daughter2=d2;
     
    
           
      // cout<<"mass of track"<< track->M()<<endl; 
      
      
      
      TLorentzVector p = d1+d2;
      
     
      parent = p;
   //   fPt = p.Pt();
      fMass_mumu_Pair=  p.M(); 
     //  cout<<"mass of muon pair"<< fM <<endl;
      if (p.Rapidity()>-2.5||p.Rapidity()<-4.0) return;//fHistCounter->Fill(15);  
      if (p.Rapidity()> -2.5){ cout<<"this cut is not working"<<endl;}
      if (p.Rapidity()< -4) { cout<<"this cut is not working"<<endl;}
      fHistCounter->Fill(12);
      fHistCounter->GetXaxis()->SetBinLabel(13,"Parent_Rap");
      //bincounter++;
      
      
      if (p.Pt()>0.25)  return;      
      fHistCounter->Fill(13);
      fHistCounter->GetXaxis()->SetBinLabel(14,"Parent_Pt");
      //bincounter++;
      
      
      
      fPhi =  p.Phi();
     fTheta = p.Theta();
     fHelicityTheta= CosThetaHelicityFrame(d1,d2,p);
     fCollinTheta= CosThetaCollinsSoper(d1,d2,p);
      
     fHelicityPhi= CosPhiHelicityFrame(d1,d2,p);
     fCollinPhi=  CosPhiCollinsSoper(d1,d2,p);
     
     fCharge_Track1 = savetrack1->Charge();
     fCharge_Track2 = savetrack2->Charge();
      
      
      
      
      
      
      
     // fPp  = TMath::Sqrt(p.Pt()*p.Pt()+p.Pz()*p.Pz());
    //  fTPCcluster1 = savetrack1->GetTPCNcls();
     // fEta1 = savetrack1->Eta();
    //  fTPCcluster2 = savetrack2->GetTPCNcls();
    //  fEta2 = savetrack2->Eta();
      
      
      fTree ->Fill();                                // continue until all the tracks are processed
      PostData(1, fOutputList);                           // stream the results the analysis of this event to
      PostData (2,fTree);                            // the output manager which will take care of writing
      //bincounter =0;                                                    // it to a file
  
      }
      
      



Double_t Polarization::CosPhiHelicityFrame(  TLorentzVector muonPositive,
                                                          TLorentzVector muonNegative,
                                                          TLorentzVector possibleJPsi )
{
  /* - This function computes the helicity phi for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
  */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  //
  // --- Determine the z axis for the calculation of the polarization angle
  // (i.e. the direction of the dimuon in the CM system)
  //
  TVector3 zaxis = (possibleJPsi.Vect()).Unit();
  TVector3 yaxis = ((pProjDimu.Vect()).Cross(pTargDimu.Vect())).Unit();
  TVector3 xaxis = (yaxis.Cross(zaxis)).Unit();
  //
  // --- Calculation of the azimuthal angle (Helicity)
  //
  Double_t phi = TMath::ATan2((pMu1Dimu.Vect()).Dot(yaxis),(pMu1Dimu.Vect()).Dot(xaxis));
  return   phi;
}      
      


Double_t Polarization::CosPhiCollinsSoper( TLorentzVector muonPositive,
                                                        TLorentzVector muonNegative,
                                                        TLorentzVector possibleJPsi )
{
  /* - This function computes the Collins-Soper PHI for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
   */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  /* - Determine the z axis for the CS angle.
     -
   */
  TVector3 zaxisCS=(((pProjDimu.Vect()).Unit())-((pTargDimu.Vect()).Unit())).Unit();
  //
  // --- Determine the CS angle (angle between mu+ and the z axis defined above)
  //
  TVector3 yaxisCS=(((pProjDimu.Vect()).Unit()).Cross((pTargDimu.Vect()).Unit())).Unit();
  TVector3 xaxisCS=(yaxisCS.Cross(zaxisCS)).Unit();

  Double_t phi = TMath::ATan2((pMu1Dimu.Vect()).Dot(yaxisCS),((pMu1Dimu.Vect()).Dot(xaxisCS)));
  return   phi;
}



Double_t Polarization::CosThetaCollinsSoper( TLorentzVector muonPositive,
                                                          TLorentzVector muonNegative,
                                                          TLorentzVector possibleJPsi )
{
  /* - This function computes the Collins-Soper cos(theta) for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
   */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  /* - Determine the z axis for the CS angle.
     -
   */
  TVector3 zaxisCS=(((pProjDimu.Vect()).Unit())-((pTargDimu.Vect()).Unit())).Unit();
  /* - Determine the CS angle (angle between mu+ and the z axis defined above)
     -
   */
  Double_t CosThetaCS = zaxisCS.Dot((pMu1Dimu.Vect()).Unit());
  return   CosThetaCS;
}


Double_t Polarization::CosThetaHelicityFrame( TLorentzVector muonPositive,
                                                           TLorentzVector muonNegative,
                                                           TLorentzVector possibleJPsi )
{
  /* - This function computes the Helicity cos(theta) for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
   */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  //
  // --- Determine the z axis for the calculation of the polarization angle
  // (i.e. the direction of the dimuon in the CM system)
  //
  TVector3 zaxis = (possibleJPsi.Vect()).Unit();
  /* - Determine the He angle (angle between mu+ and the z axis defined above)
     -
   */
  Double_t CosThetaHE = zaxis.Dot((pMu1Dimu.Vect()).Unit());
  return   CosThetaHE;

}





      
//_____________________________________________________________________________
void Polarization::Terminate(Option_t *)
  {
    // terminate
   // called at the END of the analysis (when all events are processed)
  }
  //_____________________________________________________________________________
