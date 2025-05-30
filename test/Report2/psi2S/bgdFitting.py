#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys
import numpy as np

histname = "histoPi"

class Background:
    def __call__(self, arr,par):
        if (fitRange.IsInside(arr[0])):        
            return par[0] + par[1]*arr[0] + par[2]*arr[0]*arr[0]
        else:
            r.TF1.RejectPoint()
            return 0.0
##########################################
histfilename = "psi2S.root"
histfile = r.TFile.Open(histfilename,"READ")
histo = histfile.Get(histname)
histo.SetDirectory(0)
histfile.Close()
rbhisto = histo.Rebin(2,"rbhisto")

xmin = 4.7
xmax = 6.0
axmin = 4.0
axmax = 7.0

fitRange = r.Fit.DataRange()
fitRange.AddRange(xmin,4.9)
fitRange.AddRange(5.4,xmax)
b = Background()
fitFunc = r.TF1("fitFunc",b,xmin,xmax,3)
#fitFunc.SetParameters(-4750.,0.32,6180.)

results = rbhisto.Fit(fitFunc,"ERSL")

outname = histname+"_bgd"
#'''
funcFile = r.TFile.Open(outname+"Func.root","RECREATE")
fitFunc.Write("bgd")
funcFile.Close()

with open(outname+'Fit.txt','a') as of:
    print(results, file=of)
#'''    

canvas = r.TCanvas("canvas")
canvas.cd()
canvas.SetLogy(True)

rbhisto.SetAxisRange(axmin,axmax)
#rbhisto.SetAxisRange(xmin-0.1, xmax+0.1, "X")
#rbhisto.SetAxisRange(2.e3, 7.e3, "Y")
#rbhisto.SetTitle(peakname+"\t {:.3f}".format(fitFunc.GetParameter(1))+"; Minv; #events")
rbhisto.SetStats(0)
rbhisto.Draw("h")


canvas.Print(outname+".pdf")
input('press enter to exit')