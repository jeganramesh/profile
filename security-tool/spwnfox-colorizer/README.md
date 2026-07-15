# 🦊 PwnFox Colorizer - Burp Suite Extension

> A powerful Python-based Burp Suite extension that color-codes HTTP requests for efficient bug bounty hunting and security testing.

## 📋 Overview

**PwnFox Colorizer** is a Burp Suite extension designed to streamline your security testing workflow. It automatically colorizes HTTP requests in the Proxy history based on custom headers, making it easier to identify patterns, track IDOR vulnerabilities, and organize complex request flows.

Perfect for bug bounty hunters and penetration testers who need to quickly categorize and identify suspicious requests.

## ✨ Features

- 🎨 **Automatic Color-Coding** - Colorizes requests based on custom `X-PwnFox-Color` headers
- 🔍 **IDOR Detection** - Easily spot potential Insecure Direct Object Reference vulnerabilities
- ⚡ **Real-time Processing** - Analyzes requests as they flow through the proxy
- 📊 **Request Organization** - Color-coded comments for better request tracking
- 🎯 **Bug Bounty Optimized** - Built specifically for security researchers and hunters
- 💻 **Community Edition Compatible** - Works with Burp Suite Community Edition

## 🛠️ How It Works

The extension monitors all HTTP requests passing through Burp Suite's Proxy. When it detects a request with a custom `X-PwnFox-Color` header, it:

1. Extracts the color value from the header
2. Applies the color highlight to the request in Proxy history
3. Adds a comment tag (e.g., `[RED]`, `[GREEN]`) for quick identification

This allows you to visually organize your testing workflow and quickly spot important requests.

## 📥 Installation

### Prerequisites
- Burp Suite Community Edition (or Professional)
- Python (Jython for Burp)
- Basic understanding of Burp Suite extensions

### Setup Steps

1. **Download the script**
```bash
   git clone https://github.com/yourusername/pwnfox-colorizer.git
   cd pwnfox-colorizer
```

2. **Open Burp Suite**
   - Go to `Extensions` → `Installed` → `Add`
   - Select `Extension type: Python`
   - Choose `pwnfox-colorizer.py`
   - Click `Next` to load the extension

3. **Verify Installation**
   - Check the `Extension Output` tab for: `"PwnFox Colorizer loaded"`
   - Extension is now active!

4. **Start Using**
   - Configure your requests with `X-PwnFox-Color` headers
   - Watch requests get color-coded in real-time

## 💡 Usage Examples

### Adding Color Headers

In your testing workflow, you can add custom headers to categorize requests:

```http
GET /api/user/profile HTTP/1.1
Host: target.com
X-PwnFox-Color: red
```

**Supported Colors:**
- `red` - High priority / Critical findings
- `orange` - Medium priority
- `yellow` - Low priority
- `green` - Safe requests
- `blue` - Authentication-related
- `cyan` - Information gathering
- `magenta` - Suspicious activity

### Real-World Scenario

Testing for IDOR vulnerabilities:

```http
GET /api/users/123/data HTTP/1.1
X-PwnFox-Color: red  # Potential IDOR

GET /api/users/124/data HTTP/1.1
X-PwnFox-Color: red  # Testing parameter variation

GET /api/users/admin/data HTTP/1.1
X-PwnFox-Color: orange  # Higher risk target
```

All requests appear color-coded in your Proxy history for quick analysis!

## 🔧 Code Structure

```python
class BurpExtender(IBurpExtender, IHttpListener):
    - registerExtenderCallbacks()    # Initialize extension
    - processHttpMessage()            # Process incoming/outgoing requests
```

### Key Components

- **IBurpExtender** - Required interface for Burp extensions
- **IHttpListener** - Monitors HTTP traffic
- **analyzeRequest()** - Parses request headers
- **setHighlight()** - Applies color to request
- **setComment()** - Adds identifying comment

## 🎯 Use Cases

### 1. **IDOR (Insecure Direct Object Reference) Testing**
