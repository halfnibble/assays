import sys, csv

def parse_csv(filename=None):
    try:
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                yield row
    except IOError:
        sys.exit("There was an error reading the file. Nothing was imported.")
    except csv.Error as e:
        sys.exit("There was a CSV file error: {0}".format(e))