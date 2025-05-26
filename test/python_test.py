#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3

import ROOT as r # type: ignore


mass  = r.RooRealVar("mass","Minv",0.,500.)
mu    = r.RooRealVar("mu","mu",200.,150.,300.)
lambd = r.RooRealVar("lambd","lambda",50.,40.,60.)
gamma = r.RooRealVar("gamma","gamma",3.,-2.,5.)
delta = r.RooRealVar("delta","delta",3.,1.,5.)

johnson = r.RooJohnson("johnson","johnson",mass,mu,lambd,gamma,delta,)



massFrame = mass.frame(Title="Johnson pdf")
johnson.plotOn(massFrame)

c = r.TCanvas("c","canvas",800,400)
c.cd()
massFrame.Draw()

c.Print()
input('press enter to exit')
