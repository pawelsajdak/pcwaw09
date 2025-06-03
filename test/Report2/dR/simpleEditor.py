#!/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/external/el9_amd64_gcc12/bin/python3
import ROOT as r
import sys

histfilename = "dRdistribution.root"
histfile = r.TFile.Open(histfilename,"READ")
ihisto = histfile.Get("histodR")
ihisto.SetDirectory(0)
histfile.Close()

histo = ihisto.Rebin(10,"histo")

canvas = r.TCanvas("canvas","canvas",600,200)
canvas.cd()
canvas.SetBottomMargin(0.2)
canvas.SetLeftMargin(0.07)
canvas.SetRightMargin(0.04)
canvas.SetTopMargin(0.07)
#canvas.SetLogy(True)


#histo.SetAxisRange(0.0,0.004, "X")
histo.SetAxisRange(0., 18., "Y")
histo.SetTitle("; min(#DeltaR); Counts")
histo.SetStats(0)

#r.gStyle.SetTitleFontSize(0.08)
histo.SetLabelSize(0.08,"XY")
histo.GetYaxis().SetNdivisions(6,False)
#print(histo.GetYaxis().GetNdivisions())
histo.GetXaxis().SetTitleSize(0.08)
histo.GetXaxis().SetTitleOffset(1.1)
histo.GetYaxis().SetTitleSize(0.08)
histo.GetYaxis().SetTitleOffset(0.4)
histo.GetYaxis().SetTickLength(0.01)
histo.GetXaxis().CenterTitle(True)
histo.SetFillColor(19)
#histo.SetLineColor(28)
histo.Draw("h")




canvas.Print("temp.pdf")
input('press enter to exit')