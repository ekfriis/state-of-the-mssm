#!/usr/bin/env python

'''

Make a summary plot of MSSM results

Author: Evan K. Friis, UW Madison

'''

# User options

MIN_X = 90
MAX_X = 500
MAX_Y = 60  # MSSM no longer theoretically well defined above 60

import ROOT

# Results
import results

# General root style preferences
ROOT.gROOT.SetBatch(True)
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetFrameLineWidth(2)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetHistLineWidth(3)


def make_tgraph(xys):
    """ Convert an iterable of (x, y) pairs into a TGraph """
    output = ROOT.TGraph(len(xys))
    for i, (x, y) in enumerate(xys):
        output.SetPoint(i, x, y)
    output.SetLineWidth(3)
    return output


if __name__ == "__main__":
    # Setup the background histogram frame and canvas
    canvas = ROOT.TCanvas("blah", "blah", 800, 800)
    canvas.SetLeftMargin(0.11)
    canvas.SetBottomMargin(0.13)

    background = ROOT.TH1F("background", "background",
                           MAX_X - MIN_X, MIN_X, MAX_X)
    background.GetXaxis().SetTitle("m_{A} [GeV]")
    background.GetXaxis().CenterTitle()
    background.GetYaxis().SetTitle("tan#beta")
    background.GetYaxis().CenterTitle()
    background.GetYaxis().SetTitleSize(0.065)
    background.GetYaxis().SetTitleOffset(0.7)
    background.GetXaxis().SetTitleSize(0.065)
    background.GetXaxis().SetTitleOffset(0.75)
    background.SetMaximum(MAX_Y)
    background.SetStats(0)
    background.SetTitle("")
    background.Draw()

    # Build LEP plot
    lep_graph = make_tgraph(results.lep.limit)
    lep_color = ROOT.TColor(1502, 0.494, 0.694, 0.298)
    lep_graph.SetFillColor(1502)
    lep_graph.SetLineColor(1502)
    lep_graph.SetFillStyle(1001)
    lep_graph.SetLineWidth(-9900)

    cms_graph = make_tgraph(results.cms_htt.limit)
    cms_color = ROOT.TColor(1501, 0.463, 0.867, 0.957)
    cms_graph.SetLineWidth(9902)
    cms_graph.SetFillColor(1501)
    cms_graph.SetFillStyle(1001)

    cms_charged_graph = make_tgraph(results.cms_chargedh.limit)
    cms_charged_graph.SetLineColor(ROOT.EColor.kMagenta+3)
    cms_charged_graph.SetLineStyle(2)

    atlas_graph = make_tgraph(results.atlas_htt.limit)
    atlas_graph.SetLineColor(ROOT.EColor.kRed)

