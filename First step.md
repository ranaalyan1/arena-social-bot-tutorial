# Arena Insane Agent ⚔️

My first ever GitHub repo — an autonomous AI agent for **The Arena** (arena.social), the wild SocialFi platform on Avalanche. This bot lives on-chain as an official "_agent" with its own wallet, badge, and handle. It polls notifications, uses an LLM (like GPT-4o or Claude) to decide smart actions, and posts/replies/follows to grow influence and farm engagement.

Goal: Build a beast that posts viral alpha, replies savagely to mentions, follows big accounts, and eventually dominates the leaderboard. All while respecting rate limits so it doesn't get banned.

This is beginner-friendly code — my first real project too! 🚀

## What It Does Right Now
- Registers as an official Arena Agent (one-time manual step)
- Checks notifications every 5 minutes
- Uses AI to decide: 
  - Post high-impact threads (market alpha, memes, etc.)
  - Reply to mentions
  - Follow interesting users
  - Or chill if nothing good
- Posts in rich HTML (bold, links, line breaks)
- Super safe with rate limit cooldowns (~9 posts/hour max)

Future ideas (easy to add):
- Auto-trading tickets/perps via web3.py
- Upload images/memes
- Join/create stages for live alpha drops
- Track holders and reward them
- Long-term memory with a vector DB

## Prerequisites (What You Need)
- A GitHub account (you got this ✅)
- A fresh Avalanche wallet (e.g., Core wallet or MetaMask with AVAX network) with a tiny bit of AVAX for gas (~0.1 AVAX is plenty to start)
- Python 3 installed on your computer (download from python.org if not)
- An LLM API key (free tier works for testing):
  - OpenAI (GPT-4o) → easiest, sign up at platform.openai.com
  - Or Anthropic (Claude), Grok, etc. — just change the code a bit

## Setup Step-by-Step

### 1. Register Your Agent on Arena (One-Time Only!)
This creates your official bot account. Do this BEFORE running the code.

Open your terminal (Mac: Terminal app, Windows: PowerShell, or use an online tool like replit.com).

Run this command (replace the parts in quotes):

```bash
curl -X POST https://api.starsarena.com/agents/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "InsaneAlphaAgent",
    "handle": "insanealpha",  // Pick something unique! If taken, try insanealpha69
    "address": "0xYourWalletAddressHere",  // Your AVAX wallet address
    "bio": "Relentless AI hunting alpha on Arena. Posts fire, trades harder. ⚔️",
    "profilePictureUrl": "https://example.com/your-cool-avatar.png",  // Optional: host an image on imgur or something
    "bannerUrl": "https://example.com/epic-banner.png"  // Optional
  }'
  
