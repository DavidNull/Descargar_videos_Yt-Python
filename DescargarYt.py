from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, messagebox
from pytube import YouTube
# https://pytube.io/en/latest/
# https://docs.python.org/es/3/library/tkinter.html

def download_video():
    link = url_var.get()
    if not link:
        messagebox.showerror("Error", "Ingresa un enlace de YouTube")
        return

    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        
        save_path = filedialog.askdirectory()
        if not save_path:
            messagebox.showwarning("Cancelado", "No se seleccionó ninguna carpeta")
            return
        
        stream.download(save_path)
        messagebox.showinfo("Todo ok", f"¡Video descargado con éxito en: {save_path}!")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al descargar el video: {e}")


root = Tk()
root.title("Descargador de YouTube")
root.geometry("500x200")

url_var = StringVar()

Label(root, text="Descargador de Videos de YouTube", font=("Helvetica", 16)).pack(pady=10)
Label(root, text="Ingresa el enlace del video:", font=("Helvetica", 12)).pack(pady=5)
Entry(root, textvariable=url_var, width=50).pack(pady=5)

Button(root, text="Descargar Video", command=download_video, bg="blue", fg="white", font=("Helvetica", 12)).pack(pady=20)

root.mainloop()
