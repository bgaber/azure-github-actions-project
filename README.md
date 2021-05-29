# Azure Static Website GitHub Actions Project
A Cloud Guru Challenge - https://acloudguru.com/blog/engineering/cloudguruchallenge-your-resume-in-azure

Objective
---------
![Alt text](readme_images/resume-challenge.png?raw=true "A Cloud Guru Challenge Objective Diagram")

Solution
--------
![Alt text](readme_images/github-actions-cicd-project.png?raw=true "Azure Static Website GitHub Actions Solution Diagram")

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
> az cdn profile create --resource-group StaticWebsiteRG --name MyCDNProfile --sku Standard_Microsoft
```

## Azure CLI Create a Content Delivery Network (CDN) endpoint

```
> az cdn endpoint create --resource-group StaticWebsiteRG --name brian-gaber --profile-name MyCDNProfile --origin briangithubactions.z9.web.core.windows.net --origin-host-header briangithubactions.z9.web.core.windows.net
```

## Azure CLI Create URL Redirect rule to redirect any HTTP requests to HTTPS

```
> az cdn endpoint rule add --resource-group StaticWebsiteRG --name brian-gaber --profile-name MyCDNProfile --order 1 --rule-name "redirect" --match-variable RequestScheme --operator Equal --match-values HTTP --action-name "UrlRedirect" --redirect-protocol Https --redirect-type Moved
```

### Before you can use a custom domain with an Azure CDN endpoint, you must first create a canonical name (CNAME) record with Azure DNS or your DNS provider to point to your CDN endpoint.
### https://docs.microsoft.com/en-us/azure/cdn/cdn-map-content-to-custom-domain

## Azure CLI Create a custom domain for your endpoint
```
> az cdn custom-domain create --resource-group StaticWebsiteRG --endpoint-name brian-gaber --profile-name MyCDNProfile --name MyCustomDomain --hostname briangaber.esnap.ca

```

## Azure CLI Enable https
```
az cdn custom-domain enable-https --resource-group StaticWebsiteRG --endpoint-name brian-gaber --profile-name MyCDNProfile --name MyCustomDomain
```

### Now the HTML code is uploaded by GitHub Actions by a push to the GitHub repository which will trigger GitHub Actions.

## Azure CLI Purge Content Delivery Network (CDN) endpoint

```
> az cdn endpoint purge --content-paths  "/*" --profile-name MyCDNProfile --name "brian-gaber" --resource-group "StaticWebsiteRG"
```

### Before the Resource Group containing the CDN Profile can be deleted the DNS CNAME record that points to the CDN endpoint must be removed from Azure DNS or your DNS provider

## Azure CLI Resource Group Deletion

```
> az group delete --name StaticWebsiteRG -y
```