# Tkinterのライブラリを取り込む
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os


# ファイルの参照処理
def click_refer_button():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file_path.set(filepath)


if __name__ == '__main__':

    # ウィンドウを作成
    root = tkinter.Tk()
    root.title("hello world") # アプリの名前
    root.geometry("500x300") # アプリの画面サイズ


    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル名：')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルのパスを表示するテキストボックスの作成
    file_path = StringVar()
    filepath_entry = ttk.Entry(frame1, textvariable=file_path, width=50)
    filepath_entry.grid(row=0, column=1)

    # 参照ボタンの作成
    refer_button = ttk.Button(root, text=u'参照', command=click_refer_button)
    refer_button.grid(row=0, column=2)

    # アプリ起動
    root.mainloop()
