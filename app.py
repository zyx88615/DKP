from __future__ import print_function
import os
from datetime import datetime
from flask import Flask, request,render_template,request,redirect,url_for,after_this_request,make_response,flash,jsonify
from flask import send_from_directory
from functools import wraps
import time
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

import pandas as pd


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'sql','txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv','xlsx','xls'}

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def auth_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth= request.authorization
		if auth and auth.username =="admin" and auth.password== 'admin':
			return f(*args,**kwargs)

		return make_response('Access Denied, Please Request For Access',401, {'WWW-Authenticate':'Basic realm="Login Required'})
	return decorated

@app.route('/')
def my_form():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)



    # If modifying these scopes, delete the file token.json.

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1PmzgBadfqBEzlDH5hBfXqe61z0QPp7VsUoUFV6cD-do'

    

    service = build('sheets', 'v4', credentials=credentials)


    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="DKP!a4:c100").execute()


    df = pd.DataFrame.from_records(result, columns=['values'])
    df2= pd.DataFrame(df["values"].to_list(), columns=['Player', 'Total DKP','Class'])
    df2["Total DKP"] = pd.to_numeric(df2["Total DKP"])
    df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)

    return render_template("index.html" , column_names=df2.columns.values, row_data=list(df2.values.tolist()),
                           link_column="Player", zip=zip)
@app.route("/", methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        
        SERVICE_ACCOUNT_FILE = 'key.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = None
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)



        # If modifying these scopes, delete the file token.json.

        # The ID and range of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = '1PmzgBadfqBEzlDH5hBfXqe61z0QPp7VsUoUFV6cD-do'

        

        service = build('sheets', 'v4', credentials=credentials)


        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="DKP!a4:c100").execute()


        df = pd.DataFrame.from_records(result, columns=['values'])
        df2= pd.DataFrame(df["values"].to_list(), columns=['Player', 'Total DKP','Class'])
        df2["Total DKP"] = pd.to_numeric(df2["Total DKP"])
        df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)

                
        if request.form['submit_button'] == 'Submit':
            playerclass = request.form['kts and kas']
            if playerclass == 'All':
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)
            elif playerclass == 'WarriorRogueT3':
                df2 = df2[(df2['Class'] == 'Warrior')|(df2['Class'] == 'Rogue') ]
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)
            elif playerclass == 'PaladinDruidHunterT3':
                df2 = df2[(df2['Class'] == 'Paladin')|(df2['Class'] == 'Hunter') |(df2['Class'] == 'Druid')]
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)
            elif playerclass == 'MageWarlockPriestT3':
                df2 = df2[(df2['Class'] == 'Mage')|(df2['Class'] == 'Warlock') |(df2['Class'] == 'Priest')]
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)
            elif playerclass == 'Healer Competition':
                df2 = df2[(df2['Class'] == 'Druid')|(df2['Class'] == 'Paladin') |(df2['Class'] == 'Priest')]
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)   
            elif playerclass == 'Caster DPS Competition':
                df2 = df2[(df2['Class'] == 'Mage')|(df2['Class'] == 'Warlock') ]
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)
            else:    
                df2 = df2[(df2['Class'] == playerclass)]
                df2=df2.sort_values(by=['Total DKP','Player'], ascending=False)
       
            
        return render_template("index.html" , column_names=df2.columns.values, row_data=list(df2.values.tolist()),
                           link_column="Player", zip=zip)

    """Return the homepage."""
 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS






@app.route('/delete', methods=['POST', 'GET'])
@auth_required
def html_table():
    df = pd.DataFrame({'Patient Name': ["Some name", "Another name"],
                       "Patient ID": [123, 456],
                       "Misc Data Point": [8, 53]})

    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)



    # If modifying these scopes, delete the file token.json.

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1PmzgBadfqBEzlDH5hBfXqe61z0QPp7VsUoUFV6cD-do'

    

    service = build('sheets', 'v4', credentials=credentials)


    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="DKP!a4:c100").execute()


    df = pd.DataFrame.from_records(result, columns=['values'])
    df2= pd.DataFrame(df["values"].to_list(), columns=['Player', 'Total DKP','Class'])
    df2["Total DKP"] = pd.to_numeric(df2["Total DKP"])


    dfmain = df2

    df = pd.DataFrame({'Patient Name': ["Some name", "Another name"],
                       "Patient ID": [123, 456],
                       "Misc Data Point": [8, 53]})
    return render_template("delete.html" , column_names=df.columns.values, row_data=list(df.values.tolist())
                            )

# @app.route('/static/uploads/<file1>')
# def uploaded_file3(file1):
# #delete file after finish DL
    

#     # @after_this_request 
#     # def remove_file(response): 
#     #     if os.path.exists('static/uploads/'+file1):
#     #           os.remove('static/uploads/'+file1)
#     #     return response 

#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)   
    
#     return render_template("index.html")


@app.route('/static/uploads/<filename>')
def uploaded_file4(filename):
# delete file after finish DL

    @after_this_request 
    def remove_file(response): 
        if os.path.exists('static/uploads/'+filename):
            os.remove('static/uploads/'+filename)
        return response 

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)   
    
    return render_template("index.html")


@app.route('/error', methods=['GET', 'POST'])
def upload_file5():
    return render_template("error.html")




if __name__ == '__main__':
    app.run(debug=True) 