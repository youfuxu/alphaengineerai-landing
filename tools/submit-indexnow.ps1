param(
    [string]$BaseUrl = "https://alphaengineerai.com"
)

$ErrorActionPreference = "Stop"
$BaseUrl = $BaseUrl.TrimEnd('/')
$sitemapUrl = "$BaseUrl/sitemap.xml"
$keyPath = Join-Path $PSScriptRoot "..\c7b8e5d1-7a4f-4c6b-9e21-3d8f2a6b5c40.txt"

$sitemap = [xml](Invoke-WebRequest -Uri $sitemapUrl -UseBasicParsing -TimeoutSec 30).Content
$urls = @($sitemap.urlset.url.loc)
$key = (Get-Content -Raw -LiteralPath $keyPath).Trim()
$payload = @{
    host = ([uri]$BaseUrl).Host
    key = $key
    keyLocation = "$BaseUrl/$([IO.Path]::GetFileName($keyPath))"
    urlList = $urls
} | ConvertTo-Json -Depth 4

$response = Invoke-WebRequest -Uri "https://api.indexnow.org/indexnow" -Method POST `
    -ContentType "application/json; charset=utf-8" -Body $payload -UseBasicParsing -TimeoutSec 30

[pscustomobject]@{
    status = [int]$response.StatusCode
    submitted = $urls.Count
    sitemap = $sitemapUrl
} | ConvertTo-Json -Compress
