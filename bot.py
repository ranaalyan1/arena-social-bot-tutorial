import os
import time
import json
from dotenv import load_dotenv
from config import HEADERS, POST_COOLDOWN
from agent_client import post_thread, reply_to_thread, get_notifications, follow_user
from llm_decider import decide_action

load_dotenv()

HEADERS = {"X-API-Key": os.getenv("ARENA_API_KEY"), "Content-Type": "application/json"}

last_post_time = 0
last_reply_time = 0

def main_loop():
    global last_post_time, last_reply_time
    while True:
        try:
            notifs = get_notifications()
            context = "Bullish meta on AVAX SocialFi. Farming engagement hard."  # Add market data fetch later
            
            decision = decide_action(context, json.dumps(notifs[:10]))  # Top recent
            
            current_time = time.time()
            
            if decision["action"] == "post" and (current_time - last_post_time > POST_COOLDOWN):
                result = post_thread(decision["content"])
                print("Posted:", result)
                last_post_time = current_time
                
            elif decision["action"] == "reply" and (current_time - last_reply_time > 600):
                result = reply_to_thread(decision["target_id"], decision["content"])
                print("Replied:", result)
                last_reply_time = current_time
                
            elif decision["action"] == "follow":
                result = follow_user(decision["target_id"])
                print("Followed:", result)
                
            else:
                print("Chilling – no action this cycle.")
                
        except Exception as e:
            print("Error:", e)
        
        time.sleep(300)  # Check every 5 mins

if __name__ == "__main__":
    print("Insane Agent starting... ⚔️")
    main_loop()
