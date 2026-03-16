from django.shortcuts import render
import random
import string
import qrcode
import base64
from io import BytesIO
from django.http import HttpResponse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfMerger
from django.shortcuts import render, get_object_or_404
from .models import Tool
from django.db.models import F
from django.contrib import messages


from .models import Tool


def home(request):

    query = request.GET.get("q","")

    tools = Tool.objects.all()

    results = []

    if query:
        results = tools.filter(name__icontains=query)

    return render(request,"home.html",{
        "tools":tools,
        "results":results,
        "query":query
    })

def tool_detail(request, slug):

    tool = get_object_or_404(Tool, slug=slug)

    Tool.objects.filter(id=tool.id).update(
        usage_count=F("usage_count") + 1
    )

    tool.refresh_from_db()

    return render(request, "tool_detail.html", {
        "tool": tool
    })


def tool_landing(request, slug):

    tool = get_object_or_404(Tool, slug=slug)

    return render(request, "tool_landing.html", {
        "tool": tool
    })
def word_counter(request):
    text = ""
    words = 0
    characters = 0

    if request.method == "POST":
        text = request.POST.get("text")
        words = len(text.split())
        characters = len(text)

    return render(request, "word_counter.html", {
        "text": text,
        "words": words,
        "characters": characters
    })
    
def password_generator(request):

    password = ""

    if request.method == "POST":
        length = int(request.POST.get("length"))

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))

    return render(request, "password_generator.html", {"password": password})


def qr_generator(request):

    qr_image = None

    if request.method == "POST":
        data = request.POST.get("data")

        qr = qrcode.make(data)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        img_str = base64.b64encode(buffer.getvalue()).decode()

        qr_image = img_str

    return render(request, "qr_generator.html", {"qr_image": qr_image})


def image_to_pdf(request):

    if request.method == "POST":
        image_file = request.FILES.get("image")

        image = Image.open(image_file)

        buffer = BytesIO()

        pdf = canvas.Canvas(buffer)

        width, height = image.size

        image_path = BytesIO()
        image.save(image_path, format="PNG")

        pdf.drawImage(ImageReader(image_path), 0, 0, width, height)

        pdf.showPage()
        pdf.save()

        buffer.seek(0)

        return HttpResponse(buffer, content_type='application/pdf')

    return render(request, "image_to_pdf.html")


def pdf_merge(request):

    if request.method == "POST":

        files = request.FILES.getlist("pdfs")

        merger = PdfMerger()

        for pdf in files:
            merger.append(pdf)

        buffer = BytesIO()
        merger.write(buffer)
        merger.close()

        buffer.seek(0)

        return HttpResponse(buffer, content_type="application/pdf")

    return render(request, "pdf_merge.html")

def text_case_converter(request):

    text = ""
    result = ""

    if request.method == "POST":

        text = request.POST.get("text")
        action = request.POST.get("action")

        if action == "upper":
            result = text.upper()

        elif action == "lower":
            result = text.lower()

        elif action == "title":
            result = text.title()

    return render(request, "text_case.html", {
        "text": text,
        "result": result
    })
    
def random_number(request):

    number = None

    if request.method == "POST":

        min_val = int(request.POST.get("min"))
        max_val = int(request.POST.get("max"))

        number = random.randint(min_val, max_val)

    return render(request, "random_number.html", {"number": number})

def image_compressor(request):

    if request.method == "POST":

        image_file = request.FILES.get("image")

        img = Image.open(image_file)

        buffer = BytesIO()

        img.save(buffer, format="JPEG", quality=30)

        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/jpeg")

    return render(request, "image_compressor.html")

def image_resizer(request):

    if request.method == "POST":

        image_file = request.FILES.get("image")
        width = int(request.POST.get("width"))
        height = int(request.POST.get("height"))

        img = Image.open(image_file)

        resized = img.resize((width, height))

        buffer = BytesIO()

        resized.save(buffer, format="JPEG")

        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/jpeg")

    return render(request, "image_resizer.html")


def jpg_to_png(request):

    if request.method == "POST":

        image_file = request.FILES.get("image")

        img = Image.open(image_file)

        buffer = BytesIO()

        img.save(buffer, format="PNG")

        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/png")

    return render(request, "jpg_to_png.html")

def png_to_jpg(request):

    if request.method == "POST":

        image_file = request.FILES.get("image")

        img = Image.open(image_file).convert("RGB")

        buffer = BytesIO()

        img.save(buffer, format="JPEG")

        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/jpeg")

    return render(request, "png_to_jpg.html")

def remove_spaces(request):

    text = ""
    result = ""

    if request.method == "POST":

        text = request.POST.get("text")

        result = " ".join(text.split())

    return render(request, "remove_spaces.html", {
        "text": text,
        "result": result
    })
    
    
def text_reverser(request):

    text = ""
    result = ""

    if request.method == "POST":

        text = request.POST.get("text")

        result = text[::-1]

    return render(request, "text_reverser.html", {
        "text": text,
        "result": result
    })
    

def about(request):
    return render(request,"about.html")


def privacy_policy(request):
    return render(request,"privacy_policy.html")

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Abhi simple message show karenge
        messages.success(request,"Your message has been sent!")

    return render(request,"contact.html")

def terms(request):
    return render(request,"terms.html")


def disclaimer(request):
    return render(request,"disclaimer.html")


def sitemap_page(request):

    tools = Tool.objects.all()

    return render(request,"sitemap_page.html",{
        "tools":tools
    })