import customtkinter as ctk
app=ctk.CTk()
textbox = ctk.CTkTextbox(app)

textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
# get text from line 0 character 0 till the end
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end")  # delete all text
textbox.configure(state="disabled")  # configure textbox to be read-only
