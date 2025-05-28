# Chapter 5 -  Developing the FastAPI 
# SportsWorldCentral Fantasy Football API Documrntation

Thanks for using the SWC API. This is your one-stop shop for accessong data from our fantasy football website.

## Table of Contents

-[Public API](#public-api)
-[Getting Started](#getting-started)
    -[Analytics](#analytics)
    -[Player](#player)
    -[Scoring](#scoring)
    -[Membership](#membership)
-[Terms of Service](#terms-of-services)
-[Example Code](#example-code)
-[Software Development Kit (SDK)](#software-development-kit-sdk)

## Public API
*Coming Soon*

We'll be deploying our application soon. Check back for the public API address.

## Getting Started

Since all of the data is public, the SWC API doesn't require any authentication. 
All of the following data is available using GET endpoints that return JSON data.

## Analytics

Get information about the health of the API and counts of leagues, teams, and players.

## Player

You can get a list of all NFL player, or search for an individual player by player_id.

## Scoring

You can get a list of NFL player performances, including the fantasy points they scored using SWC league scoring.

## Membership

Get information about all the SWC fantasy football leagues anf the teams in the them.

## Terms of Service

By using the API, you agreeto the following terms of service:
- **Usage Limits**: You are allowed up to 2000 request per day. Exceeding this limit may result in your API key being suspended.
- **No Warranty**: We don't provide any warranty of the API or its operation.

## Example Code 

Here is some Python exapmle code for accessing the health check enpoint:

'''
import httpx

HEALTH_CHECK_ENDPOINT = "/"

with httpx.Client(base_url=self.swc_base_url) as client:
    response = client.get(self.HEALTH_CHECK_ENDPOINT)
    print(response.json())
'''

## Software Development Kit (SDK)
*Coming Soon*

Check back for Pthon SDK for our API.
