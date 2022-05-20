# When to use which package
# Excel File Format     Read          Write                   Edit
# xlsx                  OpenPyXL      OpenPyXL, XlsxWriter    OpenPyXL
# xlsm                  OpenPyXL      OpenPyXL, XlsxWriter    OpenPyXL
# xltx, xltm            OpenPyXL      OpenPyXL                OpenPyXL
# xlsb                  yxlsb         -                       -
# xls, xlt              xlrd          xlwt                    xlutils

# The engine is the package name in lower case,
# so to write a file with OpenPyXL instead of XlsxWriter (which is the default writer in pandas),
# run the following:
# df.to_excel("filename.xlsx", engine="openpyxl")

#       The excel.py Module: to make switching between packages easier
#               Data type conversion
# Excel representation          Python data type
# Empty                         cell None
# Cell with a date format       datetime.datetime(except for pyxlsb)
# Cell with a boolean           bool
# Cell with an error            str(the error message)
# String                        str
# Float                         float or int

# read function accepts a sheet object from one of the following packages:
# xlrd, OpenPyXL, or pyxlsb
# optional arguments first_cell and last_cell. They can be provided in either the A1 notation
# or as row-column-tuple with Excel’s one-based indices: (1, 1).

# The write function works similarly: it expects a sheet object from
# xlwt, OpenPyXL, or XlsxWriter along with the values as nested list and an optional first_cell

# import excel
# values = excel.read(sheet_object, first_cell="A1", last_cell=None)
# excel.write(sheet_object, values, first_cell="A1")
