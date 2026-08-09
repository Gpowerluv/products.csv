import os
from google import genai
from google.genai import types

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def run():
    # 1. Generate the product text blueprint using Flash
    text_model_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Create a high-demand digital product blueprint for a Selar store including a Product Title, Suggested Price, Store Description, and Social Media Caption."
    )
    
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(text_model_response.text)
    print("Product text blueprint saved!")

    # 2. Generate the actual product image using the image generation model
    image_prompt = "A professional, eye-catching 3D digital product mockup cover for an online masterclass and e-book bundle, modern aesthetic, high contrast, clean typography layout."
    
    try:
        image_response = client.models.generate_content(
            model='gemini-2.5-flash-image',
            contents=image_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio="1:1")
            ),
        )
        
        # Save the generated image to your repo folder
        for part in image_response.parts:
            if part.inline_data:
                image_bytes = part.as_image()
                image_bytes.save("product_cover.png")
                print("Product cover image saved successfully as product_cover.png!")
                break
    except Exception as e:
        print(f"Image generation skipped or failed: {e}")

if __name__ == "__main__":
    run()
