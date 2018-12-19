import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Settings
ImageWidth = 512
ImageHeight = 512
OriginPath = ''
DestinationPath = ''


class SettingFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['width'] = 400
        self['height'] = 200
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.setting_label = tk.Label(self, text='Settings')
        self.setting_label.grid(column=1, row=0, columnspan=3)

        self.target_width_label = tk.Label(self)
        self.target_width_label['text'] = 'Target Width:'
        self.target_width_entry = tk.Entry(self)
        self.target_width_entry.insert(0, '512')
        self.target_width_label.grid(column=1, row=1)
        self.target_width_entry.grid(column=2, row=1)

        self.target_height_label = tk.Label(self)
        self.target_height_label['text'] = 'Target Height:'
        self.target_height_entry = tk.Entry(self)
        self.target_height_entry.insert(0, '512')
        self.target_height_label.grid(column=1, row=2)
        self.target_height_entry.grid(column=2, row=2)

        self.origin_file_path_label = tk.Label(self)
        self.origin_file_path_label['text'] = 'Origin Image Folder: '
        self.origin_file_path_entry = tk.Entry(self)
        self.origin_file_path_button = tk.Button(self, text='Browse')
        self.origin_file_path_button = tk.Button(
            self, text='Browse...', command=self.fileDialog(self.origin_file_path_entry))
        self.origin_file_path_label.grid(column=1, row=3)
        self.origin_file_path_entry.grid(column=2, row=3)
        self.origin_file_path_button.grid(column=3, row=3)

        self.destination_file_path_label = tk.Label(self)
        self.destination_file_path_label['text'] = 'Destination Image Folder: '
        self.destination_file_path_entry = tk.Entry(self)
        self.destination_file_path_button = tk.Button(
            self, text='Browse...', command=self.fileDialog(self.destination_file_path_entry))
        self.destination_file_path_label.grid(column=1, row=4)
        self.destination_file_path_entry.grid(column=2, row=4)
        self.destination_file_path_button.grid(column=3, row=4)

        self.start_button = tk.Button(
            self, text='Start', command=self.save_settings_and_close())
        self.start_button.grid(column=1, columnspan=3, row=5)

        self.bind('<Enter>', self.HandleKeyEnter(
            self.save_settings_and_close()))

    def fileDialog(self, entry):
        def fx():
            entry.delete(0, 'end')
            entry.insert(0, filedialog.askdirectory())
        return fx

    def HandleKeyEnter(self, f):
        def fx(e):
            f()
        return fx

    def save_settings_and_close(self):
        def fx():
            global ImageWidth, ImageHeight, OriginPath, DestinationPath
            ImageWidth = self.target_width_entry.get()
            ImageHeight = self.target_height_entry.get()
            OriginPath = self.origin_file_path_entry.get()
            DestinationPath = self.destination_file_path_entry.get()
            self.master.destroy()
        return fx


if __name__ == '__main__':
    root = tk.Tk()
    root.style = ttk.Style()
    root.style.theme_use('clam')
    root.title('ImageCroper2000')
    setting = SettingFrame(root)
    setting.mainloop()
