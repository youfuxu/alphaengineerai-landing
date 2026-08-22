param(
    [string]$BaseUrl = "https://alphaengineerai.com",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$BaseUrl = $BaseUrl.TrimEnd('/')
$sitemapUrl = "$BaseUrl/sitemap-index.xml"
$keyPath = Join-Path (Join-Path $PSScriptRoot "..") "c7b8e5d1-7a4f-4c6b-9e21-3d8f2a6b5c40.txt"

function Get-SitemapXml {
    param([string]$Uri)

    $lastError = $null
    for ($attempt = 1; $attempt -le 3; $attempt++) {
        try {
            return [xml](Invoke-WebRequest -Uri $Uri -UseBasicParsing -TimeoutSec 30).Content
        } catch {
            $lastError = $_
            if ($attempt -lt 3) {
                Start-Sleep -Seconds 5
            }
        }
    }

    throw "Unable to retrieve sitemap after 3 attempts: $($lastError.Exception.Message)"
}

function Get-SitemapUrls {
    param(
        [string]$Uri,
        [hashtable]$Visited
    )

    if ($Visited.ContainsKey($Uri)) {
        return @()
    }
    $Visited[$Uri] = $true

    $document = Get-SitemapXml -Uri $Uri
    switch ($document.DocumentElement.LocalName) {
        'urlset' {
            $locNodes = @($document.SelectNodes("//*[local-name()='url']/*[local-name()='loc']"))
            if ($locNodes.Count -eq 0) {
                throw "The sitemap did not contain any URL entries: $Uri"
            }
            return @($locNodes | ForEach-Object { $_.InnerText.Trim() })
        }
        'sitemapindex' {
            $childNodes = @($document.SelectNodes("//*[local-name()='sitemap']/*[local-name()='loc']"))
            if ($childNodes.Count -eq 0) {
                throw "The sitemap index did not contain any child sitemaps: $Uri"
            }
            $childUrls = @()
            foreach ($childNode in $childNodes) {
                $childUrls += @(Get-SitemapUrls -Uri $childNode.InnerText.Trim() -Visited $Visited)
            }
            return @($childUrls)
        }
        default {
            throw "Unsupported sitemap document type '$($document.DocumentElement.LocalName)': $Uri"
        }
    }
}

$feedUrl = "$BaseUrl/feed.xml"
$blogFeedUrl = "$BaseUrl/blog-feed.xml"
$urls = @(Get-SitemapUrls -Uri $sitemapUrl -Visited @{} | Where-Object { $_ }) + $feedUrl + $blogFeedUrl
$urls = @($urls | Where-Object { $_ } | Sort-Object -Unique)
if ($urls.Count -eq 0) {
    throw "The sitemap index produced no public URLs."
}
$key = (Get-Content -Raw -LiteralPath $keyPath).Trim()
$payload = @{
    host = ([uri]$BaseUrl).Host
    key = $key
    keyLocation = "$BaseUrl/$([IO.Path]::GetFileName($keyPath))"
    urlList = $urls
} | ConvertTo-Json -Depth 4

if ($DryRun) {
    [pscustomobject]@{
        status = 'dry-run'
        submitted = $urls.Count
        sitemap = $sitemapUrl
    } | ConvertTo-Json -Compress
    return
}

$response = Invoke-WebRequest -Uri "https://api.indexnow.org/indexnow" -Method POST `
    -ContentType "application/json; charset=utf-8" -Body $payload -UseBasicParsing -TimeoutSec 30

[pscustomobject]@{
    status = [int]$response.StatusCode
    submitted = $urls.Count
    sitemap = $sitemapUrl
} | ConvertTo-Json -Compress
