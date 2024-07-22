import tkinter as tk
from flask import Flask, render_template, Response
import datetime
import time
import threading
#pip install flask
global mensagem
# Inicializar a mensagem

mensagem = "broadcast news"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    global mensagem
    while True:
        
        yield  f"data: {mensagem}\n\n"
        time.sleep(1)


@app.route('/time')
def time_stream():
    return Response(generate(), mimetype='text/event-stream')

def targets():
    app.run(host='0.0.0.0', port=5000, threaded=True)


def change_message():
    global mensagem
    mensagem = texts.get("1.0", "end-1c").replace("\n","<br>").replace("\r","<br>")
    
    message_label.config(text=mensagem)
    
# Criar a janela principal
root = tk.Tk()
root.title("Change Message")
root.geometry("630x400")
root.configure(bg='white')

# Adicionar um rótulo para exibir a mensagem
message_label = tk.Label(root, text=mensagem, bg='white', font=('Arial', 14))
message_label.pack(pady=20)

# Adicionar uma caixa de texto
#texts = tk.Entry(root, font=('Arial', 14))

texts = tk.Text(root, height=10, width=50,font=('Arial', 14))
texts.pack(pady=10)


# Adicionar um botão "Change"
change_button = tk.Button(root, text="Change", command=change_message, font=('Arial', 14))
change_button.pack(pady=10)

# Iniciar o loop principal da aplicação

t1 = threading.Thread(target=targets)
t1.start()
root.mainloop()
t1.join()
