from csv_parser import parse_csv

class Processor(object):
    """Class responsible for processing a CSV file, and inserting parsed 
    data into the database."""
    sample_id_col = None
    assays = []
    
    def __init__(self, filename=None):
        self.output = {}
        self.certificate = self.cert_from_filename(filename)
        # Set data properyt to a CSV read generator
        self.data = parse_csv(filename)
        
    def run(self):
        for row in self.data:
            # Use custom logic to map the data, and update self.output
            self.data_mapper(row)
            
        # Modify the DB with self.output
        self.db_update()
        
    def cert_from_filename(self, filename):
        # Remove folder name component
        filename = filename.split('/')[-1]
        # Remove the filetype
        filename = filename.split('.')[0]
        
        return filename
            
    def data_mapper(self, row):
        # Test if we've already mapped sample_id column and assays
        if sample_id_col is None or len(assays) == 0:
            for item in row:
                # Regular express method to match key terms for either a sample
                # column, or an assays column.
                # Then save matches to a dictionary
            
        pass
        
    def db_update(self):
        pass
    
