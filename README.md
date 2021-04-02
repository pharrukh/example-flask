# example-flask

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