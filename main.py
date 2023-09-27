from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog, messagebox


# Function to add text to the image when it's clicked
def add_it(event):
    # OPEN THE IMAGE WITH PIL
    my_image = Image.open("pic.png")

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(my_image)
    # Custom font style and font size

    if text_size.get():
        size = int(text_size.get())
    else:
        size = 50
    myFont = ImageFont.truetype('CroissantOne-Regular.ttf', size)

    # get text to add to image
    text_to_add = my_entry.get()
    if not text_to_add:
        messagebox.showwarning(title="Oops⚠️", message="Please make sure you enter text to add to the image.")
    else:
        color = color_entry.get()
        if not color:
            color = "red"
            messagebox.showwarning(title="Oops", message="You didn't specify color Default color is :RED❗")

        x, y = event.x, event.y
        if not x and y:
            x, y = 10, 10

        I1.text((x, y), text_to_add, font=myFont, fill=color)
        # save the image
        new_name = new_img.get()
        my_image.save(f"{new_name}.png")
        my_entry.delete(0, END)
        # wait and show image
        my_label.after(1000, show_pic(new_name))
        messagebox.showinfo(title="SAVED ", message="Watermark successfully added to your image")


# Function to display the saved image
def show_pic(name):
    global kiz1
    kiz1 = PhotoImage(file=f"{name}.png")
    my_label.config(image=kiz1)


# Function to open an image using a file dialog
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        my_image = Image.open(file_path)
        return my_image


# Create a Tkinter window
messagebox.showinfo(title="Info", message="Please🙏 select an image🖼️ that you want to edit")
kiz_image = open_image()
window = Tk()
window.title("Watermark🚰")
window.config(padx=50, pady=50)
kiz_image = ImageTk.PhotoImage(kiz_image)

# Create a label to display the image
my_label = Label(window, image=kiz_image)
my_label.grid(row=0, column=0, columnspan=4, padx=50, pady=50)
my_label.bind("<Button-1>", add_it)  # Bind the click event to the label

# Set padding values for labels and buttons
padding_x = 10
padding_y = 10

# Create labels and buttons with consistent width
label_width = 15

# Color Entry
welcome = Label(window, text="➡️Add waterMark of your choice with options below⬇️:", font=("Helvetica", 15))
welcome.grid(row=1, column=0, padx=padding_x, pady=padding_y, sticky="e", columnspan=2)
messagebox.showinfo(title="INFO!🔼", message="After you finish to put your watermark properties \nPlease click any "
                                            "position on your picture that you want your WATERMARK to be added")

color_entry = Entry(window, font=("Helvetica", 24))
color_entry.grid(row=2, column=1, padx=padding_x, pady=padding_y, sticky="w")
color_label = Label(window, text="Text Color🔵:", font=("Helvetica", 15))
color_label.grid(row=2, column=0, padx=padding_x, pady=padding_y, sticky="e")

# TEXT SIZE
text_size = Entry(window, font=("Helvetica", 24))
text_size.grid(row=3, column=1, padx=padding_x, pady=padding_y, sticky="w")
text_size_label = Label(window, text="Text size🔠:", font=("Helvetica", 15))
text_size_label.grid(row=3, column=0, padx=padding_x, pady=padding_y, sticky="e")

my_entry = Entry(window, font=("Helvetica", 24))
my_entry.grid(row=4, column=1, padx=padding_x, pady=padding_y, sticky="w")
my_entry.focus()
my_button = Label(window, text="Add Text to Image🔤", font=("Helvetica", 15))
my_button.grid(row=4, column=0, padx=padding_x, pady=padding_y, sticky="e")

new_img = Entry(window, font=("Helvetica", 24))
new_img.grid(row=5, column=1, padx=padding_x, pady=padding_y, sticky="w")
new_img_label = Label(window, text="Name for the edited picture:", font=("Helvetica", 15))
new_img_label.grid(row=5, column=0, padx=padding_x, pady=padding_y, sticky="e")

messagebox.showinfo(title="Picture uploaded successfully✅!", message="Its time to add a watermark❕")

window.mainloop()
