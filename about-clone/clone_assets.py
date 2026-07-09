#!/usr/bin/env python3
"""
Clone wellbeing-support page assets and rewrite paths to use local copies.
Only downloads actual asset files, not HTML/JSON endpoints.
Reuses assets from homepage-clone where filenames match.
"""

import os
import re
import sys
from urllib.parse import urlparse, urlunparse
from pathlib import Path
import subprocess
import hashlib
import shutil

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

BASE_DIR = Path("/Users/paulbridges/Desktop/fbbb/wellbeing-support-clone")
ASSETS_DIR = BASE_DIR / "assets"
HTML_FILE = BASE_DIR / "index.html"
HOMEPAGE_ASSETS_DIR = Path("/Users/paulbridges/Desktop/fbbb/homepage-clone/assets")

# Domain for this site
SITE_DOMAIN = "licensedtradecharity.org.uk"

# Third-party domains that should stay remote
REMOTE_DOMAINS = {
    "instagram.com",
    "cdninstagram.com",
    "facebook.com",
    "google-analytics.com",
    "googletagmanager.com",
    "doubleclick.net",
    "cookiebar.devstars.com",
}

# Asset file extensions - only download these
ASSET_EXTENSIONS = {
    # Images
    ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico", ".avif",
    # JavaScript
    ".js",
    # CSS
    ".css",
    # Fonts
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    # Video
    ".mp4", ".webm", ".ogg",
    # Documents
    ".pdf",
}

# Create asset directories
for asset_type in ["css", "js", "fonts", "img", "video"]:
    (ASSETS_DIR / asset_type).mkdir(parents=True, exist_ok=True)

def should_keep_remote(url):
    """Check if URL should remain remote (third-party)."""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # Check if any remote domain is a substring
    for remote_domain in REMOTE_DOMAINS:
        if remote_domain in domain:
            return True

    # Check if it's Google Fonts
    if "fonts.googleapis.com" in domain or "fonts.gstatic.com" in domain:
        return True

    return False

def get_asset_type(url):
    """Determine asset type from URL."""
    parsed = urlparse(url)
    path = parsed.path.lower()

    if ".css" in path:
        return "css"
    elif ".js" in path:
        return "js"
    elif any(ext in path for ext in [".woff", ".woff2", ".ttf", ".eot", ".otf"]):
        return "fonts"
    elif any(ext in path for ext in [".mp4", ".webm", ".ogg"]):
        return "video"
    else:
        return "img"  # default for images

def generate_local_filename(url):
    """Generate a local filename for a URL."""
    parsed = urlparse(url)
    path = parsed.path

    # Remove query string for filename
    filename = path.split("/")[-1].split("?")[0]

    # If no extension or extension not recognized, look for extension in path
    if not "." in filename or not any(filename.lower().endswith(ext) for ext in ASSET_EXTENSIONS):
        # Look for extension in path
        for part in reversed(path.split("/")):
            if any(part.lower().endswith(ext) for ext in ASSET_EXTENSIONS):
                filename = part.split("?")[0]
                break
        else:
            # Use hash as fallback
            filename = f"asset-{hashlib.md5(url.encode()).hexdigest()[:8]}"

    return filename

def is_asset_url(url):
    """Check if URL is an actual asset file (not HTML/JSON endpoint)."""
    parsed = urlparse(url)
    path = parsed.path.lower()

    # Must have an asset extension
    if not any(path.endswith(ext) for ext in ASSET_EXTENSIONS):
        return False

    # Skip common non-asset paths
    skip_paths = ["wp-json", "xmlrpc", "embed", "oembed"]
    if any(skip in path for skip in skip_paths):
        return False

    return True

def copy_from_homepage(asset_type, filename):
    """Copy asset from homepage-clone if it exists there."""
    src_path = HOMEPAGE_ASSETS_DIR / asset_type / filename
    if src_path.exists():
        dest_path = ASSETS_DIR / asset_type / filename
        shutil.copy2(src_path, dest_path)
        return True
    return False

def download_asset(url, local_path):
    """Download a single asset using curl."""
    try:
        subprocess.run([
            "curl", "-s", "-A", USER_AGENT, "-o", str(local_path), url
        ], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Read HTML
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Find all asset URLs
    assets = []

    # Pattern to find URLs in src, href, data-src attributes
    patterns = [
        r'(src|href|data-src)="([^"]+)"',
        r'(data-srcset)="([^"]+)"',  # srcset can have multiple URLs
    ]

    for pattern in patterns:
        matches = re.findall(pattern, html)
        for attr, url in matches:
            # Skip empty, mailto, tel, anchor links
            if not url or url.startswith(("#", "mailto:", "tel:", "data:")):
                continue

            # Parse URL
            parsed = urlparse(url)

            # Skip if already relative
            if not parsed.netloc and parsed.path.startswith("/"):
                continue

            # Skip if should stay remote
            if should_keep_remote(url):
                continue

            # Only process actual asset files (not HTML pages, JSON endpoints, etc.)
            if not is_asset_url(url):
                continue

            # Only process assets from the target domain
            if SITE_DOMAIN not in parsed.netloc.lower():
                continue

            asset_type = get_asset_type(url)
            local_filename = generate_local_filename(url)
            local_path = ASSETS_DIR / asset_type / local_filename

            assets.append({
                "original_url": url,
                "local_path": local_path,
                "asset_type": asset_type,
                "local_url": f"assets/{asset_type}/{local_filename}",
                "attr": attr,
            })

    # Download/copy all unique assets
    downloaded = set()
    reused_from_homepage = 0
    downloaded_new = 0

    for asset in assets:
        if asset["original_url"] in downloaded:
            continue

        local_path = asset["local_path"]
        if local_path.exists():
            print(f"✓ Already exists: {local_path.name}")
            downloaded.add(asset["original_url"])
            continue

        # Try to copy from homepage-clone first
        if copy_from_homepage(asset["asset_type"], local_path.name):
            print(f"✓ Reused from homepage-clone: {local_path.name}")
            downloaded.add(asset["original_url"])
            reused_from_homepage += 1
            continue

        print(f"Downloading: {asset['original_url']}")
        success = download_asset(asset["original_url"], local_path)
        if success:
            print(f"  ✓ Saved to: {local_path}")
            downloaded.add(asset["original_url"])
            downloaded_new += 1
        else:
            print(f"  ✗ Failed: {asset['original_url']}")

    # Rewrite HTML with local paths
    rewritten_html = html
    replacements_made = 0

    for asset in assets:
        # Only replace if we successfully downloaded it
        if asset["local_path"].exists():
            old_pattern = f'{asset["attr"]}="{asset["original_url"]}"'
            new_pattern = f'{asset["attr"]}="{asset["local_url"]}"'
            rewritten_html = rewritten_html.replace(old_pattern, new_pattern)
            replacements_made += 1

    # Remove WordPress admin bar if present
    rewritten_html = re.sub(
        r'<div[^>]*id="wpadminbar"[^>]*>.*?</div>',
        "",
        rewritten_html,
        flags=re.DOTALL
    )

    # Remove WordPress admin scripts
    rewritten_html = re.sub(
        r'<script[^>]*src="[^"]*wp-admin[^"]*"[^>]*></script>',
        "",
        rewritten_html
    )

    # Remove REST API links that won't work locally
    rewritten_html = re.sub(
        r'<link[^>]*rel="https://api\.w\.org/"[^>]*/>',
        "",
        rewritten_html
    )

    # Remove oEmbed links that won't work locally
    rewritten_html = re.sub(
        r'<link[^>]*rel="alternate"[^>]*type="application/json\+oembed"[^>]*/>',
        "",
        rewritten_html
    )

    # Write rewritten HTML
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(rewritten_html)

    print(f"\n✓ Clone complete!")
    print(f"  - Reused from homepage-clone: {reused_from_homepage}")
    print(f"  - Downloaded new: {downloaded_new}")
    print(f"  - Total assets: {len(downloaded)}")
    print(f"  - Made {replacements_made} path replacements")
    print(f"  - Rewritten: {HTML_FILE}")

if __name__ == "__main__":
    main()
