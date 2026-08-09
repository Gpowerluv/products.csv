import os
import google.generativeai as genai
from google.generativeai import types
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_pdf_content(text_content):
    """Compiles the full AI text blueprint into a clean, downloadable PDF product file."""
    pdf_filename = "product_guide.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    
    # Title & Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(54, height - 54, "Your Digital Product Guide")
    
    c.setFont("Helvetica", 10)
    c.drawString(54, height - 72, "Generated autonomously by your GitHub Agent for Selar")
    
    # Divider line
    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.line(54, height - 82, width - 54, height - 82)
    
    # Body text formatting (word wrapping line by line)
    c.setFont("Helvetica", 10)
    text_object = c.beginText(54, height - 105)
    text_object.setLeading(14)
    
    for line in text_content.split('\n'):
        clean_line = line.replace('#', '').strip()
        if len(clean_line) > 90:
            chunks = [clean_line[i:i+90] for i in range(0, len(clean_line), 90)]
            for chunk in chunks:
                text_object.textLine(chunk)
        else:
            text_object.textLine(clean_line if clean_line else " ")
            
    c.drawText(text_object)
    c.save()
    print("Full multi-chapter product PDF generated successfully!")

def run():
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=types.GenerationConfig(
            max_output_tokens=4000,  # Forces the model to write a long, complete guide
            temperature=0.7,
        )
    )
    
    prompt = """
    Write a complete, comprehensive mini e-book/guide for a digital product store. 
    You must include:
    1. A catchy e-book Title
    2. An Introduction
    3. Chapter 1: The Foundation
    4. Chapter 2: The Core Framework & Execution
    5. Chapter 3: Launching & Scaling
    6. A Conclusion
    Make sure to write out all chapters fully without cutting off.
    """
    
    response = model.generate_content(prompt)
    
    # 1. Save marketing text file
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
        
    # 2. Build the full multi-chapter PDF file
    generate_pdf_content(response.text)
    print("Product blueprint and full PDF generated successfully!")

if __name__ == "__main__":
    run()
