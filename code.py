from PIL import Image
import pytesseract
import google.generativeai as genai

genai.configure(api_key="api-key")
model=genai.GenerativeModel("gemini-2.5-pro")
img = Image.open('invoice.png')
text = pytesseract.image_to_string(img)
print(text)

question=input("What would you like to ask about this document?\n")
response = model.generate_content([
    f"Document:\n{text}",
    question
])
print("\nAnswer:\n", response.text)


