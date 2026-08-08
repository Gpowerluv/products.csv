import os
import csv
import requests
import google.generativeai as genai

# --- 1. Load Secrets from GitHub Actions ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINTEREST_ACCESS_TOKEN = os.getenv("PINTEREST_ACCESS_TOKEN")
PINTEREST_BOARD_ID = os.getenv("PINTEREST_BOARD_ID")

# --- 2. Configure AI ---
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_pinterest_copy(product_name):
    """Uses AI to generate an SEO-optimized Pinterest title and description."""
    prompt = f"""
    You are an expert Pinterest marketer. I am giving you a raw Amazon product name.
    Raw Product Name: {product_name}
    
    Task 1: Write a catchy, clickable Pinterest Pin title (under 100 characters).
    Task 2: Write a visually descriptive, SEO-optimized Pinterest description with 3-4 hashtags (under 500 characters).
    
    Format the output exactly like this:
    TITLE: [Your Title Here]
    DESCRIPTION: [Your Description Here]
    """
    
    response = model.generate_content(prompt)
    text = response.text
    
    # Parse the AI response
    title = text.split("TITLE:")[1].split("DESCRIPTION:")[0].strip()
    description = text.split("DESCRIPTION:")[1].strip()
    
    return title, description

def create_pin(title, description, link, image_url):
    """Sends the formatted data to the Pinterest API."""
    url = "https://api.pinterest.com/v5/pins"
    
    headers = {
        "Authorization": f"Bearer {PINTEREST_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "board_id": PINTEREST_BOARD_ID,
        "title": title[:100], # Failsafe length limit
        "description": description[:500],
        "link": link,
        "media_source": {
            "source_type": "image_url",
            "url": image_url
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        print(f"✅ Successfully pinned: {title}")
    else:
        print(f"❌ Failed to pin: {response.text}")

# --- 3. Main Execution Workflow ---
def main():
    print("Starting Pinterest Agent...")
    
    # Read the CSV file
    with open('products.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            raw_name = row['product_name']
            link = row['affiliate_link']
            image_url = row['image_url']
            
            print(f"Processing: {raw_name}...")
            
            # Step A: AI Processing
            title, description = generate_pinterest_copy(raw_name)
            
            # Step B: Pin to Pinterest
            create_pin(title, description, link, image_url)

if __name__ == "__main__":
    main()
