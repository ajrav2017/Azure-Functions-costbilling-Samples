import io
import logging
import azure.functions as func
import urllib
import pandas as pd


from azure.mgmt.costmanagement import CostManagementClient
from azure.identity import DefaultAzureCredential, AzureCliCredential
from urlrequest import UrlRequest


def generate_cost_details_report():
    global report_metadata

    #credential = DefaultAzureCredential()
    credential = AzureCliCredential()
    client = CostManagementClient(credential)
    scope = '/subscriptions/' + subscriptionId
    parameters = {}
    parameters['metric'] = 'ActualCost'
    parameters['time_period'] = {"start": startTime, "end": endTime}
    report_metadata = client.generate_cost_details_report.begin_create_operation(scope, parameters=parameters)

def create_report_file():

    for blob in report_metadata.result().blobs:
        cost_details = urllib.request.urlopen(blob.blob_link).read()
        response = UrlRequest(blob.blob_link)

    # report level subscription level or cosmosdb based on meterCategory value
        if  meterCategory == "cosmosdb":
            df = pd.read_csv(io.StringIO(response.text))
            df = df[df['meterCategory'] =='Azure Cosmos DB']
            return df.to_csv(index=False, encoding="utf-8")
        else :
            return response.text
        

def main(req: func.HttpRequest, 
         outputBlob: func.Out[str]) -> None:

    logging.info('Python HTTP trigger function processed a request.')
    global subscriptionId
    global startTime
    global endTime
    global meterCategory

    #biniding variables
    name = req.params.get('name')
    subscriptionId = req.params.get('subscriptionId')
    filename = req.params.get('name')
    startTime = req.params.get('startTime')
    endTime = req.params.get('endTime')
    meterCategory = req.params.get('meterCategory')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')


    logging.info('subscriptionId : %s ' , subscriptionId )
    logging.info('Filename : %s' , filename )
    logging.info('Period Start Time : %s ' , startTime)
    logging.info('Period End Time : %s ' + endTime)
    logging.info('meterCategory : %s ' + meterCategory)

    generate_cost_details_report()
    outputBlob.set(create_report_file())