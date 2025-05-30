#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys
import numpy as np

# par:  mu   lambda  gamma   delta  a0  a1  a2  johnson_amplitude
class Johnson:
    def __call__(self,arr,par):
        x = arr[0]
        arg = (x-par[0])/par[1]
        expo = par[2] + par[3]*r.TMath.ASinH(arg)
        result = par[7]*par[3]/r.TMath.Sqrt(r.TMath.TwoPi())/(par[1]*r.TMath.Sqrt(1.+arg*arg))*r.TMath.Exp(-0.5*expo*expo)

        result += par[4] + x*par[5] + x*x*par[6]    # parabolic background
        return result
        
#############################################################
peakname = "Jpsi_KK__Bpm"
xmin = 4.8
xmax = 6.0
##########################################
histfilename = "rebin3partMinv.root"
histfile = r.TFile.Open(histfilename,"READ")
histo = histfile.Get("histoK10")
histo.SetDirectory(0)
histfile.Close()

# Background function with fitted parameters
bgdfilename = "histoK10"+"_bgdFunc.root"
bgdfile = r.TFile.Open(bgdfilename)
bgd = r.gROOT.FindObject("bgd")
#bgd.Print()

# Fitting function
john = Johnson()
fitFunc = r.TF1("fitFunc",john,xmin,xmax,8)
fitFunc.SetParameters(5.34,0.05,-1.,1.3,1.,1.,1.,100.)
fitFunc.SetParameter(4,bgd.GetParameter(0))
fitFunc.SetParameter(5,bgd.GetParameter(1))
fitFunc.SetParameter(6,bgd.GetParameter(2))


#'''
results = histo.Fit(fitFunc,"ERSLB")
funcFile = r.TFile.Open(peakname+"_fitFunc.root","RECREATE")
fitFunc.Write()
funcFile.Close()

with open(peakname+'_FitResults.txt','a') as of:
    print(results, file=of)
#'''
    
canvas = r.TCanvas("canvas")
canvas.cd()
#canvas.SetLogy(True)

histo.SetAxisRange(4.0,8.0)
#histo.SetAxisRange(3.5, 6., "X")
#histo.SetAxisRange(1500, 3.e3, "Y")
#histo.SetTitle("Lifetime of B^{#pm};t;Counts")
#histo.SetStats(0)
histo.Draw("h")
fitFunc.Draw("same")


canvas.Print(peakname+"_Fit.pdf")
input('press enter to exit')
