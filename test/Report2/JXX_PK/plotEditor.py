#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys

histname = "histoPK10"

histfilename = "rebinJpsi_P_K_merged.root"
histfile = r.TFile.Open(histfilename,"READ")
histo = histfile.Get(histname)
histo.SetDirectory(0)
histfile.Close()

############
#histo = ohisto.Rebin(2,"histo")
############

canvas = r.TCanvas("canvas")
canvas.cd()
canvas.SetBottomMargin(0.12)
canvas.SetLeftMargin(0.12)
canvas.SetRightMargin(0.08)
#canvas.SetTopMargin(0.2)
#canvas.SetLogy(True)


histo.SetAxisRange(4.5,6.2, "X")
#histo.SetAxisRange(1900, 8.e3, "Y")
histo.SetTitle("J/#psi + K^{ #pm} #pi^{ #mp}; M_{ J/#psi K^{#pm}#pi^{#mp}} (GeV); Counts")
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
fitFunc.SetRange(4.8,5.8)

canvas.cd()
#fitFunc.SetLineColor(3)
fitFunc.Draw("same")
#'''


l = r.TLatex()
l.SetTextFont(42)
l.SetTextSize(0.04)
#l.SetTextAlign(31)
#l.DrawLatex(1.06,220.,"#cbar M_{ J/#psiK^{+}K^{-}} - m_{ B^{0}_{s}} #cbar < 0.12 GeV")
l.DrawLatex(5.42,4050.,"prob. of common vertex > 0.15")
l.DrawLatex(5.5,3300.,"#splitline{m = (5270.88 #pm 0.98) MeV}{#sigma = (44.3 #pm 1.1) MeV}")

canvas.Print(histname+"_finePlot.pdf")
input('press enter to exit')