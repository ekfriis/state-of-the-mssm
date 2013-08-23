#!/usr/bin/env python

'''

Make a summary plot of current experimental bounds on the MSSM

Author: Evan K. Friis, UW Madison

'''

# User options

MIN_X = 90
MAX_X = 800
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


def unsuckify(pave):
    """ Default ROOT Paves just suck. This function unsucks them."""
    pave.SetFillStyle(0)
    pave.SetBorderSize(0)


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

    theory_label = ROOT.TPaveText(0.3, 0.165, 0.9, 0.23, "NDC")
    unsuckify(theory_label)
    theory_label.SetTextSize(0.04)
    theory_label.SetTextAlign(32)
    theory_label.AddText("MSSM m_{h}^{max} scenario, M_{SUSY} = 1 TeV")
    theory_label.Draw()

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
    cms_charged_graph.SetLineColor(ROOT.EColor.kMagenta + 3)
    cms_charged_graph.SetLineStyle(2)

    atlas_graph = make_tgraph(results.atlas_htt.limit)
    atlas_graph.SetLineColor(ROOT.EColor.kRed)

    d0_graph = make_tgraph(results.d0.limit)

    atlas_charged_graph = make_tgraph(results.atlas_chargedh.limit)
    atlas_charged_graph.SetLineColor(ROOT.EColor.kRed)
    atlas_charged_graph.SetLineStyle(2)

    legend = ROOT.TLegend(0.58, 0.25, 0.90, 0.42, "", "NDC")
    unsuckify(legend)

    # NB the draw and legend add orders are different :/
    lep_graph.Draw("lf")
    cms_graph.Draw("lf")
    d0_graph.Draw()
    cms_charged_graph.Draw()
    atlas_graph.Draw()
    atlas_charged_graph.Draw()

    legend.AddEntry(cms_graph, results.cms_htt.label, "f")
    legend.AddEntry(cms_charged_graph, results.cms_chargedh.label, "l")
    legend.AddEntry(atlas_graph, results.atlas_htt.label, "l")
    legend.AddEntry(atlas_charged_graph, results.atlas_chargedh.label, "l")
    legend.AddEntry(d0_graph, results.d0.label, "l")
    legend.AddEntry(lep_graph, results.lep.label, "f")
    legend.Draw()

    # Add some extra lines to cover up any render errors on the fills.
    top_frame_line = ROOT.TLine(MIN_X, MAX_Y, MAX_X, MAX_Y)
    top_frame_line.Draw()

    right_frame_line = ROOT.TLine(MAX_X, 0, MAX_X, MAX_Y)
    right_frame_line.Draw()
    canvas.RedrawAxis()

    canvas.SaveAs("state-of-the-mssm.pdf")
    canvas.SaveAs("state-of-the-mssm.png")
