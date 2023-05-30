from PIL import Image

from PIL.ExifTags import TAGS

import tkinter as tk

from tkinter import filedialog, messagebox

def open_file_dialog():

    root = tk.Tk()

    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if file_path:

        extract_geolocation(file_path)

    else:

        messagebox.showinfo("File selection", "No file selected.")

def extract_geolocation(photo_path):

    try:

        image = Image.open(photo_path)

        exif_data = image._getexif()

        if exif_data is None:

            messagebox.showinfo("EXIF Data", "No EXIF data found in the photo.")

            return

        for tag, value in exif_data.items():

            if TAGS.get(tag) == 'GPSInfo':

                gps_info = value

                lat_ref = gps_info[1]

                lat = gps_info[2]

                lon_ref = gps_info[3]

                lon = gps_info[4]

                latitude = lat[0] + lat[1] / 60 + lat[2] / 3600

                longitude = lon[0] + lon[1] / 60 + lon[2] / 3600

                if lat_ref == 'S':

                    latitude = -latitude

                if lon_ref == 'W':

                    longitude = -longitude

                show_location_info(latitude, longitude)

                return

        messagebox.showinfo("GPS Information", "No GPS information found in the photo.")

    except Exception as e:

        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def show_location_info(latitude, longitude):

    messagebox.showinfo("Location Information", f"Latitude: {latitude}\nLongitude: {longitude}")

# Usage

open_file_dialog()

 

