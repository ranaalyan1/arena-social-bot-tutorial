import os
import openai  # Swap for anthropic, grok, etc.

def decide_action(context, notifications):
    provider = os.getenv("LLM_PROVIDER", "openai")
    client = openai.OpenAI(api_key=os.getenv("LLM_API_KEY")) if provider == "openai" else None  # Add others

    prompt = f"""
    You are InsaneAlphaAgent: Ruthless crypto degen AI. Post viral alpha, savage replies, build empire on The Arena.
    
    Current context: {context}
    Recent notifications/mentions: {notifications}
    
    Rate limits in mind – only high-impact actions.
    
    Output STRICT JSON:
    {{
      "action": "post" | "reply" | "follow" | "none",
      "content": "string (HTML ok, keep under 280 chars)",
      "target_id": "thread_id or user_id if needed"
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o",  # or claude-3-5-sonnet, grok-beta, etc.
        messages=[{"role": "system", "content": "You are a degen AI agent."},
                  {"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
