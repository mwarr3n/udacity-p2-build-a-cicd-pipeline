[![Python application test with Github Actions](https://github.com/mwarr3n/udacity-p2-build-a-cicd-pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/mwarr3n/udacity-p2-build-a-cicd-pipeline/actions/workflows/pythonapp.yml)

# Overview

<TODO: complete this with an overview of your project>

This project contains a python application which predicts housing prices in Boston. Using this guide you will be able to perform the following:
* Use Azure cloud shell to run the application
* Deploy the app as an Azure App Service
* Load test the application using [Locust](https://locust.io/)

## Project Plan

* A link to a Trello board for the project: [Trello Board](https://trello.com/b/FHIB0W1R/project-2-building-a-ci-cd-pipeline)
* A link to a spreadsheet that includes the original and final project plan: [Project Plan]()

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

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


