## Azure CLI Resource Group Creation

```powershell
> az group create --name rg_static_website --location canadaeast
```

## Azure CLI Storage Account Creation

```
> az storage account create --name bgresumegitactions --resource-group rg_static_website --location canadaeast --sku Standard_LRS
```

## Azure CLI Blob Static Website Creation

```
> az storage blob service-properties update --account-name bgresumegitactions --static-website --404-document 404.html --index-document index.html
```

## Azure CLI Purge Content Delivery Network

```
> az cdn endpoint purge --content-paths  "/*" --profile-name "my-static-website" --name "brian-gaber.azureedge.net" --resource-group "rg_static_website"
```

## Azure CLI Resource Group Deletion

```
> az group delete --name rg_static_website -y
```