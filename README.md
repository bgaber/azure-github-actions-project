# Azure Static Website GitHub Actions Project
A Cloud Guru Challenge - https://acloudguru.com/blog/engineering/cloudguruchallenge-your-resumer-in-azure

## Azure CLI Resource Group Creation

```powershell
> az group create --name static_website_rg --location eastus
```

## Azure CLI Storage Account Creation

```
> az storage account create --name briangithubactions --resource-group static_website_rg --location eastus --sku Standard_LRS
```

## Azure CLI Blob Static Website Creation

```
> az storage blob service-properties update --account-name briangithubactions --static-website --404-document 404.html --index-document index.html
```

## Azure CLI Create a Content Delivery Network (CDN) profile

```
az cdn profile create --resource-group static_website_rg --name MyCDNProfile --sku Standard_Microsoft
```

## Azure CLI Create a Content Delivery Network (CDN) endpoint

```
az cdn endpoint create --resource-group static_website_rg --name "brian-gaber" --profile-name MyCDNProfile --origin briangithubactions.z13.web.core.windows.net
```

## Azure CLI Purge Content Delivery Network (CDN) endpoint

```
> az cdn endpoint purge --content-paths  "/*" --profile-name MyCDNProfile --name "brian-gaber" --resource-group "static_website_rg"
```

## Azure CLI Resource Group Deletion

```
> az group delete --name static_website_rg -y
```