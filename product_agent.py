import os
import google.generativeai as genai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_pdf_content(text_content):
    """Compiles the AI text blueprint into a clean, downloadable PDF product file."""
    pdf_filename = "product_guide.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    
    # Title & Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(54, height - 54, "Your Digital Product Guide")
    
    c.setFont("Helvetica", 10)
    c.drawString(54, height - 72, "Generated autonomously by your GitHub Agent for Selar")
    
    # Divider line
    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.line(54, height - 85, width - 54, height - 85)
    
    # Body text formatting (word wrapping line by line)
    c.setFont("Helvetica", 11)
    text_object = c.beginText(54, height - 110)
    text_object.setLeading(16)
    
    for line in text_content.split('\n'):
        # Clean up Markdown hash symbols for clean PDF reading
        clean_line = line.replace('#', '').strip()
        if len(clean_line) > 85:
            # Simple chunking for long lines
            chunks = [clean_line[i:i+85] for i in range(0, len(clean_line), 85)]
            for chunk in chunks:
                text_object.textLine(chunk)
        else:
            text_object.textLine(clean_line if clean_line else " ")
            
    c.drawText(text_object)
    c.save()
    print("Downloadable product PDF generated successfully as product_guide.pdf!")

def run():
    model = genai.GenerativeModel("gemini-3.5-flash")
    
    prompt = """
    Create a comprehensive, high-value mini e-book/guide content for a digital product store. 
    Include an introduction, 3 clear actionable chapters/steps on the topic, and a conclusion.
    Keep the language practical and ready to sell.
    """
    
    response = model.generate_content(prompt)
    
    # 1. Save the marketing blueprint text file
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
        
    # 2. Build the actual PDF product file using the generated content
    generate_pdf_content(response.text)
    print("Product blueprint and PDF generated successfully!")

if __name__ == "__main__":
    run()
