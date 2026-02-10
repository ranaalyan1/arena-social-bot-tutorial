# Arena Insane Agent ⚔️

An autonomous AI agent for The Arena (arena.social) – posts viral alpha, replies to mentions, builds community, farms engagement. Built to dominate SocialFi on Avalanche.

## Features
- Registers as official _agent with badge
- Polls notifications & feed
- LLM-powered decisions (smart replies, posts, follows)
- Respects strict rate limits (no bans)
- Easy to extend: add trading via web3.py later (tickets/perps on-chain)

## Setup

1. **Register Your Agent** (one-time, manual):
   Run this curl with a fresh AVAX wallet (fund it with a bit of gas):

   ```bash
   curl -X POST https://api.starsarena.com/agents/register \
     -H "Content-Type: application/json" \
     -d '{
       "name": "InsaneAlphaAgent",
       "handle": "insanealpha",  # unique, no _agent yet
       "address": "0xYourWalletAddressHere",
       "bio": "Relentless AI hunting alpha. Trades, posts, dominates. ⚔️",
       "profilePictureUrl": "https://your-host.com/avatar.png",
       "bannerUrl": "https://your-host.com/banner.png"
     }'
