import tkinter as tk
from tkinter import END, messagebox, ttk
from PIL import Image, ImageTk
import csv
import os
from collections import defaultdict

class TheaterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Theater Management System")
        self.geometry("800x500")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=500)
        self.canvas.pack(fill="both", expand=True)

        # Load the background image
        self.bg_image = Image.open("background.jpg")  # Replace with your background image file
        self.bg_image = self.bg_image.resize((800, 500), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Display the background image
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.label_title = tk.Label(self, text="Theater Management System", font=("Lucida Handwriting", 30, "bold"), bg="#850305", fg="#fc5154")
        self.canvas.create_window(400, 50, window=self.label_title)

        self.label_title = tk.Label(self, text="New to the website??", font=("Segoe UI Light", 14), bg="#14151a", fg="White")
        self.canvas.create_window(300, 150, window=self.label_title)

        self.label_title = tk.Label(self, text="Already existing user??Login!!", font=("Segoe UI Light", 15), bg="#d6b087")
        self.canvas.create_window(400, 230, window=self.label_title)

        # Create the manager button
        self.button_manager = tk.Button(self, text="ADMIN", font=("Helvetica", 14), activebackground='Red', width=15, height=2, command=self.open_manager_login)
        self.canvas.create_window(300, 300, window=self.button_manager)

        # Create the user button
        self.button_user = tk.Button(self, text="USER", font=("Helvetica", 14), width=15, height=2, command=self.open_user_login)
        self.canvas.create_window(520, 300, window=self.button_user)
        
        # Create the create account button
        self.button_create_account = tk.Button(self, text="Create Account", font=("Helvetica", 14), width=15, height=2, command=self.open_create_account)
        self.canvas.create_window(500, 150, window=self.button_create_account)

    def open_manager_login(self):
        self.withdraw()  # Hide the main window
        manager_login_window = ManagerLogin(self)
        manager_login_window.grab_set()

    def open_user_login(self):
        self.withdraw()  # Hide the main window
        user_login_window = UserLogin(self)
        user_login_window.grab_set()

    def open_create_account(self):
        self.withdraw()  # Hide the main window
        create_account_window = SignUpPage(self)
        create_account_window.grab_set()

class LoginWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.geometry("800x500")
        self.configure(bg="#14151a")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=500, bg="#14151a")
        self.canvas.pack()

        self.label_username = tk.Label(self, text="Username", font=("Helvetica", 14), bg="#14151a", fg="white")
        self.canvas.create_window(400, 200, window=self.label_username)

        self.entry_username = tk.Entry(self, font=("Helvetica", 14))
        self.canvas.create_window(400, 230, window=self.entry_username)

        self.label_password = tk.Label(self, text="Password", font=("Helvetica", 14), bg="#14151a", fg="white")
        self.canvas.create_window(400, 260, window=self.label_password)

        self.entry_password = tk.Entry(self, show="*", font=("Helvetica", 14))
        self.canvas.create_window(400, 290, window=self.entry_password)

        self.button_login = tk.Button(self, text="Login", font=("Helvetica", 14), command=self.login)
        self.canvas.create_window(400, 350, window=self.button_login)

        self.button_back = tk.Button(self, text="Back", font=("Helvetica", 14), command=self.go_back)
        self.canvas.create_window(400, 400, window=self.button_back)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.validate_login(username, password):
            self.login_success_message()
        else:
            self.login_failed_message()

    def login_success_message(self):
        messagebox.showinfo("Login Successful", "Welcome!")

    def login_failed_message(self):
        messagebox.showerror("Login Failed", "Invalid username or password")

    def go_back(self):
        self.destroy()  # Close the current window
        self.master.deiconify()  # Show the main window

class ManagerLogin(LoginWindow):
    def __init__(self, master):
        super().__init__(master)
        self.title("Admin Login")

        # Load the image
        self.manager_image = Image.open("manager.png")  # Replace with your manager image file
        self.manager_image = self.manager_image.resize((150, 150), Image.Resampling.LANCZOS)
        self.manager_photo = ImageTk.PhotoImage(self.manager_image)

        # Create a label with the image
        self.label_image = tk.Label(self.canvas, image=self.manager_photo, bg="#14151a")
        self.canvas.create_window(400, 100, window=self.label_image)

    def validate_login(self, username, password):
        return username == "admin" and password == "Password@123"

    def login_success_message(self):
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        self.destroy()
        manager_page_window = AdminPage(self.master)
        manager_page_window.grab_set()

class UserLogin(LoginWindow):
    def __init__(self, master):
        super().__init__(master)
        self.title("User Login")

        # Load the image
        self.user_image = Image.open("user.png")  # Replace with your user image file
        self.user_image = self.user_image.resize((150, 150), Image.Resampling.LANCZOS)
        self.user_photo = ImageTk.PhotoImage(self.user_image)

        # Create a label with the image
        self.label_image = tk.Label(self.canvas, image=self.user_photo, bg="#14151a")
        self.canvas.create_window(400, 100, window=self.label_image)
    
    def validate_login(self, username, password):
        # Example: You might want to load and check credentials from a CSV file
        users_file = 'users.csv'
        if os.path.isfile(users_file):
            with open(users_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Username'] == username and row['Password'] == password:
                        return True
        return False

    def login_success_message(self):
        messagebox.showinfo("Login Successful", "Welcome, User!")
        self.destroy()
        user_page_window = UserPage(self.master)
        user_page_window.grab_set()

class SignUpPage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("SIGN UP")

        self.w_width = 800
        self.w_height = 700
        self.geometry(f"{self.w_width}x{self.w_height}+250+10")
        self.resizable(0, 0)
        
        self.bg_image = ImageTk.PhotoImage(file="accnt.png")
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        self.title_label = tk.Label(self, text="SIGN UP", font=("Microsoft Yahei UI Light", 20), bg="white")
        self.title_label.pack()

        self.accntimg = ImageTk.PhotoImage(file="accnt.png")
        self.accnt_lbl = tk.Label(self, image=self.accntimg) 
        self.accnt_lbl.place(x=0, y=0)

        self.accnt = tk.Label(self, text="Create Account", font=("Microsoft Yahei UI Light", 25, "bold"), bg="#4B7A80", fg="white", bd=0)
        self.accnt.place(x=260, y=145)

        self.fname = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.fname.insert(0, 'First Name')
        self.fname.bind('<FocusIn>', self.on_press_fname)
        self.fname.place(x=234, y=197)

        self.lname = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.lname.insert(0, 'Last Name')
        self.lname.bind('<FocusIn>', self.on_press_lname)
        self.lname.place(x=234, y=259)

        self.uname = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.uname.insert(0, 'Username')
        self.uname.bind('<FocusIn>', self.on_press_uname)
        self.uname.place(x=234, y=321)

        self.pwd = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.pwd.insert(0, 'Password')
        self.pwd.bind('<FocusIn>', self.on_press_pwd)
        self.pwd.place(x=234, y=385)

        self.cfm_pwd = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.cfm_pwd.insert(0, 'Confirm Password')
        self.cfm_pwd.bind('<FocusIn>', self.on_press_cfm_pwd)
        self.cfm_pwd.place(x=234, y=450)

        self.email = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.email.insert(0, 'E-mail')
        self.email.bind('<FocusIn>', self.on_press_email)
        self.email.place(x=234, y=513)

        self.contact = tk.Entry(self, width=25, font=("Microsoft Yahei UI Light", 13), bg="#FFFFFF", fg="grey", bd=0)
        self.contact.insert(0, 'Contact')
        self.contact.bind('<FocusIn>', self.on_press_contact)
        self.contact.place(x=234, y=576)

        self.create = tk.Button(self, width=18, text="Create Account", font=("Microsoft Yahei UI Light", 15), bd=0, bg="#1A182E", fg="cyan", activebackground="cyan", activeforeground="#1A182E", cursor="hand2", command=self.createaccount)
        self.create.place(x=300, y=640)

        self.button_back = tk.Button(self, text="Back to Main Page", font=("Microsoft Yahei UI Light", 12), bd=0, bg="#1A182E", fg="cyan", activebackground="cyan", activeforeground="#1A182E", cursor="hand2", command=self.go_back)
        self.button_back.place(x=630, y=645)

    def on_press_fname(self, event):
        if self.fname.get() == "First Name":
            self.fname.delete(0, END)
            self.fname.config(fg="black")

    def on_press_lname(self, event):
        if self.lname.get() == "Last Name":
            self.lname.delete(0, END)
            self.lname.config(fg="black")

    def on_press_uname(self, event):
        if self.uname.get() == "Username":
            self.uname.delete(0, END)
            self.uname.config(fg="black")

    def on_press_pwd(self, event):
        if self.pwd.get() == "Password":
            self.pwd.delete(0, END)
            self.pwd.config(fg="black")

    def on_press_cfm_pwd(self, event):
        if self.cfm_pwd.get() == "Confirm Password":
            self.cfm_pwd.delete(0, END)
            self.cfm_pwd.config(fg="black")

    def on_press_email(self, event):
        if self.email.get() == "E-mail":
            self.email.delete(0, END)
            self.email.config(fg="black")
    
    def on_press_contact(self, event):
        if self.contact.get() == "Contact":
            self.contact.delete(0, END)
            self.contact.config(fg="black")

    def go_back(self):
        self.destroy()
        self.master.deiconify()

    def createaccount(self):
        if self.fname.get() in (None, "First Name") or self.lname.get() in (None, "Last Name") or self.uname.get() in (None, "Username") or self.pwd.get() in (None, "Password") or self.cfm_pwd.get() in (None, "Confirm Password") or self.email.get() in (None, "E-mail") or self.contact.get() in (None, "Contact"):
            messagebox.showerror("Error", "All fields are required")
        elif self.cfm_pwd.get() != self.pwd.get():
            messagebox.showerror("Error", "Confirm the correct password")
        else:
            try:
                users_file = 'users.csv'
                # Check if the CSV file exists
                if not os.path.isfile(users_file):
                    with open(users_file, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(['First_Name', 'Last_Name', 'Username', 'Password', 'Email', 'Contact'])

                # Check if username already exists
                with open(users_file, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Username'] == self.uname.get():
                            messagebox.showerror("Error", "Username already exists")
                            return

                # Write new user data to the CSV file
                with open(users_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.fname.get(), self.lname.get(), self.uname.get(), self.pwd.get(), self.email.get(), self.contact.get()])

                messagebox.showinfo("Welcome {}".format(self.uname.get()), "Account created successfully")
                self.go_back()
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {e}")

class AdminPage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Admin Dashboard")
        self.geometry("700x400")
        self.configure(bg="#453737")
        self.available_screens = 16  # Total available screens
        self.allocated_screens = 0  # Total screens allocated
        self.scheduled_movies = {}  # Dictionary to store scheduled movies and their allocated screens
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=700, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Load and display the background image
        self.bg_image = Image.open("theatre.jpg")
        self.bg_image = self.bg_image.resize((700, 400), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create all labels and buttons
        self.label_welcome = tk.Label(self, text="Welcome to the Admin Dashboard", font=("Lucida Handwriting", 20, "bold"), bg="#440303", fg="#ac67dd")
        self.canvas.create_window(350, 30, window=self.label_welcome)

        self.button_book_tickets = tk.Button(self, text="Schedule Screen", font=("Helvetica", 14), bg="#aeaeae", command=self.open_movie_scheduler)
        self.canvas.create_window(350, 200, window=self.button_book_tickets)

        self.button_view_movies = tk.Button(self, text="Remove Movies", font=("Helvetica", 14), bg="#aeaeae", command=self.open_remove_movie)
        self.canvas.create_window(350, 250, window=self.button_view_movies)

        self.button_view_history = tk.Button(self, text="View Booking History", font=("Helvetica", 14), bg="#aeaeae", command=self.open_view_bookings)
        self.canvas.create_window(350, 300, window=self.button_view_history)

        self.button_logout = tk.Button(self, text="LOGOUT", font=("Helvetica", 8), command=self.logout, bg="Black", fg="White")
        self.canvas.create_window(130, 380, window=self.button_logout)

    def open_movie_scheduler(self):
        self.destroy()
        MovieScheduler(self)

    def open_remove_movie(self):
        self.destroy()
        remove_movie=RemoveMoviePage(self)

    def open_view_bookings(self):
        self.destroy()
        ViewBookingsPage(self)

    def logout(self):
        self.destroy()
        self.master.deiconify()
    
    def deiconify(self):
        if self.master:
            self.master.deiconify()

class MovieScheduler(tk.Toplevel):
    def __init__(self, admin_page):
        super().__init__(admin_page.master)
        self.admin_page = admin_page
        self.title("Movie Scheduler")
        self.geometry("800x500")

        self.movies = self.load_movies()
        self.num_screens = 16

        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.movie_label = tk.Label(self, text="Enter Movie Details:")
        self.canvas.create_window(10, 10, window=self.movie_label, anchor="nw")

        self.title_label = tk.Label(self, text="Title:")
        self.canvas.create_window(50, 50, window=self.title_label, anchor="center")
        self.title_entry = tk.Entry(self)
        self.canvas.create_window(150, 50, window=self.title_entry, anchor="center")

        self.cast_label = tk.Label(self, text="Cast:")
        self.canvas.create_window(50, 90, window=self.cast_label, anchor="center")
        self.cast_entry = tk.Entry(self)
        self.canvas.create_window(150, 90, window=self.cast_entry, anchor="center")

        self.description_label = tk.Label(self, text="Description:")
        self.canvas.create_window(50, 130, window=self.description_label, anchor="center")
        self.description_entry = tk.Entry(self)
        self.canvas.create_window(150, 130, window=self.description_entry, anchor="center")

        self.rating_label = tk.Label(self, text="Rating:")
        self.canvas.create_window(50, 170, window=self.rating_label, anchor="center")
        self.rating_entry = tk.Entry(self)
        self.canvas.create_window(150, 170, window=self.rating_entry, anchor="center")

        self.add_button = tk.Button(self, text="Add Movie", command=self.add_movie)
        self.canvas.create_window(50, 210, window=self.add_button, anchor="center")

        self.schedule_button = tk.Button(self, text="Schedule Movies", command=self.schedule_movies)
        self.canvas.create_window(100, 250, window=self.schedule_button, anchor="center")

        self.result_label = tk.Label(self, text="")
        self.canvas.create_window(400, 200, window=self.result_label, anchor="center")

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.canvas.create_window(50, 450, window=self.back_button, anchor="e")

    def add_movie(self):
        title = self.title_entry.get()
        cast = self.cast_entry.get()
        try:
            rating = float(self.rating_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid rating (a number).")
            return
        description = self.description_entry.get()
        self.movies.append({"title": title, "cast": cast, "description": description, "rating": rating, "screen":0})
        
        self.title_entry.delete(0, tk.END)
        self.cast_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

    def get_movie_description(self, title):
        for movie in self.movies:
            if movie['title'] == title:
                return movie['description']
        return "Description not found."
    
    def schedule_movies(self):
        if len(self.movies) == 0:
            messagebox.showerror("Error", "No movies added for scheduling.")
            return

        # Convert all ratings to float
        for movie in self.movies:
            try:
                movie['rating'] = float(movie['rating'])
            except ValueError:
                messagebox.showerror("Error", f"Invalid rating for movie '{movie['title']}': {movie['rating']}")
                return
        
        # Sort movies by rating
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        total_rating = sum(movie['rating'] for movie in sorted_movies)

        # Calculate the number of screens to allocate for each movie proportionally
        screens_allocated = {}
        allocated_screens = 0
        for movie in sorted_movies:
            screens = int((movie['rating'] / total_rating) * self.num_screens)
            allocated_screens += screens
            screens_allocated[movie['title']] = screens

        # Distribute any remaining screens to movies with the highest ratings
        remaining_screens = self.num_screens - allocated_screens
        for movie in sorted_movies:
            if remaining_screens == 0:
                break
            if movie['title'] in screens_allocated:
                screens_allocated[movie['title']] += 1
                remaining_screens -= 1
        
        for movie in self.movies:
            movie['screen'] = screens_allocated.get(movie['title'], 0)
        
        self.save_movies()

        # Display the schedule
        result_text = "Movie Schedule:\n\n"
        for movie, screens in screens_allocated.items():
            result_text += f"Movie: {movie}\nScreens: {screens}\n\n"

        self.result_label.config(text=result_text)
    
    def load_movies(self):
        try:
            with open('movies.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

    def save_movies(self):
        with open('movies.csv', mode='w', newline='') as file:
            fieldnames = ['title', 'cast', 'description', 'rating', 'screen']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for movie in self.movies:
                writer.writerow({'title': movie['title'], 'cast': movie['cast'], 'description': movie['description'], 'rating': movie['rating'], 'screen': movie['screen']})

    def go_back(self):
        self.destroy()
        self.master.deiconify()

class ViewBookingsPage(tk.Toplevel):
    def __init__(self, admin_page):
        super().__init__(admin_page.master)
        self.admin_page = admin_page
        self.title("Booking History")
        self.geometry("400x300")

        bookings = []
        try:
            with open('past_bookings.csv', 'r') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Skip the header row
                for row in reader:
                    if len(row) == 5:  # Ensure there are exactly 4 columns
                        movie, seats, amount, screen, show_time= row
                        bookings.append({'Movie': movie, 'Seats': seats, 'Amount': int(amount), 'Screen': screen, 'Show Time':show_time})
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
            self.go_back()
            return
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.go_back()
            return

        if bookings:
            movie_stats = defaultdict(lambda: {'seats': 0, 'revenue': 0})
            total_revenue = 0

            for booking in bookings:
                movie = booking['Movie']
                seats = booking['Seats'].split(',') if booking['Seats'] else []  # Handle empty seat bookings
                amount = booking['Amount']
                movie_stats[movie]['seats'] += len(seats)
                movie_stats[movie]['revenue'] += amount
                total_revenue += amount

            tk.Label(self, text="Booking History", font=("Arial", 14)).pack(pady=10)

            for movie, stats in movie_stats.items():
                tk.Label(self, text=f"Movie: {movie}, Seats: {stats['seats']}, Revenue: Rs.{stats['revenue']}").pack(pady=5)

            tk.Label(self, text=f"Total Revenue: Rs.{total_revenue}", font=("Arial", 12, "bold")).pack(pady=10)

            back_button = tk.Button(self, text="Back", command=self.go_back)
            back_button.pack(pady=10)
        else:
            messagebox.showinfo("History", "No booking history available.")
            self.go_back()

    def go_back(self):
        self.destroy()
        self.master.deiconify()

class RemoveMoviePage(tk.Toplevel):
    def __init__(self, admin_page):
        super().__init__(admin_page.master)
        self.admin_page = admin_page
        self.title("Remove Movies")
        self.geometry("400x300")
        self.movies = self.load_movies()
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.label = tk.Label(self, text="Select a movie to remove:")
        self.label.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        self.populate_listbox()

        self.remove_button = tk.Button(self, text="Remove Movie", command=self.remove_movie)
        self.remove_button.pack()

        self.remove_button = tk.Button(self, text="Schedule Movie", command=self.schedule_movie)
        self.remove_button.pack()

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack()

    def load_movies(self):
        try:
            with open('movies.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                return [row for row in reader]
        except FileNotFoundError:
            return []

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for movie in self.movies:
            self.listbox.insert(tk.END, movie[0])

    def remove_movie(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a movie to remove.")
            return

        selected_movie = self.listbox.get(selected_index)
        for movie in self.movies:
            if movie[0] == selected_movie:
                self.movies.remove(movie)
                break

        self.update_csv()
        self.populate_listbox()
        messagebox.showinfo("Info", f"{selected_movie} has been removed.")

    def update_csv(self):
        with open('movies.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'cast', 'description', 'rating', 'screen'])
            writer.writerows(self.movies)

    def schedule_movie(self):
        moviescheduling=MovieScheduler(self)
    
    def go_back(self):
        self.destroy()
        self.master.deiconify()  
    
    def on_closing(self):
        self.master.deiconify()
        self.destroy()

class UserPage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("User Dashboard")
        self.geometry("700x400")
        self.configure(bg="#453737")
        self.bookings = []  # Store user bookings
        self.movie_booking_window = None
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=700, height=400)
        self.canvas.pack(fill="both", expand=True)

        #Load and display background image
        self.bg_image = Image.open("theatre.jpg")
        self.bg_image = self.bg_image.resize((700, 400), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create all labels
        self.label_welcome = tk.Label(self, text="Welcome to the User Dashboard", font=("Lucida Handwriting", 20, "bold"), bg="#440303", fg="#ac67dd")
        self.canvas.create_window(350, 30, window=self.label_welcome)

        self.button_book_tickets = tk.Button(self, text="Book Tickets", font=("Helvetica", 14), bg="#aeaeae", command=self.open_movie_selection)
        self.canvas.create_window(350, 200, window=self.button_book_tickets)

        self.button_view_movies = tk.Button(self, text="View Movies", font=("Helvetica", 14), bg="#aeaeae", command=self.view_movies)
        self.canvas.create_window(350, 250, window=self.button_view_movies)

        self.button_view_history = tk.Button(self, text="View History", font=("Helvetica", 14), bg="#aeaeae", command=self.history)
        self.canvas.create_window(350, 300, window=self.button_view_history)

        self.button_logout = tk.Button(self, text="LOGOUT", font=("Helvetica", 8), command=self.logout, bg="Black", fg="White")
        self.canvas.create_window(130, 380, window=self.button_logout)

    def open_movie_selection(self):
        self.destroy()  # Destroy the current window
        self.movie_selection_window = MovieSelectionWindow(self.master, self)

    def book_tickets(self):
        # Ask user to select the movies that are running before booking seats
        movie_selection_window = tk.Toplevel(self.master)
        movie_selection_window.title("Select Movie")
        movie_selection_window.geometry("400x300")

        tk.Label(movie_selection_window, text="Select a Movie", font=("Arial", 14)).pack(pady=10)
        self.selected_movie = tk.StringVar()

        # Listbox to display movies
        self.movie_listbox = tk.Listbox(movie_selection_window, width=40, height=10)
        self.movie_listbox.pack(pady=10)
        self.load_movies_from_csv('movies.csv')

        # Confirm selection button
        confirm_button = tk.Button(movie_selection_window, text="Confirm Selection", command=lambda: self.confirm_movie_selection(movie_selection_window))
        confirm_button.pack(pady=10)
 
    def load_movies_from_csv(self, csv_filename):
        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.movie_listbox.insert(tk.END, row['title'])

    def confirm_movie_selection(self, window):
        try:
            selected_index = self.movie_listbox.curselection()[0]
            selected_movie = self.movie_listbox.get(selected_index)
            self.selected_movie.set(selected_movie)
            window.destroy()
            self.master.withdraw()  # Hide the main user window
            seat_booking_window = tk.Toplevel(self.master)
            seat_booking_screen = SeatBookingScreen(seat_booking_window, selected_movie, self.user_page.master)
        except IndexError:
            messagebox.showwarning("Movie Selection", "Please select a movie.")

    def view_movies(self):
        self.movie_booking_window = MovieBookingApp(self)

    def history(self):
        history_viewer = BookingHistoryViewer(self)
    
    def go_back(self):
        if self.master is not None:
            self.destroy()  # Destroy the current window
            self.master.deiconify()  # Restore the parent window
        else:
            messagebox.showerror("Error", "Parent window not found.")
    
    def logout(self):
        self.destroy()
        self.master.deiconify()

    def deiconify(self):
        if self.master:
            self.master.deiconify()

class MovieSelectionWindow(tk.Toplevel):
    def __init__(self, master, user_page):
        super().__init__(master)
        self.master = master
        self.title("Select Movie")
        self.geometry("400x400")
        self.user_page = user_page

        tk.Label(self, text="Select a Movie", font=("Arial", 14)).pack(pady=10)
        self.selected_movie = tk.StringVar()

        # Listbox to display movies
        self.movie_listbox = tk.Listbox(self, width=40, height=10)
        self.movie_listbox.pack(pady=10)
        # Load movies from CSV
        self.load_movies_from_csv()

        # Confirm selection button
        confirm_button = tk.Button(self, text="Confirm Selection", command=self.confirm_movie_selection)
        confirm_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.destroy()
        self.master.deiconify()


    def load_movies_from_csv(self):
        movies_file = 'movies.csv'
        if os.path.isfile(movies_file):
            with open(movies_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.movie_listbox.insert(tk.END, row['title'])
        else:
            messagebox.showerror("Error", "Movies file not found.")

    def confirm_movie_selection(self):
        try:
            selected_index = self.movie_listbox.curselection()[0]
            selected_movie = self.movie_listbox.get(selected_index)
            self.selected_movie.set(selected_movie)
            self.destroy()  # Destroy the movie selection window
            screen_selection_window = ScreenSelectionWindow(self.master, selected_movie, self.user_page)
        except IndexError:
            messagebox.showwarning("Movie Selection", "Please select a movie.")

class ScreenSelectionWindow(tk.Toplevel):
    def __init__(self, master, selected_movie, user_page):
        super().__init__(master)
        self.master = master
        self.selected_movie = selected_movie
        self.user_page = user_page
        self.title("Select Screen and Show Time")
        self.geometry("600x400")

        tk.Label(self, text="Select a Screen", font=("Arial", 14)).pack(pady=10)
        self.selected_screen = tk.StringVar()
        self.selected_show_time = tk.StringVar()

        # Frame to hold both listboxes
        listbox_frame = tk.Frame(self)
        listbox_frame.pack(pady=10)

        # Listbox to display screens
        self.screen_listbox = tk.Listbox(listbox_frame, width=20, height=10)
        self.screen_listbox.pack(side=tk.LEFT, padx=10)
        self.screen_listbox.bind('<<ListboxSelect>>', self.on_screen_select)
        # Load screens from CSV
        self.load_screens_from_csv()

        # Listbox to display show times
        self.show_time_listbox = tk.Listbox(listbox_frame, width=20, height=10)
        self.show_time_listbox.pack(side=tk.LEFT, padx=10)
        self.show_time_listbox.bind('<<ListboxSelect>>', self.on_show_time_select)
        self.load_show_times()

        # Confirm selection button
        confirm_button = tk.Button(self, text="Confirm Selection", command=self.confirm_selection)
        confirm_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.destroy()
        self.master.deiconify()

    def load_screens_from_csv(self):
        movies_file = 'movies.csv'
        if os.path.isfile(movies_file):
            with open(movies_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['title'] == self.selected_movie:
                        num_screens = int(row.get('screen', 0))
                        for i in range(1, num_screens + 1):
                            self.screen_listbox.insert(tk.END, f"Screen {i}")
        else:
            messagebox.showerror("Error", "Movies file not found.")

    def load_show_times(self):
        show_times = ["11:00 AM", "2:30 PM", "7:00 PM", "10:30 PM"]
        for time in show_times:
            self.show_time_listbox.insert(tk.END, time)

    def on_screen_select(self, event):
        selected_index = self.screen_listbox.curselection()
        if selected_index:
            self.selected_screen.set(self.screen_listbox.get(selected_index[0]))

    def on_show_time_select(self, event):
        selected_index = self.show_time_listbox.curselection()
        if selected_index:
            self.selected_show_time.set(self.show_time_listbox.get(selected_index[0]))

    def confirm_selection(self):
        if not self.selected_screen.get():
            messagebox.showwarning("Screen Selection", "Please select a screen.")
            return

        if not self.selected_show_time.get():
            messagebox.showwarning("Show Time Selection", "Please select a show time.")
            return

        self.destroy()
        screen_selection_window = SeatBookingScreen(self.master, self.selected_movie, self.selected_screen.get(), self.selected_show_time.get(), self.user_page)

class SeatBookingScreen(tk.Toplevel):
    def __init__(self, root, selected_movie, selected_screen, selected_show_time, user_page):
        super().__init__(root)
        self.master = root
        root.withdraw()
        self.title("Seat Booking Screen")
        self.geometry("1000x1000")
        self.selected_movie = selected_movie
        self.selected_screen = selected_screen
        self.selected_show_time = selected_show_time
        self.user_page = user_page
        self.worker_seats = ["I1", "I2", "I3", "H1", "H2", "H3"]

        self.reserved_seats = self.load_reserved_seats()

        # Load movies and find the rating for the selected movie
        self.movies = self.load_movies()
        self.rating = self.get_movie_rating(self.selected_movie)

        # Initialize dictionaries to keep track of booked seats and their categories
        self.booked_seats = {}  # Store bookings as {seat: category}
        self.seat_buttons = {}
        self.seat_categories = {}

        # Define seat categories with prices based on the movie rating
        if self.rating > 7:
            self.seat_categories["Economy"] = {"price": 150, "seats": []}
            self.seat_categories["Premium"] = {"price": 250, "seats": []}
            self.seat_categories["VIP"] = {"price": 500, "seats": []}

        elif 5 <= self.rating <= 7:
            self.seat_categories["Economy"] = {"price": 250, "seats": []}
            self.seat_categories["Premium"] = {"price": 350, "seats": []}
            self.seat_categories["VIP"] = {"price": 600, "seats": []}

        else:
            self.seat_categories["Economy"] = {"price": 300, "seats": []}
            self.seat_categories["Premium"] = {"price": 400, "seats": []}
            self.seat_categories["VIP"] = {"price": 650, "seats": []}

        self.seating_frame = tk.Frame(self)
        self.seating_frame.pack()

        self.seats = []
        rows = 10
        cols = 10
        for row_idx in range(rows):
            seat_row = []
            for col_idx in range(cols):
                seat_id = f"{chr(65 + row_idx)}{col_idx + 1}"
                category = self.get_seat_category(row_idx)
                price = self.seat_categories[category]["price"]
                if seat_id in self.worker_seats:
                    seat_btn = tk.Button(self.seating_frame, text=f"{seat_id}\n(Rs.{price})", width=8, height=2,
                                         bg="blue", state="disabled")
                
                elif seat_id in self.reserved_seats:
                    seat_btn = tk.Button(self.seating_frame, text=f"{seat_id}\n(Rs.{price})", width=8, height=2,
                                         bg="gray", state="disabled")
                
                else:
                    seat_btn = tk.Button(self.seating_frame, text=f"{seat_id}\n(Rs.{price})", width=8, height=2,
                                         command=lambda r=row_idx, c=col_idx: self.toggle_seat(r, c))
                seat_row.append(seat_btn)
                seat_btn.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                self.seat_buttons[seat_id] = seat_btn  # Save reference to the button
            self.seats.append(seat_row)

        # Add a label indicating the direction of the movie screen
        screen_label = tk.Label(self, text="Movie Screen", font=("Arial", 14, "bold"), pady=10)
        screen_label.pack()

        # Add Confirm Booking buttons
        self.confirm_button = tk.Button(self, text="Confirm Seats", command=self.show_payment_window)
        self.confirm_button.pack(pady=10)
        
        self.food_button = tk.Button(self, text="Add Food", command=self.show_food_selection)
        self.food_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.destroy()
        self.user_page.deiconify()

    def load_reserved_seats(self):
        reserved_seats = {}
        reserved_seats_file = 'past_bookings.csv'
        if os.path.isfile(reserved_seats_file):
            with open(reserved_seats_file, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 3 and row[0] == self.selected_movie and row[3] == self.selected_screen and row[4] == self.selected_show_time:
                        seats = row[1].strip('"').split(', ')
                        for seat in seats:
                            reserved_seats[seat] = True
        else:
            messagebox.showerror("Error", "Reserved seats file not found.")
        return reserved_seats
   
    def load_movies(self):
        try:
            with open('movies.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

    def get_movie_rating(self, movie_name):
        for movie in self.movies:
            if movie['title'] == movie_name:
                return float(movie['rating'])
        return 0  # Default rating if movie not found

    def toggle_seat(self, row, col):
        seat_id = f"{chr(65 + row)}{col + 1}"
        if seat_id in self.reserved_seats:
            messagebox.showinfo("Reserved Seat", f"Seat {seat_id} is reserved and cannot be selected.")
        elif seat_id in self.booked_seats:
            category = self.booked_seats[seat_id]
            self.seat_categories[category]["seats"].remove(seat_id)
            self.seats[row][col].config(bg="SystemButtonFace")  # Deselect the seat
            del self.booked_seats[seat_id]
        else:
            category = self.get_seat_category(row)
            self.booked_seats[seat_id] = category
            self.seat_categories[category]["seats"].append(seat_id)
            self.seats[row][col].config(bg="red")  # Select the seat

    def get_seat_category(self, row):
        if row < 3:
            return "VIP"
        elif row > 2 and row < 8:
            return "Premium"
        else:
            return "Economy"

    def show_payment_window(self, food_total=0):
        total_seats = sum(len(details["seats"]) for details in self.seat_categories.values())
        total_cost = sum(self.seat_categories[cat]["price"] * len(self.seat_categories[cat]["seats"]) for cat in self.seat_categories)
        
        # Apply discount if more than 10 seats are booked
        if total_seats > 10:
            dis = 1
            discount = (0.2 * total_cost)
            final_total_cost = total_cost - discount
            grand_total = final_total_cost + food_total
        else:
            dis = 0
            grand_total = total_cost + food_total

        payment_window = tk.Toplevel(self)
        payment_window.title("Payment")
        payment_window.geometry("400x500")
        tk.Label(payment_window, text="Payment Summary", font=("Arial", 14)).pack(pady=10)
        for category, details in self.seat_categories.items():
            seat_list = ", ".join(details["seats"])
            tk.Label(payment_window, text=f"{category} Seats: {seat_list}").pack()
            tk.Label(payment_window, text=f"Total {category} Cost: Rs.{details['price'] * len(details['seats'])}").pack()
        if dis > 0:
            tk.Label(payment_window, text=f"Discount Applied: Rs.{discount}", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(payment_window, text=f"Food Total: Rs.{food_total}").pack(pady=10)
        tk.Label(payment_window, text=f"Grand Total: Rs.{grand_total}").pack(pady=10)
        tk.Button(payment_window, text="Pay Now", command=lambda: self.confirm_booking(grand_total, payment_window)).pack(pady=20)

    def show_food_selection(self):
        total_seats = sum(len(cat["seats"]) for cat in self.seat_categories.values())
        food_selection = FoodSelection(self, total_seats)
        self.wait_window(food_selection)
        if food_selection.final_total is not None:
            self.show_payment_window(food_selection.final_total)

    def confirm_booking(self, total_cost, payment_window):
        total_seats = [seat for cat in self.seat_categories.values() for seat in cat["seats"]]
        booking_details = {"movie": self.selected_movie, "seats": ", ".join(total_seats)}

        # Write booking details to CSV file
        with open('past_bookings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([booking_details['movie'], booking_details['seats'], int(total_cost), self.selected_screen, self.selected_show_time])

        messagebox.showinfo("Booking Confirmed", f"Your seats for {self.selected_movie} have been booked successfully!")

        # Close payment window and return to user page
        payment_window.destroy()
        self.destroy()
        self.user_page.deiconify()

class FoodSelection(tk.Toplevel):
    def __init__(self, master, total_seats):
        super().__init__(master)
        self.master = master
        self.total_seats = total_seats
        self.selected_items_count = 0
        self.final_total = None
        self.title("Food Selection")
        self.geometry("500x800")
        
        # Food options data
        self.food_data = {
            "Popcorn": {"Salty": {"Large": 250, "Medium": 170}, "Butter": {"Large": 250, "Medium": 170}, "Cheesy": {"Large": 250, "Medium": 170}},
            "Soft Drink": {"Pepsi": {"Large": 120, "Medium": 90}, "Cola": {"Large": 120, "Medium": 90}, "7up": {"Large": 120, "Medium": 90}},
            "Cheesy Nachos": 110,
            "Samosa": 50,
            "Sandwich": {"Cheese": 90, "Paneer": 100, "Chicken": 120},
            "Burger": {"Veg": 105, "Non-Veg": 125},
            "Pizza": {"Veg": 150, "Cheese": 180, "Chicken": 200}
        }

        # Dictionary to store selected items and their quantities
        self.selected_items = {}

        # Create Canvas and Scrollbar
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame to contain all widgets
        self.main_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.main_frame, anchor=tk.NW)

        # Create UI
        self.create_widgets()

        # Configure Canvas scrolling
        self.main_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def create_widgets(self):
        row = 0
        for item, options in self.food_data.items():
            if isinstance(options, dict):
                if item in ["Popcorn", "Soft Drink"]:
                    item_frame = tk.Frame(self.main_frame)
                    item_frame.grid(row=row, column=0, pady=5)

                    tk.Label(item_frame, text=item).pack(side=tk.LEFT)

                    variant_choice = tk.StringVar(value=next(iter(options)))
                    variant_dropdown = ttk.Combobox(item_frame, textvariable=variant_choice, values=list(options.keys()), state="readonly")
                    variant_dropdown.pack(side=tk.LEFT, padx=5)

                    size_choice = tk.StringVar(value="Medium" if "Medium" in options[variant_choice.get()] else next(iter(options[variant_choice.get()])))
                    size_dropdown = ttk.Combobox(item_frame, textvariable=size_choice, values=list(options[variant_choice.get()].keys()), state="readonly")
                    size_dropdown.pack(side=tk.LEFT, padx=5)

                    quantity_var = tk.IntVar(value=0)
                    tk.Button(item_frame, text="-", command=lambda q=quantity_var: self.decrease_quantity(q)).pack(side=tk.LEFT)
                    tk.Label(item_frame, textvariable=quantity_var).pack(side=tk.LEFT, padx=5)
                    tk.Button(item_frame, text="+", command=lambda q=quantity_var: self.increase_quantity(q)).pack(side=tk.LEFT)
                    tk.Button(item_frame, text="Add", command=lambda i=item, v=size_choice, p=options[variant_choice.get()], q=quantity_var: self.add_item(i, v.get(), p, q)).pack(side=tk.LEFT)

                    row += 1
                else:
                    for variant, prices in options.items():
                        variant_frame = tk.Frame(self.main_frame)
                        variant_frame.grid(row=row, column=0, pady=5)
                        tk.Label(variant_frame, text=f"{item} ({variant})").pack(side=tk.LEFT)

                        quantity_var = tk.IntVar(value=0)
                        tk.Button(variant_frame, text="-", command=lambda q=quantity_var: self.decrease_quantity(q)).pack(side=tk.LEFT)
                        tk.Label(variant_frame, textvariable=quantity_var).pack(side=tk.LEFT, padx=5)
                        tk.Button(variant_frame, text="+", command=lambda q=quantity_var: self.increase_quantity(q)).pack(side=tk.LEFT)
                        tk.Button(variant_frame, text="Add", command=lambda i=item, v=variant, p=prices, q=quantity_var: self.add_item(i, v, p, q)).pack(side=tk.LEFT)

                        row += 1
            else:
                item_frame = tk.Frame(self.main_frame)
                item_frame.grid(row=row, column=0, pady=5)
                tk.Label(item_frame, text=f"{item} (Rs.{options})").pack(side=tk.LEFT)

                quantity_var = tk.IntVar(value=0)
                tk.Button(item_frame, text="-", command=lambda q=quantity_var: self.decrease_quantity(q)).pack(side=tk.LEFT)
                tk.Label(item_frame, textvariable=quantity_var).pack(side=tk.LEFT, padx=5)
                tk.Button(item_frame, text="+", command=lambda q=quantity_var: self.increase_quantity(q)).pack(side=tk.LEFT)
                tk.Button(item_frame, text="Add", command=lambda i=item, p=options, q=quantity_var: self.add_item(i, None, p, q)).pack(side=tk.LEFT)

                row += 1

        # Total cost and summary display
        self.total_label = tk.Label(self.main_frame, text="Total: Rs.0")
        self.total_label.grid(row=row, column=0, pady=10)
        self.summary_label = tk.Label(self.main_frame, text="Selected items:")
        self.summary_label.grid(row=row + 1, column=0, pady=10)

        # Proceed to Payment Button
        tk.Button(self.main_frame, text="Proceed to Payment", command=self.proceed_to_payment).grid(row=row + 2, column=0, pady=10)

        self.back_button = tk.Button(self.main_frame, text="Back", command=self.go_back)
        self.back_button.grid(row=row + 3, column=0, pady=10)

    def go_back(self):
        self.destroy()
        self.master.deiconify()

    # Function to update the total cost
    def update_total(self):
        total = 0
        summary = []
        self.selected_items_count = 0
        for item, details in self.selected_items.items():
            if isinstance(details['price'], dict):
                total += details['price'][details['variant']] * details['quantity']
                summary.append(f"{details['quantity']} x {item} ({details['variant']} - Rs.{details['price'][details['variant']]})")
            else:
                total += details['price'] * details['quantity']
                summary.append(f"{details['quantity']} x {item} (Rs.{details['price']})")
            self.selected_items_count += details['quantity']
        self.total_label.config(text=f"Total: Rs.{total}")
        self.summary_label.config(text="Selected items:\n" + "\n".join(summary))

    # Function to handle item selection and quantity adjustment
    def add_item(self, item, variant, price, quantity_var):
        quantity = quantity_var.get()
        if quantity > 0:
            self.selected_items[item] = {'variant': variant, 'price': price, 'quantity': quantity}
        elif item in self.selected_items:
            del self.selected_items[item]
        self.update_total()

    # Function to increase quantity
    def increase_quantity(self, quantity_var):
        quantity_var.set(quantity_var.get() + 1)

    # Function to decrease quantity
    def decrease_quantity(self, quantity_var):
        if quantity_var.get() > 0:
            quantity_var.set(quantity_var.get() - 1)

    # Function to proceed to payment
    def proceed_to_payment(self):
        total_cost = int(self.total_label.cget("text").split("Rs.")[-1])
        seat_discount = self.total_seats * 50
        if self.selected_items_count > 5:
            seat_discount += 100
        grand_total = total_cost - seat_discount
        self.final_total = total_cost
        self.destroy()

class MovieBookingApp(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Movie Booking App")
        self.geometry("800x500")
        self.configure(bg="#14151a")
        self.movies = {}  # Initialize the movies dictionary here
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=800, height=500, bg="#14151a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.label = self.canvas.create_text(400, 50, text="Movies Available", font=("Helvetica", 20), fill="white")

        self.movie_listbox = tk.Listbox(self, font=("Helvetica", 14), width=50, height=10, bg="#14151a", fg="white")
        self.load_movies()
        self.movie_listbox.bind('<<ListboxSelect>>', self.display_movie_description)
        self.movie_listbox_window = self.canvas.create_window(400, 150, window=self.movie_listbox, anchor="center")

        self.movie_description_label = tk.Label(self, font=("Helvetica", 14), width=60, height=5, bg="#14151a", fg="white", wraplength=700, justify="left")
        self.movie_description_label_window = self.canvas.create_window(400, 300, window=self.movie_description_label, anchor="center")

        self.button_back = tk.Button(self, text="Back", font=("Helvetica", 14), command=self.back, bg="#aeaeae")
        self.button_back_window = self.canvas.create_window(400, 400, window=self.button_back, anchor="center")

    def load_movies(self):
        movies_file = 'movies.csv'
        if os.path.isfile(movies_file):
            with open(movies_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.movie_listbox.insert(tk.END, row['title'])
                    self.movies[row['title']] = {
                        'description': row['description'],
                        'cast': row['cast']
                    }
        else:
            messagebox.showerror("Error", "Movies file not found.")


    def display_movie_description(self, event):
        selected_movie = self.movie_listbox.get(self.movie_listbox.curselection())
        movie_info = self.movies.get(selected_movie, {"description": "Description not available.", "cast": "Cast not available."})
        
        description = movie_info['description']
        cast = movie_info['cast']
        
        self.movie_description_label.config(text=f"Description: {description}\nCast: {cast}")

    def back(self):
        if self.master is not None:
            self.destroy()  # Destroy the current window
            self.master.deiconify()  # Restore the parent window
        else:
            messagebox.showerror("Error", "Parent window not found.")

class BookingHistoryViewer:
    def __init__(self, master):
        self.master = master
        self.show_history()

    def show_history(self):
        try:
            with open('past_bookings.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames:
                    history_window = tk.Toplevel(self.master)
                    history_window.title("Booking History")
                    history_window.geometry("500x500")

                    tk.Label(history_window, text="Booking History", font=("Arial", 14)).pack(pady=10)
                    for row in reader:
                        tk.Label(history_window, text=f"Movie: {row['movie']}, Seats: {', '.join(row['seats'].split(';'))}").pack(pady=5)

                    # Add a back button
                    back_button = tk.Button(history_window, text="Back", command=history_window.destroy)
                    back_button.pack(pady=10)
                
                else:
                    messagebox.showinfo("History", "No booking history available.")
        
        except FileNotFoundError:
            messagebox.showerror("Error", "Booking history file not found.")

if __name__ == "__main__":
    app = TheaterApp()
    app.mainloop()
