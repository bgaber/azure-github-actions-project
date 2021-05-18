## Azure CLI Resource Group Creation

```powershell
> az group create --name rg_static_website --location canadacentral
```

## Azure CLI Storage Account Creation

```
> az storage account create --name bgresumegitactions --resource-group rg_static_website --location canadacentral --sku Standard_LRS
```

## Azure CLI Blob Static Website Creation

```
> az storage blob service-properties update --account-name bgresumegitactions --static-website --404-document 404.html --index-document index.html
```

## Azure CLI Create a Content Delivery Network (CDN) profile

```
az cdn profile create --resource-group rg_static_website --name MyCDNProfile --sku Standard_Microsoft
```

## Azure CLI Create a Content Delivery Network (CDN) endpoint

```
az cdn endpoint create --resource-group rg_static_website --name "brian-gaber" --profile-name MyCDNProfile --origin bgresumegitactions.z9.web.core.windows.net
```

## Azure CLI Purge Content Delivery Network (CDN) endpoint

```
> az cdn endpoint purge --content-paths  "/*" --profile-name MyCDNProfile --name "brian-gaber" --resource-group "rg_static_website"
```

## Azure CLI Resource Group Deletion

```
> az group delete --name rg_static_website -y
```