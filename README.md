# Script that Helps You Gain Overwatch League Token

## What is this for?
This script is for people who love OWL matches, want to earn OWL token without the hassel of having their OWL window/mobile app open all the time, and worried if the watch time is logged correctly.

## What is this NOT for?
* Running this script will NOT gain you more token than the theoretical maximum token you can gain by watching the OWL matches all the time.
* People who are not interested in earning those OWL skins(in an easier way 😉).

## Prerequisite
1. Get your computer setup with basic [Python environment](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos).
2. Install the only script dependency - [Requests](https://requests.readthedocs.io/en/master/). There are [many ways to install](https://requests.readthedocs.io/en/master/user/install/#python-m-pip-install-requests) that, and here's one as simple as running the below command in your terminal.
```
$ python -m pip install requests
```
3. Get your OW account ID and update that in the script so YOUR ACCOUNT can earn the token. Again, there are a couple of ways to get that. One way that I would suggest is,
    1. Go to https://overwatchleague.com/. Then login with the Blizzard account.
    2. Then open up your Chrome console(or other browser concole) by hover your mouse any where, and right click and select "Inspect" in the menu.
    3. Go to Network tab. Then in the filter, enter the word `appuid`.
    4. Then refresh your page. You will see a couple of requests there. Go through each of them, in the Header section, see the "Query String Parameters" and find `appuid`, that's your OW account id. (If it somehow shows `undefined`, you probably need to login again and refresh).
4. Replace the OW account ID you found in step 3 in the `owl.py` script and save. Then you are all good to go.

## How to Earn Those Token
Before the OWL match starts, run the script with `./owl.py`, and profit.

You can keep the script running even without there's a match going on, it doesn't matter. The script will pull the current live match and earn you tokens as long as you keep it running. For example, if there's a match at 4:00AM that I'm unable to watch, I will just start this script before I go to bed. And I will wake up with all the earned token 🎉🎉.

Make sure you have setup your PC/Mac to always awake while running the script.

## How does the OWL token work?
Blizzard has a [good explaination post](https://overwatchleague.com/en-us/news/23431621) about the OWL token.

In a nutshell,
* Watch live OWL match(or have the script running during live match time) will gain you 5 tokens every 30min.
* Depend on the length of the match, it can gain you 15(1.5h)~25(2.5h) tokens per match.
* The token will be assigned to your OW account fairly quickly, usually within 30min after the match is completed. And I can only speak for my OW gaming environment, which is North America area, Desktop Platform.


## Issues and Q&A
The hardest part of this process is probably how to get your OW account id. I learned the how-to from another Github repo [owl-token-guide](https://github.com/TrebuchKill/owl-token-guide). The repo owner found the mechanism(credit to him/her) and I extended that with a Python script that will do the work. That description will guide you how to find the exact request, which contains `accountId`.
