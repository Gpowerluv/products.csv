import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def run():
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = """
    Create a high-demand digital product blueprint for a Selar store. 
    Provide the output clearly separated like this:
    - PRODUCT TITLE:
    - SUGGESTED PRICE (in USD/NGN):
    - SELAR STORE DESCRIPTION (Persuasive sales copy):
    - SOCIAL MEDIA MARKETING CAPTION:
    """
    response = model.generate_content(prompt)
    
    print(response.text)
    
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    run()
