import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def run():
    # Use active gemini-2.5-flash model
    model = genai.GenerativeModel("gemini-3.5-flash")
    
    prompt = """
    Create a high-demand digital product blueprint for a Selar store. 
    Provide the output clearly separated like this:
    - PRODUCT TITLE:
    - SUGGESTED PRICE (in USD/NGN):
    - SELAR STORE DESCRIPTION (Persuasive sales copy):
    - SOCIAL MEDIA MARKETING CAPTION:
    - PRODUCT COVER IMAGE PROMPT (Provide a detailed 3D graphic prompt for Canva/Midjourney/Bing to design the product cover):
    """
    
    response = model.generate_content(prompt)
    
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print("Successfully generated product blueprint!")

if __name__ == "__main__":
    run()
