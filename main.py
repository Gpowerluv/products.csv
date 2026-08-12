import csv
import os
import random
import uuid
from datetime import datetime

# Path to your products database file
CSV_FILE = "products.csv"

# Define the CSV headers suitable for digital products
HEADERS = [
    "product_id",
    "title",
    "category",
    "price_ngn",
    "description",
    "blueprint_outline",
    "created_at"
]

# Sample data pools for autonomous research & generation
CATEGORIES = [
    "Remote Work & Freelancing",
    "Digital Marketing & Growth",
    "E-commerce & Importation",
    "Content Creation & Monetization",
    "AI Tools & Automation"
]

TITLES_POOL = [
    "The Ultimate Fiverr Freelancing Playbook",
    "Cross-Border Digital Commerce Blueprint",
    "Automated Social Media Monetization Guide",
    "Remote Tech Skills & Global Job Strategy",
    "AI Prompt Engineering for Digital Creators",
    "The High-Converting Digital Storefront Manual",
    "Passive Income Blueprint for Agency Owners"
]

DESCRIPTIONS_POOL = [
    "A step-by-step actionable guide designed to help remote professionals scale their digital services globally.",
    "Comprehensive manual detailing automated systems, payment routing, and international monetization strategies.",
    "Complete breakdown of high-demand digital assets, client acquisition templates, and automated delivery setups.",
    "Practical toolkit equipped with workflows, cheat sheets, and blueprints to build a profitable online operation."
]

OUTLINES_POOL = [
    "Module 1: Market Research | Module 2: Setup & Configuration | Module 3: Client Acquisition | Module 4: Automation",
    "Chapter 1: Foundations | Chapter 2: Asset Creation | Chapter 3: Monetization Funnels | Chapter 4: Scaling",
    "Section A: Tooling & APIs | Section B: Operations Manual | Section C: Growth Hacking | Section D: Maintenance"
]


def initialize_csv():
    """Ensure products.csv exists with proper headers."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
        print(f"Created new database file: {CSV_FILE}")


def generate_product_blueprint():
    """Generate a structured digital product blueprint entry."""
    product_id = f"PROD-{str(uuid.uuid4())[:8].upper()}"
    title = random.choice(TITLES_POOL)
    category = random.choice(CATEGORIES)
    price_ngn = random.choice([3500, 5000, 7500, 10000, 15000])
    description = random.choice(DESCRIPTIONS_POOL)
    blueprint_outline = random.choice(OUTLINES_POOL)
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [
        product_id,
        title,
        category,
        price_ngn,
        description,
        blueprint_outline,
        created_at
    ]


def append_product_to_csv(product_data):
    """Append the newly generated blueprint to products.csv."""
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(product_data)
    
    print(f"Successfully generated product: {product_data[1]} (ID: {product_data[0]})")


def main():
    print("--- Starting Selar Autonomous Product Generator ---")
    initialize_csv()
    
    # Generate new entry
    new_product = generate_product_blueprint()
    append_product_to_csv(new_product)
    
    print("--- Process Completed Successfully ---")


if __name__ == "__main__":
    main()
