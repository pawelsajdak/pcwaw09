#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys

histname = "histoK_tight_NEW"

histfilename = "Jpsi_K_newdR.root"
histfile = r.TFile.Open(histfilename,"READ")
histo = histfile.Get("histoK_tight")
histo.SetDirectory(0)
histfile.Close()


canvas = r.TCanvas("canvas")
canvas.cd()
canvas.SetBottomMargin(0.12)
canvas.SetLeftMargin(0.12)
canvas.SetRightMargin(0.08)
#canvas.SetTopMargin(0.2)
#canvas.SetLogy(True)

#histo.SetAxisRange(4.2,5.5)
#print(histo.Integral())
histo.SetAxisRange(3.75,5.9, "X")
#print(histo.Integral())
histo.SetAxisRange(7000.,25.e3, "Y")
histo.SetTitle("J/#psi + K^{ #pm}  (#DeltaR > 0.1); M_{ inv} (GeV); Counts")
histo.SetStats(0)

r.gStyle.SetTitleFontSize(0.06)
histo.SetLabelSize(0.04,"XY")
#histo.SetNdivisions(40206, "X")
histo.GetXaxis().SetTitleSize(0.05)
histo.GetXaxis().SetTitleOffset(1.0)
histo.GetYaxis().SetTitleSize(0.05)
histo.GetYaxis().SetTitleOffset(1.2)
histo.GetXaxis().CenterTitle(True)
histo.SetFillColor(19)
#histo.SetLineColor(28)
histo.Draw("h")

'''
funcfilename = histname+"hill"+"_fitFunc.root"
funcfile = r.TFile.Open(funcfilename)
Bfunc = r.gROOT.FindObject("fitFunc")

canvas.cd()
Bfunc.SetLineColor(3)
Bfunc.Draw("same")
'''


# Background line
bgdfilename = histname+"_hill"+"_bgdFunc.root"
bgdfile = r.TFile.Open(bgdfilename)
bgd = r.gROOT.FindObject("bgd")
bgdparams = bgd.GetParameters()
expression = "[0]+[1]*exp([2]*x)"
bgdDrawFunc = r.TF1("bgdDrawFunc",expression,3.8,5.8,3)
bgdDrawFunc.SetParameters(bgdparams)

canvas.cd()
bgdDrawFunc.SetLineColor(6)
bgdDrawFunc.SetLineStyle(2)
bgdDrawFunc.Draw("same")

# Legend
leg = r.TLegend(0.57,0.8,0.92,0.9)
leg.AddEntry("bgdDrawFunc","exponential background","l")
leg.Draw()


'''
l = r.TLatex()
l.SetTextFont(42)
l.SetTextSize(0.06)
l.DrawLatex(5.25,3400.,"B^{ #pm}")
l.SetTextSize(0.035)
#l.DrawLatex(5.4,5300.,"|#it{M_{#mu#mu} - m_{J/#psi}}| < 0.1 GeV")
'''


canvas.Print(histname+"_hill"+"_finePlot.pdf")
input('press enter to exit')