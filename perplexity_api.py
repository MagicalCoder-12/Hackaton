# perplexity_api.py
import httpx
import os
import json # Import json for pretty printing

# It's better to move the key retrieval into the function
# to ensure .env has been loaded.
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

async def ask_perplexity(question: str, context: str = "") -> str:
    # --- FIX: Get the API key here ---
    # This ensures load_dotenv() in main.py has already run.
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        # This will raise a clear error if the key is missing.
        raise ValueError("PERPLEX_API_KEY not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    system_prompt = (
        f"You are an expert at extracting factual details from insurance/contract documents. "
        f"Use ONLY information present in this document: {context}. "
        f"If the answer cannot be determined, say 'Not found in document.'"
    )
    payload = {
        "model": "sonar-medium-online",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "max_tokens": 512,
        "temperature": 0.2,
        "stream": False,
    }

    # --- Optional: For debugging, you can uncomment these lines ---
    # print("--- Sending to Perplexity ---")
    # print(f"Headers: {headers}")
    # print(f"Payload: {json.dumps(payload, indent=2)}")
    # print("-----------------------------")

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(PERPLEXITY_API_URL, headers=headers, json=payload)
            response.raise_for_status() # This will raise an error for 4xx or 5xx responses
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        except httpx.HTTPStatusError as e:
            # Log the error response from the server for better debugging
            print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
            print(f"Response body: {e.response.text}")
            raise # Re-raise the exception to be handled by FastAPI
