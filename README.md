# konnector
Helper to spin up a konnect instance on Digital Ocean for VPN shenanigans

## Overview
It's a single python script which:
 - spins up a 1-click application from the DigitalOcean Marketplace
 - queries the DigitalOcean API for the IP
 - connects to the new droplet and starts the initial docker container for the konnect instance
 - greps the logfile for the unique authentication token
 - displays the http link and token required for the initial setup via a browser

## Why?
The idea for it was triggered by the need of a fresh public IP, on-the-fly, with the least hassle while at the same using the wireguard client on a macOS system.

This script does not solve any specific issue. It just reduces the amount of manual work to minimum for a new konnect instance.

The creation of the konnect droplet via direct API call was chosen because doctl did not provide the konnect marketplace app as a 1-click action.

## Requirements
You need to have:
 - A [DigitalOcean account (referral link)](https://m.do.co/c/c1ec6dfbd619)
 - A read/write DigitalOcean API token
 - You need the fingerprint of a [valid ssh key](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/to-account/) for your DigitalOcean account
 - You need to have doctl (DigitalOcean Binary) installed on your macOS system. [Check out brew.sh](https://brew.sh) if you don't know how to get doctl!

Ideally the token should be available in your shell environment variables as DO_API_TOKEN. You can use the token directly adding it to line 10 of konnector. The same goes for the ssh key fingerprint. This should be in your shell environment variables as DO_SSH_FINGERPRINT; or hardcoded in line 11 of konnector. Your choice!

Also, if you want to use a non-default ssh key, the path should be in the shell environment variable DO_SSH_KEY or hardcoded in line 12 :)

Example for your .zshrc:
`export DO_SSH_KEY='~/.ssh/do_rsa'`

**Be aware though** -> do not expose the API token to others in any way. I would also recommend to set an expire timeframe for it.
Better safe than sorry!

Happy hacking!
