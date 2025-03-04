# ✈️ Flight Deal Finder

**Never Overpay for Flights Again!**  
Automatically track flight prices and get instant alerts when deals drop below your target price.

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/Tequila_API-Kiwi.com-success)](https://tequila.kiwi.com/)
[![GMAIL SMTP](https://img.shields.io/badge/Gmail-SMTP-red)](https://developers.google.com/gmail/imap/imap-smtp/)

**Quick Links**  
[Installation](#-installation) • [Configuration](#-configuration) • [Usage](#-usage) • [Troubleshooting](#-troubleshooting)


## 🌟 Key Features
- **Automated Price Tracking**: Scans flights daily using Kiwi's Tequila API
- **Custom Alerts**: SMS via Twilio + Email notifications via Gmail SMTP
- **Google Sheets Integration**: Manage destinations & price thresholds via Sheety API
- **Smart IATA Lookup**: Automatically converts city names to airport codes
- **Flexible Date Range**: Search flights within configurable date windows

## ⚡ Installation

### Prerequisites
- Python 3.10+
- Google Sheet with [Sheety](https://sheety.co/) integration
- [Tequila API Key](https://tequila.kiwi.com/portal/)
- [Twilio Account](https://www.twilio.com/)

1. Clone repository:
```bash
git clone https://github.com/educatedadi/Flight-deal-finder.git
cd flight-deal-finder
