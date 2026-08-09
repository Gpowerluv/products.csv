import os
import datetime
import html
import google.generativeai as genai
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def run():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    archive_dir = f"archive/product_{timestamp}"
    os.makedirs(archive_dir, exist_ok=True)

    model = genai.GenerativeModel("gemini-3.5-flash")
    
    prompt = """
    Write a complete, comprehensive, multi-chapter mini e-book guide for a digital product store. 
    You must write out every section fully without cutting off. 
    Include:
    1. A catchy e-book Title
    2. Introduction
    3. Chapter 1: The Foundation and Niche Research
    4. Chapter 2: The Core Framework and Product Creation
    5. Chapter 3: Launching, Pricing, and Automation
    6. Conclusion and Action Steps
    
    [MARKETING_SECTION]
    7. SELAR STORE DESCRIPTION (Persuasive sales copy for your landing page)
    8. SUGGESTED PRICE (In USD / NGN)
    9. PRODUCT COVER IMAGE PROMPT (Provide a detailed, professional 3D visual design prompt that can be pasted into an AI image generator to create an eye-catching store cover graphic)
    """
    
    response = model.generate_content(
        prompt,
        generation_config={"max_output_tokens": 8192}
    )
    
    full_text = response.text
    
    # Save full text with marketing metadata for Selar
    with open("generated_product_idea.txt", "w", encoding="utf-8") as f:
        f.write(full_text)
        
    with open(f"{archive_dir}/product_idea.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    # Slice out only the e-book content
    if "[MARKETING_SECTION]" in full_text:
        ebook_content = full_text.split("[MARKETING_SECTION]")[0]
    else:
        ebook_content = full_text

    # Build the PDF cleanly without headers or bot metadata
    pdf_filenames = ["product_guide.pdf", f"{archive_dir}/product_guide.pdf"]
    
    for pdf_filename in pdf_filenames:
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
        
        story = []
        
        for paragraph in ebook_content.split('\n\n'):
            cleaned = paragraph.replace('#', '').strip()
            if cleaned:
                safe_text = html.escape(cleaned)
                story.append(Paragraph(safe_text, normal_style))
                
        doc.build(story)

    print(f"Clean product PDF successfully created and archived in {archive_dir}!")

if __name__ == "__main__":
    run()
