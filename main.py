# -*- coding: utf_8 -*-
import sys, codecs
import wikiscraper
import IO
import argparse

# set default encoding to utf-8. "-1" is the StreamWriter class of the CodecInfo object returned
sys.stdout = codecs.lookup('utf_8')[-1](sys.stdout)

# initialize class using Japanese as the language
wscraper = wikiscraper.wikiScraper("ja")

# parse arguments
parser = argparse.ArgumentParser(description='Gets English or Japanese translations of keyword terms from wikipedia')
parser.add_argument('--batch', type=argparse.FileType('r'), help='batch process a list of terms from a file')
parser.add_argument('--out', type=argparse.FileType('w'), help='output the equivalent term and summary as <input term><output term><summary> delimited by tabs')
args = parser.parse_args()
print "Processing file:" + args.batch.name

#read from file
reader = IO.TSVUnicodeReader(open(args.batch.name,"r"))

# get a title,summary for each row from the file
output = []
for row in reader:
    strOriginalStr = row[0];
    print "Scraping:" + strOriginalStr
    candidates = wscraper.searchKw(strOriginalStr)
    if len(candidates) > 0:
        strTitle = wscraper.getPageTitle(candidates[0])
        strSummary= wscraper.getSummary(candidates[0])
    output.append([strOriginalStr,strTitle,strSummary])

#output to TSV file
writer = IO.TSVUnicodeWriter(open(args.out.name,"w"))
writer.writerows(output)

print "Output to file:" + args.out.name
#end of program
