# Azure Functions to Extract Costbilling Data

The azure function is an example to show how to extract costbilling data from Azure subscription. The azure function calls the ***Generate Cost Details Report REST API***, which returns a CSV file with the cost details for a specified time period and scope. You can use this data to analyze your Azure spending and optimize your cloud resources.

This azure function uses Azure Active Directory **(AAD)** feature to authenticate and authorize the access to the report data.


## Create function app settings used 

| **Congiration** | **Value** |
| ---------- | -------- |
| **Runtime Stack** | Python |
| **Version** | 3.10 |
| **Operating System** | Linux |
| **Hosting options and plans** | App Service Plan |




## Configration changes to add AAD support

- Modify the configuration application settings of AzureWebJobsStorage after deploying your app to Azure. This is necessary if you want to use Azure Data Lake Storage Gen2 (ADLS2) as your storage account.

  1. The first step is to find the AzureWebJobsStorage setting in your app's configuration blade on the Azure portal. This setting contains the connection string for your storage account. By default, it uses a blob storage account.

  2. The second step is to change the name of the setting from AzureWebJobsStorage to AzureWebJobsStorage__accountName, where accountName is the name of your ADLS2 storage account. For example, if your ADLS2 storage account name is mystorage, you would change the setting name to AzureWebJobsStorage__accountname.

  3. The third step is to change the value of the setting from the connection string to just the ADLS2 storage account name. For example, if your ADLS2 storage account name is mystorage, you would change the setting value to mystorage.

  4. The final step is to save your changes and restart your app. You should now be able to use ADLS2 as your storage account for your app.

- Adding system identity to function app is important to enable Azure AD support. System identity is a feature of Azure that allows your app to access other Azure services without storing any secrets. You can use system identity to authenticate to Azure SQL, Application Insights, Service Bus and more. To use system identity, you need to enable it in your function app settings and assign the appropriate roles to the identity in the target resources.  [Add system assigned identity]( https://learn.microsoft.com/EN-us/azure/app-service/overview-managed-identity?toc=%2Fazure%2Fazure-functions%2Ftoc.json&tabs=portal%2Chttp#add-a-system-assigned-identity)

- Create a role assignment granting the system-assigned identity access to your storage account [more details]( https://learn.microsoft.com/EN-us/azure/azure-functions/functions-identity-based-connections-tutorial#grant-the-system-assigned-identity-access-to-the-storage-account)

### Function Parameters 
The funciton accepts the following parameters to extract the report data

| **Parameter Name** | **Value** | **Description** |
| ---------- | -------- | -------|
| **name** | filename |Name of a file|
| **subscriptionId** | xxxx-xxxx-xxx-xxxxx |Resource ID for subscription | 
| **startTime** | e.g 2023-04-01T00:00:00 |  Billing Period Start Date|
| **endTime** |  e.g 2023-04-30T00:00:00 |  Billing Period End Date|
| **meterCategory** | cosmosdb,All |Report resource scope|
