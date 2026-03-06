import customtkinter as ctk
from Backend import Library, Member, Book
from tkinter import messagebox
#1 Main window setup

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("600x500")
app.title("Library Manager Pro")

title_lbl=ctk.CTkLabel(app,text="📚 Library Manager Pro",font=("Arial",26,"bold"))
title_lbl.pack(pady=15)

#2.Create tabs
tabs=ctk.CTkTabview(app,width=550,height=450)
tabs.pack(pady=10)

tabs.add("Dashboard")
tabs.add("Add Book")
tabs.add("Add Member")
tabs.add("Transactions")

my_library=Library()

#3. Dummy Functions
def ui_add_book():
    title=book_title_entry.get()
    author=book_author_entry.get()

    if title and author:
        result=my_library.add_book(title,author)
        messagebox.showinfo("Success",result)

        book_title_entry.delete(0,ctk.END)
        book_author_entry.delete(0,ctk.END)
    else:
        messagebox.showerror("Error","Please fill in all fields.")


def ui_add_member():
    name=member_name_entry.get()

    if name:
        result=my_library.add_member(name)
        messagebox.showinfo("Success",result)

        member_name_entry.delete(0,ctk.END)
    else:
        messagebox.showerror("Error","Please fill in the member name.")

def ui_issue_book():
    b_id=trans_book_id.get()

    if b_id:
        result=my_library.issue_book(b_id)
        if "Success" in result:
            transaction_status_lbl.configure(text=result,text_color="red")
            trans_book_id.delete(0,ctk.END)
        else:
            transaction_status_lbl.configure(text=result,text_color="red")
            trans_book_id.delete(0,ctk.END)
    else:
        transaction_status_lbl.configure(text="Please fill all the spaces",text_color="red")
        trans_book_id.delete(0,ctk.END)     
        

def ui_return_book():
    b_id=trans_book_id.get()

    if b_id:
        result=my_library.return_book(b_id)
        if "Success" in result:
            transaction_status_lbl.configure(text=result,text_color="red")
            trans_book_id.delete(0,ctk.END)
        else:
            transaction_status_lbl.configure(text="Please fill all the spaces",text_color="red")
            trans_book_id.delete(0,ctk.END)
    
    
    #4. Design dashboard tab

welcome_lbl=ctk.CTkLabel(tabs.tab("Dashboard"),text="Welcome to the library!👋",font=("Arial",24,"bold"))

def show_welcome():
    catalog_frame.pack_forget()
    back_button.pack_forget()

    welcome_lbl.configure(text="Welcome to the library!👋")
    sub_lbl.pack(pady=5)
    view_book_button.pack(pady=10)

sub_lbl=ctk.CTkLabel(tabs.tab("Dashboard"),text="Manage books,track members and process transactions.",text_color="gray",font=("Arial",14))

catalog_header=ctk.CTkScrollableFrame(tabs.tab("Dashboard"),fg_color="transparent",width=450,height=250)
back_btn=ctk.CTkButton(catalog_header,text="🔙back",width=60,fg_color="grey",hover_color="#555555",command=show_welcome)
back_btn.pack(side="left")

catalog_lbl=ctk.CTkLabel(catalog_header,text="📚Library Catalog",font=("Arial",18,"bold"))
catalog_lbl.pack(pady=10)

catalog_frame=ctk.CTkScrollableFrame(tabs.tab("Dashboard"),width=500,height=250)
for i in range(1,15):
    dummy_lbl=ctk.CTkLabel(catalog_frame,text=f"📕Book {i}: The Great Gatsby(ID: {100+i}-[AVAILABLE])",font=("Arial",14))
    dummy_lbl.pack(anchor="w",padx=5,pady=10)

def show_catalog():
    sub_lbl.pack_forget()
    welcome_lbl.pack_forget()
    view_book_button.pack_forget()

    catalog_header.pack(fill="x",padx=20,pady=10)
    catalog_frame.pack(pady=10)

    welcome_lbl.configure(text="📚Library Catalog")
    catalog_frame.pack(pady=10)
    back_btn.pack(anchor="w", padx=20,pady=(0,10))


view_book_button=ctk.CTkButton(tabs.tab("Dashboard"),text="📖 View all books",command=show_catalog,font=("Arial",16,"bold"),height=45)
back_button=ctk.CTkButton(tabs.tab("Dashboard"),text="🔙 Go Back",fg_color="gray",hover_color="#555555",command=show_welcome)

welcome_lbl.pack(pady=(40,5))
sub_lbl.pack(pady=(0,30))
view_book_button.pack(pady=10)

#5.Add book tab
ctk.CTkLabel(tabs.tab("Add Book"),text="Enter Book Details",font=("Arial",18,"bold")).pack(pady=10)
book_title_entry=ctk.CTkEntry(tabs.tab("Add Book"),placeholder_text="Book Title",width=250)
book_title_entry.pack(pady=10)

book_author_entry=ctk.CTkEntry(tabs.tab("Add Book"),placeholder_text="Author Name",width=250)
book_author_entry.pack(pady=10)

#book_id_entry=ctk.CTkEntry(tabs.tab("Add Book"),placeholder_text="Book ID",width=250)
#book_id_entry.pack(pady=10)

add_book_btn=ctk.CTkButton(tabs.tab("Add Book"),text="➕ Add Book",command=ui_add_book,font=("Arial",16,"bold"),height=45)
add_book_btn.pack(pady=20)

#6.Add member tab
ctk.CTkLabel(tabs.tab("Add Member"),text="Enter Member Details",font=("Arial",18,"bold")).pack(pady=10)
member_name_entry=ctk.CTkEntry(tabs.tab("Add Member"),placeholder_text="Member Name",width=250)
member_name_entry.pack(pady=10)

#member_id_entry=ctk.CTkEntry(tabs.tab("Add Member"),placeholder_text="Member ID",width=250)
#member_id_entry.pack(pady=10)

add_member_btn=ctk.CTkButton(tabs.tab("Add Member"),text="➕ Add Member",command=ui_add_member,font=("Arial",16,"bold"),height=45)
add_member_btn.pack(pady=20)

#7.Transactions tab
ctk.CTkLabel(tabs.tab("Transactions"),text="Issue or Return Books",font=("Arial",18,"bold")).pack(pady=10 )

trans_book_id=ctk.CTkEntry(tabs.tab("Transactions"),placeholder_text="Book ID",width=250)
trans_book_id.pack(pady=10)

#trans_member_id=ctk.CTkEntry(tabs.tab("Transactions"),fg_color="transparent",placeholder_text="member ID",width=250)
#trans_member_id.pack(pady=10)

btn_frame=ctk.CTkFrame(tabs.tab("Transactions"),fg_color="transparent")
btn_frame.pack(pady=10)

issue_btn=ctk.CTkButton(btn_frame,text="📗 Issue Book",fg_color="green",command=ui_issue_book,font=("Arial",16,"bold"),height=45)
issue_btn.pack(side="left", padx=10)

return_btn=ctk.CTkButton(btn_frame,text="📕 Return Book",fg_color="red",command=ui_return_book,font=("Arial",16,"bold"),height=45)
return_btn.pack(side="left", padx=10)

transaction_status_lbl=ctk.CTkLabel(tabs.tab("Transactions"),text="Waiting for transaction...",text_color="gray",font=("Arial",14))
transaction_status_lbl.pack(pady=10)

app.mainloop()