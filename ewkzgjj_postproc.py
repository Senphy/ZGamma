#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  zgammaModule import *

from  countHistogramsModule import *



#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/2A93F220-480C-E811-B41A-FA163E62B5E7.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/3C52A3B5-540C-E811-8F16-FA163EA77E04.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/3E58C862-A20C-E811-A231-90E2BAC9B7A8.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/464C1632-A20C-E811-9FA3-FA163E5303D3.root","root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/54EEA3FF-460C-E811-AF8A-FA163EED3A98.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && nMuon >= 2 && Muon_pt[0] > 20 && Muon_pt[1] > 20","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)
#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleMuon/NANOAOD/05Feb2018-v1/40000/2A93F220-480C-E811-B41A-FA163E62B5E7.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && nMuon >= 2 && Muon_pt[0] > 20 && Muon_pt[1] > 20","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/80000/DAF92081-7F11-E811-B3F3-0025905C543A.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && ((nMuon >= 2) || (nElectron >= 2))","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/80000/DAF92081-7F11-E811-B3F3-0025905C543A.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && nElectron >= 2","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)

p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/80000/DAF92081-7F11-E811-B3F3-0025905C543A.root"],"","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False,histDirName="myhistdir",histFileName="myhistfile.root")

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/80000/DAF92081-7F11-E811-B3F3-0025905C543A.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && nElectron >= 2 && event == 4784","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/80000/DAF92081-7F11-E811-B3F3-0025905C543A.root"],"nJet >= 2 && Jet_pt[0] >= 30 && Jet_pt[1] >= 30 && nPhoton >= 1 && Photon_pt[0] > 25 && ((nMuon >= 2 && Muon_pt[0] > 20 && Muon_pt[1] > 20) || (nElectron >= 2 && Electron_pt[0] > 20 && Electron_pt[1] > 20))","keep_and_drop.txt",[exampleModule()],provenance=True,justcount=False,noOut=False)

p.run()
