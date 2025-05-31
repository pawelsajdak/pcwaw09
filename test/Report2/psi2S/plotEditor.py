#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys

histname = "histoPi"

histfilename = "psi2S.root"
histfile = r.TFile.Open(histfilename,"READ")
ohisto = histfile.Get(histname)
ohisto.SetDirectory(0)
histfile.Close()

############
histo = ohisto.Rebin(2,"histo")
############

canvas = r.TCanvas("canvas")
canvas.cd()
canvas.SetBottomMargin(0.12)
canvas.SetLeftMargin(0.12)
canvas.SetRightMargin(0.08)
#canvas.SetTopMargin(0.2)
#canvas.SetLogy(True)


histo.SetAxisRange(4.,7., "X")
#histo.SetAxisRange(1900, 8.e3, "Y")
histo.SetTitle("#psi(2S) + #pi^{#pm};M_{ inv} (GeV); Counts")
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

#'''
funcfilename = histname+"_fitFunc.root"
funcfile = r.TFile.Open(funcfilename,"READ")
fitFunc = r.gROOT.FindObject("fitFunc")

canvas.cd()
#fitFunc.SetLineColor(3)
fitFunc.Draw("same")
#'''


l = r.TLatex()
l.SetTextFont(42)
l.SetTextSize(0.04)
#l.SetTextAlign(31)
l.DrawLatex(5.8,1820.,"#splitline{m = (5.183 #pm 0.004) GeV}{#sigma = (0.0513 #pm 0.0037) GeV}")


canvas.Print(histname+"_finePlot.pdf")
input('press enter to exit')