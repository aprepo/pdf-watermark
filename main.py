import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja2 environment
template_dir = '.'  # Directory containing watermark.html template
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('watermark.html')

# Example data to populate the template
data = {
    "invoice_date": "October 31, 2024",
    "client_name": "John Doe",
    "client_address": "5678 Lane St.",
    "client_city": "Anytown",
    "client_state": "AN",
    "client_zip": "12345",
    "client_email": "john.doe@example.com",
    "invoice_number": "INV-1001",
    "due_date": "November 30, 2024",
    "items": [
        {"description": "Consulting Service", "quantity": 5, "unit_price": 150.00, "total_price": 750.00},
        {"description": "Software License", "quantity": 1, "unit_price": 300.00, "total_price": 300.00},
        {"description": "Additional Support", "quantity": 2, "unit_price": 100.00, "total_price": 200.00}
    ],
    "subtotal": 1250.00,
    "tax": 125.00,
    "total": 1375.00
}

# Render the HTML with data
html_out = template.render(data)

# Output PDF file path
output_pdf = 'output_invoice.pdf'

# Generate PDF from HTML
pdfkit.from_string(html_out, output_pdf)

print(f"PDF generated successfully: {output_pdf}")
