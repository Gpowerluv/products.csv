import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_profitable_product():
    prompt = """
    Act as an elite e-commerce product researcher and digital marketing expert for Selar stores. 
    Analyze current online trends and select ONE extremely high-demand digital product that sells itself 
    with minimal friction (such as a ready-made social media content bundle, professional resume/CV template pack, 
    or a targeted digital growth toolkit for small businesses and creators).
    
    Provide the output structured precisely as follows:
    
    1. PRODUCT TYPE / NICHE:
    2. PRODUCT TITLE:
    3. WHY THIS SELLS ITSELF (Market Demand & Psychological Trigger):
    4. COMPLETE PRODUCT BLUEPRINT / CONTENTS (What the buyer gets inside):
    5. HIGH-CONVERTING SELAR STORE DESCRIPTION (Persuasive sales copy with clear benefits):
    6. INSTAGRAM & FACEBOOK PROMOTIONAL CAPTION (With strong hooks, emojis, and a clear call-to-action to buy via the store link):
    """

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(prompt)
    
    product_blueprint = response.text
    print("--- AUTONOMOUS PRODUCT RESEARCH & CREATION COMPLETE ---")
    print(product_blueprint)

    filename = "generated_product_idea.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(product_blueprint)
    print(f"Successfully saved product blueprint to {filename}")

if __name__ == "__main__":
    generate_profitable_product()
