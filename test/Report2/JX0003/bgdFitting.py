#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys
import numpy as np

histname = "histoK_tight"

class Background:
    def __call__(self, arr,par):
        if (fitRange.IsInside(arr[0])):        
            return par[0] + par[1]*r.TMath.Exp(par[2]*arr[0])
        else:
            r.TF1.RejectPoint()
            return 0.0
##########################################
histfilename = "Jpsi_K_full2024F"
histfile = r.TFile.Open(histfilename+".root","READ")
histo = histfile.Get(histname)
histo.SetDirectory(0)
histfile.Close()

xmin = 3.8
xmax = 5.8
axmin = 3.8
axmax = 6.0-1.e-5

fitRange = r.Fit.DataRange()
fitRange.AddRange(xmin,4.5)
fitRange.AddRange(4.8,5.1)
fitRange.AddRange(5.4,xmax)
b = Background()
fitFunc = r.TF1("fitFunc",b,xmin,xmax,3)
fitFunc.SetParameters(6300.,4.e6,-1.4)

results = histo.Fit(fitFunc,"ERSL")

outname = histname+"_hill_bgd"
'''
funcFile = r.TFile.Open(outname+"Func.root","RECREATE")
fitFunc.Write("bgd")
funcFile.Close()

with open(outname+'Fit.txt','a') as of:
    print(results, file=of)
'''    

canvas = r.TCanvas("canvas")
canvas.cd()
#canvas.SetLogy(True)

#histo.SetAxisRange(axmin,axmax,"X")
#histo.SetAxisRange(xmin-0.1, xmax+0.1, "X")
#histo.SetAxisRange(2.e3, 7.e3, "Y")
#histo.SetTitle(peakname+"\t {:.3f}".format(fitFunc.GetParameter(1))+"; Minv; #events")
histo.SetStats(0)
histo.Draw("h")


canvas.Print(outname+".pdf")
input('press enter to exit')