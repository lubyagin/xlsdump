import xlrd

def func(filename):
  book = xlrd.open_workbook(filename)
  print book.codepage # Stats
  print book.user_name
  print book.nsheets,",",book.sheet_names()
  sheet = book.sheet_by_index(0)
  nr = sheet.nrows
  nc = sheet.ncols
  for r in xrange(nr):
    for c in xrange(nc):
      print sheet.cell(r,c).value,
    print

import sys
filename = sys.argv[1]
func(filename)
