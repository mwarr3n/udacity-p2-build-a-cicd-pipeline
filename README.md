[![Python application test with Github Actions](https://github.com/mwarr3n/udacity-p2-build-a-cicd-pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/mwarr3n/udacity-p2-build-a-cicd-pipeline/actions/workflows/pythonapp.yml)

# Overview
This project will demonstrate Continuous Integration and Continuous Delivery for a Python-based machine learning application using the Flask web framework. Automated code testing has been implemented using GitHub Actions. An Azure DevOps pipeline has been created to test and deploy to a Azure App Service.

Using this guide you will be able to perform the following:
* Use Azure Cloud Shell to run the application
* Deploy the application as an Azure App Service
* Load test the application using [Locust](https://locust.io/)

<TODO: Architecture diagram here>

The application predicts housing prices in Boston using a pre-trained sklearn model.
```
    Input:
    {
        "CHAS":{
            "0":0
        },
        "RM":{
            "0":6.575
        },
        "TAX":{
            "0":296.0
        },
        "PTRATIO":{
            "0":15.3
        },
        "B":{
            "0":396.9
        },
        "LSTAT":{
            "0":4.98
        }
    }

    result:
    { "prediction": [ 20.35373177134412 ] }
```

## Project Plan

* A link to a Trello board for the project: [Trello Board](https://trello.com/b/FHIB0W1R/project-2-building-a-ci-cd-pipeline)
* A link to a spreadsheet that includes the original and final project plan: [Project Plan]()

# Instructions
## Azure Cloud Shell
Lets deploy the application using Azure Cloud Shell.

Clone the repo in Azure Cloud Shell:
```
git clone git@github.com:mwarr3n/udacity-p2-build-a-cicd-pipeline.git
```
![git-clone.png](img/git-clone.png)

Go to this folder:
```
cd udacity-p2-build-a-cicd-pipeline
```

Create environment:
```
make setup
```

Activate the environment:
```
source ~/.udacity-devops/bin/activate
```

Install dependencies in the virtual environment and run tests:
```
make all
```
Output:
![make-all.png](img/make-all.png)

Start the application:
```
python app.py
```
![app-running.png](img/app-running.png)

Open a new cloud shell and use the following to run the application:
```
cd udacity-p2-build-a-cicd-pipeline
./make_prediction.sh
```

You should see the following output:
![app-prediction.png](img/app-prediction.png)

## Azure App Service
Lets deploy the application using Azure App Services.

Open Azure Cloud Shell and navigate to the cloned project.
```
cd udacity-p2-build-a-cicd-pipeline
```

Deploy the app to Azure App service. The following command deploys the code to a app service called udacity-project2-wa using resource group udacity-project2-rg.
```
az webapp up -n udacity-project2-wa -g udacity-project2-rg --sku F1
```
![app-service.png](img/app-service.png)

![azure-app-service.png](img/azure-app-service.png)


Check state of newly created app service by opening a web browser and navigating to http://udacity-project2-wa.azurewebsites.net.
![app-service-output.png](img/app-service-output.png)

Test the app bexecuting the following command in clous shell. 
Note: Before executing, verify the url on line 28 of make_predict_azure_app.sh matches the url of your app service. 
In clou shell, You can use the following to execute the newly deployed app service:
```
./make_predict_azure_app.sh
```
![app-service-predict.png](img/app-service-predict.png)

You can use the following to view a stream of the deployed apps logs:
```
az webapp log tail -n udacity-project2-wa -g udacity-project2-rg
```
![log-stream.png](img/log-stream.png)



<TODO: 
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment
>


## Load Test
Load test application using locust

Install Locust
```
pip install locust
```

Run app
```
python app.py
```

Open a new terminal and start locust
```
locust
```

Open a browser and go to http://localhost:8089. Enter the total number of users to simulate, spawn rate and set the host to http://localhost:5000.  click Start Swarming to begin load test. See the following image for values used in the test:

![locust-start.png](img/locust-start.png)

Locust Results:
![locust-finished.png](img/locust-finished.png)

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


