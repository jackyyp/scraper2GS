import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from dataPreprocesser import df
import pprint

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]

#please get the `client_key` from google drive api 

#Authorization
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

sheet = client.open('python2sheet').sheet1

#dont touch this, unexpected error may happen
df = df.fillna('')


#Update to google sheet
sheet.update([df.columns.values.tolist()] + df.values.tolist())


'''
#Some simple function you may use
#note that all index follow google sheet's   

#read record using built-in pretty print function
#python_sheet = sheet.get_all_records()
#pp = pprint.PrettyPrinter()
#pp.pprint(python_sheet)


#fetch row 
row = sheet.row_values(3)
print('\nFetched Row')
pp.pprint(row)


#fetch col
col = sheet.col_values(3)
print('\nFetched col')
pp.pprint(col)

#Update cell.
sheet.update_cell(3,3,'N')

#Insert Row
row = ['a','b','9']
index = 8
sheet.insert_row(row,index)
'''




