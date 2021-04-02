# example-flask

[![Build Status](https://dev.azure.com/normuradov0143/normuradov/_apis/build/status/pharrukh.example-flask?branchName=main)](https://dev.azure.com/normuradov0143/normuradov/_build/latest?definitionId=7&branchName=main)

Hybridization between Azure Functions and Flask

## HOWTO

```shell
az functionapp start --name example-flask --resource-group rg-prototyping
az functionapp stop --name example-flask --resource-group rg-prototyping
```

## request example

```shell
curl "https://example-flask.azurewebsites.net/api/Flask?uri=/hello/timur&code={FUNCTION_CODE}"
```