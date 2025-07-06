# CST8919 Lab 3: Azure Login Monitoring with Alerts
## Objective
The objective of this lab was to deploy a Flask login monitoring service to Azure App Service, configure Azure Log Analytics to capture failed login attempts, and create an Azure Monitor alert to automatically notify via email when five or more failed login attempts occur within a five-minute window.
## Video Link: https://youtu.be/RIZgv7LlqLg
## Lab Overview

### 1. Flask Login Monitoring Service
- Created a Flask application with a `/login` POST endpoint that checks user credentials.
- Configured the app to log successful and failed login attempts using Python's `logging` module, ensuring logs are output to `stdout` for Azure to capture.

### 2. Deploying to Azure App Service
- Created an Azure Resource Group and App Service Plan.
- Deployed the Flask application to Azure App Service.
- Verified the app was running by accessing the Azure-hosted URL, confirming it returned:  
  `Flask Login App Lab 3 is Running.`

### 3. Connecting to Log Analytics
- Created a Log Analytics Workspace in Azure.
- Configured the App Service to send `AppServiceConsoleLogs` to Log Analytics.
- Confirmed that failed login attempts were being logged and captured within the workspace.

### 4. Writing the KQL Query
- Wrote the following KQL query to detect failed login attempts:
    ```kql
    AppServiceConsoleLogs
    | where TimeGenerated > ago(5m)
    | where ResultDescription has "Login FAILED"
    | summarize Count = count() by bin(TimeGenerated, 5m)
    | where Count >= 5
    ```
- This query checks for five or more failed login attempts within a five-minute window.

### 5. Configuring Azure Monitor Alerts
- Created an Action Group with my email address to receive notifications.
- Created an Alert Rule in Azure Monitor using the KQL query.
- Set the evaluation period to 5 minutes and frequency to 5 minutes, ensuring alerts trigger promptly when conditions are met.

### 6. Testing and Verification
- Used VS Code REST Client to send multiple failed login requests to the Azure-hosted Flask app.
- Verified that failed login attempts appeared in Log Analytics with the correct timestamp and content.
- Confirmed that the Azure Monitor Alert was triggered after exceeding five failed attempts.
- Verified that an email notification was received, demonstrating the alert system's functionality.

## Technologies Used
- Python Flask for building the login monitoring service.
- Azure App Service for cloud deployment.
- Azure Log Analytics for log collection and querying.
- KQL (Kusto Query Language) for analyzing logs.
- Azure Monitor Alerts for automated notifications.
- VS Code REST Client for testing API endpoints.

## Conclusion
Through this lab, I successfully demonstrated how to deploy a Flask login monitoring service to Azure, capture application logs using Log Analytics, and configure Azure Monitor Alerts to provide proactive notifications when suspicious login activity is detected.
