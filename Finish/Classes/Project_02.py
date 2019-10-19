# Import modules
import csv


# Create Class
class Data:

  def __init__(self, pathToCSV, delimiter):
    self.pathToCSV = pathToCSV
    self.delimiter = delimiter
    self.file = csv.DictReader(open(pathToCSV))

    # with open(path, 'r') as csvfile:
    #   readCSV = csv.reader(csvfile, delimiter=delimiter)
    #
    #   for row in readCSV:
    #     self.columns = row
    #     row.append(row)
    #     print(row[0], row[1], row[2], )
    #   print(readCSV.line_num)

  def showNames(self):
    pass

  # Change order Function
  def setOrder(self, listOfColumns):
    pass

  # Get number of columns
  def getColumns(self):
    pass

  def showColumn(self, columnName):
    print(type(columnName))
    for x in self.file:
      for col in columnName:
        print(x[col])

  # Show list of columns
  def showRow(self, range):
   pass


path = '/Users/orion/Desktop/Python_Workshop/Finish/Data/Data_Unix.csv'
delimiter = ','
handleCSV = Data(path, delimiter)

handleCSV.showColumn(['first_name', 'last_name'])

# with open(path) as csvfile:
#   readCSV = csv.reader(csvfile, delimiter=delimiter)
#
#   for row in readCSV:
#     print(row)
#     print(row[0])
#     print(row[0], row[1], row[2], )
