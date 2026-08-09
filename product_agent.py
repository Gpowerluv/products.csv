import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def run():
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = "Create a high-demand digital product blueprint for a Selar store, including product title, target audience, contents, and Facebook ad copy."
    response = model.generate_content(prompt)
    
    print(response.text)
    
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    run()
