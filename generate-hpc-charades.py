from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black

input_file = "hpc-charades.txt"
output_file = "hpc-charades.pdf"

# Page setup
page_width, page_height = A4

# Layout: 10 per page
cols = 2
rows = 5
phrases_per_page = cols * rows

margin_x = 10 * mm
margin_y = 10 * mm

box_width = (page_width - 2 * margin_x) / cols
box_height = (page_height - 2 * margin_y) / rows

font_name = "Helvetica-Bold"
font_size = 12

def read_hpc_phrases(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def draw_hpc_phrase(c, phrase, x, y):
    c.setLineWidth(1)
    c.rect(x, y, box_width, box_height)

    c.setFont(font_name, font_size)
    c.setFillColor(black)

    c.drawCentredString(
        x + box_width / 2,
        y + box_height / 2,
        phrase
    )

def generate_pdf(phrases):
    c = canvas.Canvas(output_file, pagesize=A4)

    for i, phrase in enumerate(phrases):
        position = i % phrases_per_page
        col = position % cols
        row = position // cols

        x = margin_x + col * box_width
        y = page_height - margin_y - (row + 1) * box_height

        draw_hpc_phrase(c, phrase, x, y)

        # New page after 10 badges
        if position == phrases_per_page - 1:
            c.showPage()

    c.save()

if __name__ == "__main__":
    phrases = read_hpc_phrases(input_file)
    generate_pdf(phrases)
    print(f"Created {output_file} with {len(phrases)} HPC phrases (10 per page).")
