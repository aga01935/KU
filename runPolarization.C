#if !defined (__CINT__) || defined (__CLING__)
#include "AliAnalysisAlien.h"
#include "AliAnalysisManager.h"
#include "AliAODInputHandler.h"
#include "Polarization.h"
#endif

void runPolarization()
{    
    
    // set if you want to run the analysis locally (kTRUE), or on grid (kFALSE)
    Bool_t local = kTRUE;
    // if you run on grid, specify test mode (kTRUE) or full grid model (kFALSE)
    Bool_t gridTest = kTRUE;
    
    
    // set the date here  2015 if analyzing 2015 data , 20181 if 2018q data and 20182if 2018r data  
    Int_t date = 2015;
    
    // since we will compile a class, tell root where to look for headers  
#if !defined (__CINT__) || defined (__CLING__)
    gInterpreter->ProcessLine(".include $ROOTSYS/include");
    gInterpreter->ProcessLine(".include $ALICE_ROOT/include");
#else
    gROOT->ProcessLine(".include $ROOTSYS/include");
    gROOT->ProcessLine(".include $ALICE_ROOT/include");
#endif
     
    // create the analysis manager
   
    AliAnalysisManager *mgr = new AliAnalysisManager("AnalysisTaskExample");
    AliAODInputHandler *aodH = new AliAODInputHandler();
    mgr->SetInputEventHandler(aodH);
    

     //gROOT->LoadMacro("$ALICE_ROOT/ANALYSIS/macros/AddTaskPIDResponse.C");
    // AddTaskPIDResponse();

    // compile the class and load the add task macro
    // here we have to differentiate between using the just-in-time compiler
    // from root6, or the interpreter of root5
#if !defined (__CINT__) || defined (__CLING__)
    gInterpreter->LoadMacro("Polarization.cxx++g");
    Polarization *task = reinterpret_cast<Polarization*>(gInterpreter->ExecuteMacro("AddPolarization.C"));
#else
    gROOT->LoadMacro("Polarization.cxx++g");
    gROOT->LoadMacro("AddPolarization.C");
    Polarization *task = AddPolarization();
     
#endif 
    

    if(!mgr->InitAnalysis()) return;
    mgr->SetDebugLevel(2);
    mgr->PrintStatus();
    mgr->SetUseProgressBar(1, 25);

    if(local) {
        // if you want to run locally, we need to define some input
        TChain* chain = new TChain("aodTree");
        // add a few files to the chain (change this so that your local files are added)
        chain->Add("AliAOD.UPCNano.root");
        // start the analysis locally, reading the events from the tchain
        mgr->StartAnalysis("local", chain);
    } else {
        // if we want to run on grid, we create and configure the plugin
        AliAnalysisAlien *alienHandler = new AliAnalysisAlien();
        // also specify the include (header) paths on grid
        alienHandler->AddIncludePath("-I. -I$ROOTSYS/include -I$ALICE_ROOT -I$ALICE_ROOT/include -I$ALICE_PHYSICS/include");
        // make sure your source files get copied to grid
        alienHandler->SetAdditionalLibs("Polarization.cxx Polarization.h");
        alienHandler->SetAnalysisSource("Polarization.cxx");
        // select the aliphysics version. all other packages
        // are LOADED AUTOMATICALLY!
        alienHandler->SetAliPhysicsVersion("vAN-20180829-1");
        // set the Alien API version
        alienHandler->SetAPIVersion("V1.1x");
        
        // MC has no prefix, data has prefix 000
        alienHandler->SetRunPrefix("000");
        // runnumber
       // alienHandler->AddRunNumber(245692);
           
           
       
       
           //2015 run numbers
           if (date==2015){
           alienHandler->AddRunNumber("246087");
              // alienHandler->AddRunNumber("244980 244982 244983 245064 245066 245068 245145 245146 245151 245152 245231 245232 245233 245253 245259 245343 245345 245346 245347 245353 245401 245407 245409 245410 245446 245450 245496 245501 245504 245505 245507 245535 245540 245542 245543 245554 245683 245692 245700 245705 245729 245731 245738 245752 245759 245766 245775 245785 245793 245829 245831 245833 245949 245952 245954 245963 245996 246001 246003 246012 246036 246037 246042 246048 246049 246053 246087 246089 246113 246115 246148 246151 246152 246153 246178 246181 246182 246217 246220 246222 246225 246272 246275 246276 246390 246391 246392 246424 246428 246431 246433 246434 246487 246488 246493 246495 246675 246676 246750 246751 246755 246757 246758 246759 246760 246763 246765 246804 246805 246806 246807 246808 246809 246844 246845 246846 246847 246851 246855 246859 246864 246865 246867 246871 246930 246937 246942 246945 246948 246949 246980 246982 246984 246989 246991 246994");
                           
                           alienHandler->SetGridDataDir("/alice/data/2015/LHC15o");
                           //it appears that nano aod do not exitst for all the run numbers hence will use normal aods
                           alienHandler->SetDataPattern("muon_calo_pass1/AOD229/PWGUD/UD_PbPb_AOD/522_20190828-1630/*UPCNano.root");
                          // alienHandler->SetDataPattern("muon_calo_pass1/AOD229/*AliAOD.root");
                           
                           }
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
              if (date==20181){
                alienHandler->AddRunNumber("296510");
             
             //2018q run numbers
            // alienHandler->AddRunNumber("295585 295586 295587 295588 295589 295612 295615 295665 295666 295667 295668 295671 295673 295675 295676 295677 295714 295716 295717 295718 295719 295723 295725 295753 295754 295755 295758 295759 295762 295763 295786 295788 295791 295816 295818 295819 295822 295825 295826 295829 295831 295854 295855 295856 295859 295860 295861 295863 295881 295908 295909 295910 295913 295936 295937 295941 295942 295943 295945 295947 296061 296062 296063 296065 296066 296068 296123 296128 296132 296133 296134 296135 296142 296143 296191 296192 296194 296195 296196 296197 296198 296241 296242 296243 296244 296246 296247 296269 296270 296273 296279 296280 296303 296304 296307 296309 296312 296377 296378 296379 296380 296381 296383 296414 296419 296420 296423 296424 296433 296472 296509 296510 296511 296514 296516 296547 296548 296549 296550 296551 296552 296553 296615 296616 296618 296619 296622 296623"); 
                                         
                   
                           alienHandler->SetGridDataDir("/alice/data/2018/LHC18q");
                          alienHandler->SetDataPattern("*muon_calo_pass3/AOD225/PWGUD/UD_PbPb_AOD/501_20190723-1440/*AliAOD.UPCNano.root");
                           //  alienHandler->SetDataPattern("muon_calo_pass3/AOD225/*AliAOD.root");
                   
                   
                    }                     
                                         
               
             if (date==20182){                             
           //2018r run numbers
            // alienHandler->AddRunNumber("296690 296691 296694 296749 296750 296781 296784 296785 296786 296787 296791 296793 296794 296799 296836 296838 296839 296848 296849 296850 296851 296852 296890 296894 296899 296900 296903 296930 296931 296932 296934 296935 296938 296941 296966 296967 296968 296969 296971 296975 296976 296979 297029 297031 297035 297085 297117 297118 297119 297123 297124 297128 297129 297132 297133 297193 297194 297196 297218 297219 297221 297222 297278 297310 297312 297315 297317 297363 297366 297367 297372 297379 297380 297405 297408 297413 297414 297415 297441 297442 297446 297450 297451 297452 297479 297481 297483 297512 297537 297540 297541 297542 297544 297558 297588 297590 ");      
                                         
              alienHandler->AddRunNumber("297481");                           
             alienHandler->SetGridDataDir("/alice/data/2018/LHC18r");
             alienHandler->SetDataPattern("*muon_calo_pass3/AOD225/PWGUD/UD_PbPb_AOD/502_20190723-1441/*AliAOD.UPCNano.root");  
            // alienHandler->SetDataPattern("*muon_calo_pass3/AOD225/ *AliAOD.root");
                                                                
                                         
                                         
                     }                    
             
             
        // number of files per subjob
        alienHandler->SetSplitMaxInputFileNumber(40);
        alienHandler->SetExecutable("myTask.sh");
        // specify how many seconds your job may take
        alienHandler->SetTTL(10000);
        alienHandler->SetJDLName("myTask.jdl");

        alienHandler->SetOutputToRunNo(kTRUE);
        alienHandler->SetKeepLogs(kTRUE);
        // merging: run with kTRUE to merge on grid
        // after re-running the jobs in SetRunMode("terminate") 
        // (see below) mode, set SetMergeViaJDL(kFALSE) 
        // to collect final results
        alienHandler->SetMaxMergeStages(1);
        alienHandler->SetMergeViaJDL(kTRUE);

        // define the output folders
        alienHandler->SetGridWorkingDir("Polarization_2015");
        alienHandler->SetGridOutputDir("Polarization_2015");

        // connect the alien plugin to the manager
        mgr->SetGridHandler(alienHandler);
        if(gridTest) {
            // speficy on how many files you want to run
            alienHandler->SetNtestFiles(1);
            // and launch the analysis
            alienHandler->SetRunMode("test");
            mgr->StartAnalysis("grid");
        } else {
            // else launch the full grid analysis
            alienHandler->SetRunMode("full");
            mgr->StartAnalysis("grid");
        }
    }
}
