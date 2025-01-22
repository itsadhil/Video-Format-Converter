import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from moviepy.editor import VideoFileClip
import os

# Supported video formats
VIDEO_FORMATS = ["mp4", "avi", "mov", "mkv", "wmv", "flv", "webm", "gif"]

# Function to convert video
def convert_video(input_path, output_path, output_format):
    try:
        # Load the video
        clip = VideoFileClip(input_path)
        # Write the video in the desired format
        output_file = f"{output_path}.{output_format}"
        clip.write_videofile(output_file, codec="libx264")
        clip.close()
        messagebox.showinfo("Success", f"Video converted successfully!\nSaved to: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Function to handle conversion process
def start_conversion():
    input_path = input_file_var.get()
    output_path = output_file_var.get()
    output_format = output_format_var.get()
    
    if not input_path or not output_path or not output_format:
        messagebox.showerror("Error", "Please select all fields before converting.")
        return
    
    convert_video(input_path, output_path, output_format)

# Function to browse input video file
def browse_input_file():
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv *.webm *.gif")]
    )
    input_file_var.set(file_path)

# Function to browse output folder
def browse_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_file_var.set(os.path.join(folder_path, "output_video"))

# Create the main application window
root = ThemedTk(theme="equilux")
root.title("Video Format Converter")
root.geometry("500x300")

# Input file selection
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
output_format_var = tk.StringVar()

ttk.Label(root, text="Select Input Video:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
ttk.Entry(root, textvariable=input_file_var, width=40).grid(row=0, column=1, padx=10, pady=10)
ttk.Button(root, text="Browse", command=browse_input_file).grid(row=0, column=2, padx=10, pady=10)

# Output folder selection
ttk.Label(root, text="Select Output Path:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
ttk.Entry(root, textvariable=output_file_var, width=40).grid(row=1, column=1, padx=10, pady=10)
ttk.Button(root, text="Browse", command=browse_output_folder).grid(row=1, column=2, padx=10, pady=10)

# Output format selection
ttk.Label(root, text="Select Output Format:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
ttk.Combobox(root, textvariable=output_format_var, values=VIDEO_FORMATS, state="readonly", width=37).grid(row=2, column=1, padx=10, pady=10)

# Convert button
ttk.Button(root, text="Convert Video", command=start_conversion).grid(row=3, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
