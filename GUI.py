import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import os

# Import your existing modules
import fasttext
from pathlib import Path
import pdfParser as pp
import extraction_summary
import cosine_similarity
import wordcloud_am

class TextSummarizerGUI:import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import os

# Import your existing modules
import fasttext
from pathlib import Path
import pdfParser as pp
import extraction_summary
import cosine_similarity
import wordcloud_am

class TextSummarizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Text Summarizer")

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.master, text="Enter PDF URL:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = ttk.Entry(self.master, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        self.summarize_button = ttk.Button(self.master, text="Summarize", command=self.summarize_text)
        self.summarize_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_text_label = ttk.Label(self.master, text="Summarized Text:")
        self.result_text_label.grid(row=2, column=0, padx=10, pady=10)

        self.result_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=80, height=20)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def summarize_text(self):
        url = self.url_entry.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid PDF URL.")
            return

        try:
            # Read PDF
            pparser = pp.pdfPrser(url)

            # Detect language
            lang = detect_language(pparser.clean_text)

            if lang == 'am':
                # Wordclouds
                wordcloud_am.generate_wordcloud(pparser.words, pparser.stop_words, 'word_cloud.png')

                # Extraction summary
                hyper_param = 1.5
                ext_summary = extraction_summary._get_summary(pparser, hyper_param)
                self.update_result_text(ext_summary)

                # Cosine summary
                cos_summary = cosine_similarity.build_summary(pparser.sentences, pparser.stop_words)
                self.update_result_text('\n\nCosine Similarity Summary:\n' + cos_summary)
                
                # Abstract summary (TODO)

            else:
                messagebox.showwarning("Unsupported Language", f"Language not supported for {url}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_result_text(self, text):
        self.result_text.delete(1.0, tk.END)  # Clear previous text
        self.result_text.insert(tk.END, text)


def detect_language(text):
    model = fasttext.load_model(os.path.dirname(Path(__file__)) + '/fastText/lid.176.ftz')
    return model.predict(text, k=1)[0][0][-2:]


def main():
    root = tk.Tk()
    app = TextSummarizerGUI(root)
    
    # Set the size of the window
    root.geometry("800x600")
    
    root.mainloop()


if __name__ == "__main__":
    main()

    def __init__(self, master):
        self.master = master
        master.title("Text Summarizer")

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.master, text="Enter PDF URL:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = ttk.Entry(self.master, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        self.summarize_button = ttk.Button(self.master, text="Summarize", command=self.summarize_text)
        self.summarize_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_text_label = ttk.Label(self.master, text="Summarized Text:")
        self.result_text_label.grid(row=2, column=0, padx=10, pady=10)

        self.result_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=60, height=10)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def summarize_text(self):
        url = self.url_entry.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid PDF URL.")
            return

        try:
            # Read PDF
            pparser = pp.pdfPrser(url)

            # Detect language
            lang = detect_language(pparser.clean_text)

            if lang == 'am':
                # Wordclouds
                wordcloud_am.generate_wordcloud(pparser.words, pparser.stop_words, 'word_cloud.png')

                # Extraction summary
                hyper_param = 1.5
                ext_summary = extraction_summary._get_summary(pparser, hyper_param)
                self.update_result_text(ext_summary)

                # Cosine summary
                cos_summary = cosine_similarity.build_summary(pparser.sentences, pparser.stop_words)
                self.update_result_text('\n\nCosine Similarity Summary:\n' + cos_summary)
                
                # Abstract summary (TODO)

            else:
                messagebox.showwarning("Unsupported Language", f"Language not supported for {url}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_result_text(self, text):
        self.result_text.delete(1.0, tk.END)  # Clear previous text
        self.result_text.insert(tk.END, text)


def detect_language(text):
    model = fasttext.load_model(os.path.dirname(Path(__file__)) + '/fastText/lid.176.ftz')
    return model.predict(text, k=1)[0][0][-2:]


def main():
    root = tk.Tk()
    app = TextSummarizerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
