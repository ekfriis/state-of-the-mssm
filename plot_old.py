#!/usr/bin/env python
#import re
import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetFrameLineWidth(2)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetHistLineWidth(3)

def make_tgraph(xys):
    output = ROOT.TGraph(len(xys))
    for i, (x, y) in enumerate(xys):
        output.SetPoint(i, x, y)
    output.SetLineWidth(3)
    return output

min = 100
max = 450
ymax = 50

cms_result_txt = '''
    mass 	    obs      -95%     -68%   median     +68%     +95%
    -----	   -----    -----    -----    -----    -----    -----
    90 	  12.246    5.194    7.009    8.371   10.605   12.836
    100 	  11.799    6.492    7.450    8.777   10.828   13.418
    120 	   9.842    4.500    6.475    8.087    9.889   11.957
    130 	   9.026    5.369    6.710    7.847    9.691   11.453
    140 	   8.031    5.615    6.628    7.901    9.692   11.557
    160 	   7.113    5.574    6.986    8.514   10.419   12.453
    180 	   7.504    6.747    8.140    9.533   11.324   13.762
    200 	   8.464    7.845    9.118   10.519   12.811   14.989
    250 	  13.755   10.327   12.344   13.923   16.765   19.373
    300 	  20.943   13.469   15.704   18.378   21.415   24.471
    350 	  29.124   17.660   20.093   23.025   26.939   31.113
    400 	  37.298   21.923   24.298   27.886   32.449   37.293
    450 	  45.178   25.008   29.164   33.264   38.800   44.728
    500 	  51.904   30.315   35.739   40.510   47.145   55.000
'''

cms_result = []
def is_float(x):
    try:
        float(x)
        return True
    except:
        return False
for line in cms_result_txt.split('\n'):
    if not line:
        continue
    fields = line.split()
    if not is_float(fields[0]):
        continue
    cms_result.append(
        (float(fields[0]), float(fields[1]))
    )

cms_result = [ (-100, 1000) ] + cms_result + [ (1000, 1000) ]


# Extractd from HIG-11-008 NOTE THESE ARE CHARGED HIGGS MASSES
# (HP, TB) -> (MA0, TB) using Feynhiggs
cms_charged_hp = [
    (120.03018282166263,18.789237668161434),
    (140.23212027135793,24.798206278026907),
    (150.06266528688053,39.05829596412556),
    (155.14803955386915,52.33183856502242),
]

# NOTE THESE ARE CHARGED HIGGS MASSES
atlas_charged_hp = [
    ( 90.06321728277304,18.983957219251337 ),
    ( 99.88320530903408,16.203208556149733 ),
    (109.96884798425148,13.422459893048128),
    (120.05733188566093,11.497326203208553),
    (130.0239982140864,12.887700534759357),
    (139.99847791454,16.631016042780743),
    (150.12496321626804,26.14973262032086),
    (160.16230504622064,48.82352941176472),
]

# (HP, TB) -> (MA0, TB) using Feynhiggs
cms_charged = \
        [(87.908369129999997, 18.789237668161434),
         (112.22192412, 24.798206278026907),
         (119.52907261999999, 39.058295964125563),
         (120.42727809, 52.331838565022423)]

# (HP, TB) -> (MA0, TB) using Feynhiggs
atlas_charged = \
        [(38.276520939999997, 18.983957219251337),
         (58.767585250000003, 16.203208556149733),
         (75.369741930000004, 13.422459893048128),
         (89.811092590000001, 11.497326203208553),
         (102.44565561, 12.887700534759357),
         (114.05903626999999, 16.631016042780743),
         (123.93978249, 26.149732620320862),
         (128.24601704, 48.823529411764717),
         (128.24601704, 100) # added to put it off screen
        ]

#Extracted from fig 10a of ATLAS 1.1 fb paper
atlas = [
    (90.08714596949889,28.037383177570092),
    (100.43572984749454,18.598130841121495),
    (109.6949891067538,16.542056074766357),
    (120.58823529411764,13.738317757009346),
    (130.39215686274508,14.11214953271028),
    (140.19607843137254,14.11214953271028),
    (150,16.44859813084112),
    (170.69716775599127,15.794392523364483),
    (200.10893246187362,16.44859813084112),
    (250.21786492374727,19.90654205607477),
    (300.3267973856209,24.859813084112147),
    (349.8910675381263,31.588785046728972),
    (400,40.2803738317757),
    (450.1089324618736,52.803738317757),
]

d0 = [
    (90, 28.8),
    (100, 32.0),
    (110, 33.6),
    (120, 25.0),
    (130, 26.3),
    (140, 28.1),
    (150, 25.3),
    (160, 27.3),
    (170, 29.8),
    (180, 38.4),
    (190, 41.6),
    (200, 45.8),
    (210, 51.8),
    (220, 56.7),
    (230, 60.9),
    (240, 68.6),
    (250, 75.5),
    (260, 81.0),
    (270, 93.5),
    (280, 99.2),
]

hp_lep = [
    (-100, -100),
    (50,100),
    (91,100),
    (91.8,30.02624),
    (91.845,22.07032),
    (91.845,17.12491),
    (91.84523,13.64727),
    (92.61388,11.94143),
    (93.38253,10.03852),
    (94.91982,9.021481),
    (95.68846,8.107481),
    (97.22578,7.141608),
    (99.5317,6.680381),
    (103.375,7.189448),
    (104.1436,7.841313),
    (106.4496,8.326916),
    (109.5242,8.609568),
    (112.5988,8.438845),
    (115.6733,8.107481),
    (118.748,7.384029),
    (122.5912,6.547911),
    (126.4344,5.963618),
    (131.815,5.359424),
    (138.7328,4.752558),
    (144.1134,4.445624),
    (149.4939,4.186368),
    (156.4118,3.968637),
    (164.8669,3.687628),
    (177.1653,3.472575),
    (187.9264,3.29197),
    (203.2994,3.141663),
    (221.7469,2.978266),
    (241.7318,2.861322),
    (261.7167,2.767383),
    (283.2388,2.676528),
    (304.761,2.641027),
    (334.7383,2.554322),
    (357.0292,2.50367),
    (383.9319,2.48701),
    (420.8271,2.454023),
    (452.3417,2.421473),
    (487.6996,2.405361),
]

# extend of screen to prevent rendering errors
hp_lep.append((550,2.405361))
#hp_lep.append((487.6996,0))
hp_lep.append((550,0))
hp_lep.append((550,-100))


if __name__ == "__main__":
    background = ROOT.TH1F("background", "background", max - min, min, max)
    background.GetXaxis().SetTitle("m_{A} [GeV]")
    background.GetXaxis().CenterTitle()
    background.GetYaxis().SetTitle("tan#beta")
    background.GetYaxis().CenterTitle()
    background.GetYaxis().SetTitleSize(0.065)
    background.GetYaxis().SetTitleOffset(0.7)
    background.GetXaxis().SetTitleSize(0.065)
    background.GetXaxis().SetTitleOffset(0.75)
    background.SetMaximum(ymax)
    background.SetStats(0)
    background.SetTitle("")

    canvas = ROOT.TCanvas("blah", "blah", 800, 800)
    canvas.SetLeftMargin(0.11)
    canvas.SetBottomMargin(0.13)

    background.Draw()

    lep_graph = make_tgraph(hp_lep)

    d0_graph = make_tgraph(d0)

    cms_graph = make_tgraph(cms_result)
    cms_color = ROOT.TColor(1501, 0.463, 0.867, 0.957)
    cms_graph.SetLineWidth(9902)
    cms_graph.SetFillColor(1501)
    cms_graph.SetFillStyle(1001)

    cms_charged_graph = make_tgraph(cms_charged)
    cms_charged_graph.SetLineColor(ROOT.EColor.kMagenta+3)
    cms_charged_graph.SetLineStyle(2)

    atlas_charged_graph = make_tgraph(atlas_charged)
    atlas_charged_graph.SetLineColor(ROOT.EColor.kRed)
    atlas_charged_graph.SetLineStyle(2)

    atlas_graph = make_tgraph(atlas)
    atlas_graph.SetLineColor(ROOT.EColor.kRed)

    lep_color = ROOT.TColor(1502, 0.494, 0.694, 0.298)
    lep_graph.SetFillColor(1502)
    lep_graph.SetLineColor(1502)
    lep_graph.SetFillStyle(1001)
    lep_graph.SetLineWidth(-9900)

    lep_graph.Draw("lf")
    cms_graph.Draw('lf')
    d0_graph.Draw()
    cms_charged_graph.Draw()
    atlas_graph.Draw()
    atlas_charged_graph.Draw()

    def unshitify(pave):
        pave.SetFillStyle(0)
        pave.SetBorderSize(0)

    legend = ROOT.TLegend(0.58, 0.25, 0.90, 0.42,
    #legend = ROOT.TLegend(0.62, 0.25, 0.9, 0.48,
                          "", "NDC")

    theory_label = ROOT.TPaveText(0.3, 0.165, 0.9, 0.23, "NDC")
    unshitify(theory_label)
    theory_label.SetTextSize(0.04)
    theory_label.SetTextAlign(32)
    theory_label.AddText("MSSM m_{h}^{max} scenario, M_{SUSY} = 1 TeV")
    theory_label.Draw()

    unshitify(legend)

    legend.AddEntry(cms_graph, "CMS H#tau#tau 4.7 fb^{-1}", "f")
    legend.AddEntry(cms_charged_graph, "CMS H^{+} 2.2 fb^{-1}", "l")
    legend.AddEntry(atlas_graph, "ATLAS H#tau#tau 1.1 fb^{-1}", "l")
    legend.AddEntry(atlas_charged_graph, "ATLAS H^{+} 4.6 fb^{-1}", "l")
    legend.AddEntry(d0_graph, "D0 7.3 fb^{-1}", "l")
    legend.AddEntry(lep_graph, "LEP", "f")

    legend.Draw()

    # Add some extra lines on the right and top
    top_frame_line = ROOT.TLine(min, ymax, max, ymax)
    top_frame_line.Draw()

    right_frame_line = ROOT.TLine(max, 0, max, ymax)
    right_frame_line.Draw()
    canvas.RedrawAxis()

    canvas.SaveAs("mssm_with_taus_summary_plot.pdf")
    canvas.SaveAs("mssm_with_taus_summary_plot.eps")
