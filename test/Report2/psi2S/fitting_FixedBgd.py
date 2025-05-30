#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys

histname = "histoPi"
xmin = 4.7
xmax = 6.0
##########################################
histfilename = "psi2S.root"
histfile = r.TFile.Open(histfilename,"READ")
histo = histfile.Get(histname)
histo.SetDirectory(0)
histfile.Close()
rbhisto = histo.Rebin(2,"rbhisto")



# Background function with fitted parameters
bgdfilename = histname+"_bgdFunc.root"
bgdfile = r.TFile.Open(bgdfilename)
bgd = bgdfile.Get("bgd")

# Fitting function
expression = "[0]+[1]*x+[2]*x*x + [3]*exp((-(x-[4])**2)/(2*[5]**2))"# + [6]*exp((-(x-[7])**2)/(2*[8]**2))"
fitFunc = r.TF1("fitFunc",expression,xmin,xmax,6)
fitFunc.SetParameters(1.,1.,1.,200.,5.25,0.1)
fitFunc.SetParameter(0,bgd.GetParameter(0))
fitFunc.SetParameter(1,bgd.GetParameter(1))
fitFunc.SetParameter(2,bgd.GetParameter(2))

results = rbhisto.Fit(fitFunc,"ERSLB")

#'''
funcFile = r.TFile.Open(histname+"_fitFunc.root","UPDATE")
fitFunc.Write()
funcFile.Close()

with open(histname+'_fitResults.txt','a') as of:
    print(results, file=of)
#'''
    
canvas = r.TCanvas("canvas")
canvas.cd()
#canvas.SetLogy(True)

rbhisto.SetAxisRange(4.0,7.0)
#rbhisto.SetAxisRange(3.5, 6., "X")
#rbhisto.SetAxisRange(1500, 3.e3, "Y")
#rbhisto.SetTitle("Lifetime of B^{#pm};t;Counts")
rbhisto.SetStats(0)
rbhisto.Draw("h")
fitFunc.Draw("same")


canvas.Print(histname+"_Fit.pdf")
input('press enter to exit')
