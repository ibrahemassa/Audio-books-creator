from tkinter import *
from tkinter import filedialog

from gtts import gTTS
import PyPDF2

pdf_file = None


def convert():
    language = 'en'
    global pdf_file

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    pdf_file.close()

    print(text)

    speach = gTTS(text=text, lang=language, slow=0)
    speach_file = f'{output_name.get()}.mp3'
    speach.save(speach_file)


def open_file():
    global pdf_file
    pdf_file = filedialog.askopenfile(mode='rb', filetypes=[("PDF files", "*.pdf")])
    browse_label.config(text=pdf_file.name.split('/')[-1])


root = Tk()
root.title("Audio book creator")
root.geometry("300x300")
root.resizable(width=False, height=False)

browse_label = Label(text='Select a PDF file:', font=('Aerial', 16))
browse_label.pack()

browse_button = Button(root, text='Browse', font=('Georgia', 13), padx=20, command=open_file)
browse_button.pack(pady=10)

output_label = Label(text='Enter the output file name:', font=('Aerial', 16))
output_label.pack()

output_name = Entry(root, font=('Aerial', 16))
output_name.pack(pady=7)

save_button = Button(root, text='Save', font=('Georgia', 13), padx=20, command=convert)
save_button.pack(pady=40)


root.mainloop()





