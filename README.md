## Azure CLI Resource Group Creation

```powershell
> az group create --name rg_static_website --location canadaeast
```

az storage account create --name bgresumegitactions --resource-group rg_static_website --location canadaeast --sku Standard_LRS

az storage blob service-properties update --account-name bgresumegitactions --static-website --404-document 404.html --index-document index.html

## Azure CLI Resource Group Deletion

```
> az group delete --name rg_static_website -y
```