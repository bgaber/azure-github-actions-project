# Azure Static Website GitHub Actions Project
A Cloud Guru Challenge - https://acloudguru.com/blog/engineering/cloudguruchallenge-your-resume-in-azure

## Azure CLI Resource Group Creation

```powershell
> az group create --name StaticWebsiteRG --location canadacentral
```

## Azure CLI Storage Account Creation

```
> az storage account create --name briangithubactions --resource-group StaticWebsiteRG --location canadacentral --sku Standard_LRS
```

## Azure CLI Blob Static Website Creation

```
> az storage blob service-properties update --account-name briangithubactions --static-website --404-document 404.html --index-document index.html
```

## Azure CLI Create a Content Delivery Network (CDN) profile

```
az cdn profile create --resource-group StaticWebsiteRG --name MyCDNProfile --sku Standard_Microsoft
```

## Azure CLI Create a Content Delivery Network (CDN) endpoint

```
az cdn endpoint create --resource-group StaticWebsiteRG --name "brian-gaber" --profile-name MyCDNProfile --origin briangithubactions.z9.web.core.windows.net --origin-host-header briangithubactions.z9.web.core.windows.net
```

## Azure CLI Purge Content Delivery Network (CDN) endpoint

```
> az cdn endpoint purge --content-paths  "/*" --profile-name MyCDNProfile --name "brian-gaber" --resource-group "StaticWebsiteRG"
```

## Azure CLI Resource Group Deletion

```
> az group delete --name StaticWebsiteRG -y
```