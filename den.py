import tkinter as tk
import random
import winsound
import datetime

def generate_random_text():
    texts = [
        "Evet bu mesajı gördün, sen bir harikasın!",
        "Eğer bu mesajı görürsen Discord üzerinden selam gönder.",
        "Bana selam söyle!",
        "Programımı beğendin mi?",
        "İyi günler!",
        "Programlama eğlencelidir!",
        "Hadi biraz daha tıkla!",
        "Kod yazmaya devam edin!",
        "Başarılar!",
        "Güzel bir gün olsun!"
    ]
    random_text = random.choice(texts)
    label.config(text=random_text, font=("Arial", 18), fg="blue")

def play_sound():
    global sound_playing
    if sound_playing:
        winsound.PlaySound(None, winsound.SND_PURGE)
        sound_playing = False
    else:
        winsound.PlaySound("dosyalar/sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        sound_playing = True

root = tk.Tk()
root.title("Shady Mesajlaşma")
root.geometry("850x450")

# Programın üst kısmındaki başlık çubuğuna ikon ekleme
root.iconbitmap("dosyalar/kerrhigh_1.ico")

label = tk.Label(root, text="Butona Tıklayın", font=("Arial", 24))
label.pack(pady=20)

button = tk.Button(root, text="Üret", font=("Arial", 14), command=generate_random_text)
button.pack(pady=10)

sound_playing = False

# Alt bölüm için çerçeve (frame) oluşturma
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(fill=tk.X, side=tk.BOTTOM)

# "Pixel" yazısı
pixel_label = tk.Label(frame, text="Pixel", font=("Arial", 12), bg="#f0f0f0", fg="gray")
pixel_label.pack(side=tk.LEFT, padx=10, pady=5)

# Tarih bilgisi
now = datetime.datetime.now()
date_label = tk.Label(frame, text=now.strftime("%d.%m.%Y"), font=("Arial", 12), bg="#f0f0f0", fg="gray")
date_label.pack(side=tk.RIGHT, padx=10, pady=5)

root.mainloop()
