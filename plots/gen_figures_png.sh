#!/bin/sh
# pdfcrop plots.pdf plots2.pdf
# convert -quality 00 -density 500x500 plots.pdf plots_%d.png
pdftoppm plots.pdf plots -png -rx 500 -ry 500
# rm plots.pdf
