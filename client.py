import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext


class ChatClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        # نافذة منبثقة لطلب الاسم
        root = tk.Tk()
        root.withdraw()
        self.nickname = simpledialog.askstring(
            "الاسم", "الرجاء إدخال اسمك المستعار:", parent=root
        )

        if not self.nickname:
            self.nickname = "مجهول"

        # بناء الواجهة الرسومية الرئيسية
        self.win = tk.Tk()
        self.win.title(f"غرفة الدردشة - {self.nickname}")
        self.win.geometry("400x500")

        self.chat_label = tk.Label(
            self.win, text="المحادثة الجماعية:", font=("Arial", 12)
        )
        self.chat_label.pack(padx=10, pady=5)

        self.text_area = scrolledtext.ScrolledText(self.win, font=("Arial", 10))
        self.text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        self.text_area.config(state="disabled")

        self.msg_label = tk.Label(self.win, text="اكتب رسالتك هنا:", font=("Arial", 10))
        self.msg_label.pack(padx=10, pady=5)

        self.input_area = tk.Entry(self.win, font=("Arial", 12))
        self.input_area.pack(padx=10, pady=5, fill=tk.X)
        self.input_area.bind("<Return>", self.write)  # الإرسال عند الضغط على Enter

        self.send_button = tk.Button(
            self.win, text="إرسال", font=("Arial", 10), command=self.write
        )
        self.send_button.pack(padx=10, pady=5)

        # تشغيل Thread الاستقبال
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.win.mainloop()

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if message == "NICK":
                    self.client.send(self.nickname.encode("utf-8"))
                else:
                    self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, message + "\n")
                    self.text_area.yview(tk.END)
                    self.text_area.config(state="disabled")
            except:
                print("تم قطع الاتصال!")
                self.client.close()
                break

    def write(self, event=None):
        message = self.input_area.get()
        if message:
            full_message = f"{self.nickname}: {message}"
            # إظهار الرسالة محلياً في نافذة المرسل
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, full_message + "\n")
            self.text_area.yview(tk.END)
            self.text_area.config(state="disabled")

            # إرسال الرسالة للخادم ليبثها للباقين
            self.client.send(full_message.encode("utf-8"))
            self.input_area.delete(0, tk.END)

    def on_closing(self):
        self.client.close()
        self.win.destroy()


if __name__ == "__main__":
    ChatClient("127.0.0.1", 55555)
