import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def run():
    model = genai.GenerativeModel("gemini-3.5-flash")
    
    # Prompt asking for both copy and an image generation prompt for your product cover
    prompt = """
    Create a high-demand digital product blueprint for a Selar store. 
    Provide the output clearly separated like this:
    - PRODUCT TITLE:
    - SUGGESTED PRICE (in USD/NGN):
    - SELAR STORE DESCRIPTION (Persuasive sales copy):
    - SOCIAL MEDIA MARKETING CAPTION:
    - PRODUCT COVER IMAGE PROMPT (Detailed visual description for an AI image generator to create a professional e-book cover or mockup):
    """
    
    response = model.generate_content(prompt)
    
    # Save the blueprint text including the image prompt
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print("Product blueprint and image concept generated successfully!")

if __name__ == "__main__":
    run()
