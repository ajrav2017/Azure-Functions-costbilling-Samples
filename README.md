# azure-functions-samples-costbilling
The example shows you how to develop a Python azure function that can extract CostBilling Report from your Azure subscription. This azure function uses Azure Active Directory (AAD) feature to authenticate and authorize the access to the report data.


### Configration changes to add AAD support

- Modify the configuration application settings of AzureWebJobsStorage after deploying your app to Azure. This is necessary if you want to use Azure Data Lake Storage Gen2 (ADLS2) as your storage account.

- The first step is to find the AzureWebJobsStorage setting in your app's configuration blade on the Azure portal. This setting contains the connection string for your storage account. By default, it uses a blob storage account.

- The second step is to change the name of the setting from AzureWebJobsStorage to AzureWebJobsStorage__accountName, where accountName is the name of your ADLS2 storage account. For example, if your ADLS2 storage account name is mystorage, you would change the setting name to AzureWebJobsStorage__accountname.

- The third step is to change the value of the setting from the connection string to just the ADLS2 storage account name. For example, if your ADLS2 storage account name is mystorage, you would change the setting value to mystorage.

- The final step is to save your changes and restart your app. You should now be able to use ADLS2 as your storage account for your app.

- Add system assigned identity using the steps mentioned below.
https://learn.microsoft.com/EN-us/azure/app-service/overview-managed-identity?toc=%2Fazure%2Fazure-functions%2Ftoc.json&tabs=portal%2Chttp#add-a-system-assigned-identity

- Grant the system-assigned identity access to the storage account

## see also
https://learn.microsoft.com/EN-us/azure/azure-functions/functions-identity-based-connections-tutorial#grant-the-system-assigned-identity-access-to-the-storage-account


