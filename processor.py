import re
from csv_parser import parse_csv

class Processor(object):
    """Class responsible for processing a CSV file, and inserting parsed 
    data into the database."""
    sample_id_column = None
    assay_columns = []
    element_row = None
    method_row = None
    unit_row = None
    data_start_row = None
    # Contain an array of objects
    # { 'column': <col>, 'element': <elem>, 'method': <meth>, 'units': <unit>}
    assays = []
    
    elements = ['Au', 'Pt', 'Pd',]
    units = ['ppb', ] # Add rest of units.
    
    def __init__(self, filename=None):
        self.output = {}
        self.certificate = self.cert_from_filename(filename)
        # Set data properyt to a CSV read generator
        self.data = parse_csv(filename)
        
    def run(self):
        # Use custom logic to map the data, and update self.output
        map_status = self.data_mapper(self.data)
        
        # Loop through data and then..
            
        # Modify the DB with self.output
        self.db_update()
        
    def cert_from_filename(self, filename):
        # Remove folder name component
        filename = filename.split('/')[-1]
        # Remove the filetype
        filename = filename.split('.')[0]
        
        return filename
            
    def data_mapper(self, data):
        # Loop through and create data map
        for row_index, row in enumerate(data):
            # Test if each value is set, and if not, test for it.
            if self.sample_id_column is None:
                # Create Regex
                pattern = re.compile('Sample', re.IGNORECASE)
                for column_index, column in enumerate(row):
                    if pattern.match(str(column)) is not None:
                        self.sample_id_column = column_index
                        print 'sample_id_column =', column_index
            if len(self.assay_columns) == 0:
                for column_index, column in enumerate(row):
                    if str(column) in self.elements:
                        self.assay_columns.append(column_index)
                        if self.element_row is None:
                            self.element_row = row_index
                print 'assay_columns =', self.assay_columns
                print 'element_row =', self.element_row
            
                              
                    
            
            
        pass
        
    def db_update(self):
        pass
    
