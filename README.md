# HowGood Application Exercise

This repository contains the code for my HowGood application exercise.

## Application payload

The application data is defined in `apply.py`. The HMAC signing secret is intentionally not stored in this repository. It is read from the local environment variable:

```text
HOWGOOD_SECRET
```

For example, in PowerShell:

```powershell
$env:HOWGOOD_SECRET="<secret provided by HowGood>"
```

## Resume

A PDF copy of my resume is included in the `docs/` directory.

## Live project

Place Picker is a live application that can be used without creating an account:

https://place-picker-production.up.railway.app/

The submission code itself is in this repository and will be completed here.
