import os
import google.generativeai as genai
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_pdf_content(text_content):
    """Compiles the full multi-chapter AI text into a multi-page PDF guide."""
    pdf_filename = "product_guide.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                            rightMargin=54, leftMargin=54,
                            topMargin=54, bottomMargin=54)
    
    styles = getSampleStyleSheet()
    normal_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        spaceAfter=10
    )
    
    title_style = ParagraphStyle(
        'TitleCustom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        spaceAfter=5
    )
    
    story = []
    story.append(Paragraph("Your Digital Product Guide", title_style))
    story.append(Paragraph("Generated autonomously by your GitHub Agent for Selar", normal_style))
    story.append(Spacer(1, 10))
    
    # Split the AI text into paragraphs and add them to the document flow
    for paragraph in text_content.split('\n\n'):
        cleaned = paragraph.replace('#', '').strip()
        if cleaned:
            story.append(Paragraph(cleaned, normal_style))
            
    doc.build(story)
    print("Multi-page PDF generated successfully!")

def run():
    model = genai.GenerativeModel("gemini-3.5-flash")
    
    # Strict prompt forcing all chapters to be fully written out
    prompt = """
    Write a complete, comprehensive, multi-chapter mini e-book guide for a digital product store. 
    You must write out every section fully without summarizing or cutting off. 
    Include:
    1. A catchy e-book Title
    2. Introduction
    3. Chapter 1: The Foundation and Niche Research
    4. Chapter 2: The Core Framework and Product Creation
    5. Chapter 3: Launching, Pricing, and Automation
    6. Conclusion and Action Steps
    """
    
    # Requesting a large response size to prevent truncation
    response = model.generate_content(
        prompt,
        generation_config={"max_output_tokens": 8192}
    )
    
    # 1. Save text file
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
        
    # 2. Build the full multi-page PDF
    generate_pdf_content(response.text)
    print("Full product package generated successfully!")

if __name__ == "__main__":
    run()
