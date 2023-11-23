import openai
from my_key import my_api_key
openai.api_key = my_api_key

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

import tkinter as tk

def create_multi_line_input_with_placeholder(master, placeholder):
    def clear_placeholder(event):
        if input_widget.get("1.0", "end-1c") == placeholder:
            input_widget.delete("1.0", "end")
            input_widget["fg"] = default_fg_color

    def set_placeholder(event=None):
        if not input_widget.get("1.0", "end-1c"):
            input_widget.insert("1.0", placeholder)
            input_widget["fg"] = placeholder_color

    input_widget = tk.Text(master, height=3)
    input_widget.placeholder = placeholder
    input_widget.placeholder_color = "grey"
    input_widget.default_fg_color = input_widget["fg"]
    placeholder_color = "grey"
    default_fg_color = input_widget["fg"]
    input_widget.bind("<FocusIn>", clear_placeholder)
    input_widget.bind("<FocusOut>", set_placeholder)
    set_placeholder()
    return input_widget

def create_app(master):
    def show_answer():
        message = message_input.get("1.0", "end-1c")
        answer_label.insert("end", "\n\n" + "user: " + message)
        clear_message()
        answer_question(message)

    message_label = tk.Label(master, text="Write your message:")
    message_label.pack()

    message_input = create_multi_line_input_with_placeholder(master, "Type your message here")
    message_input.pack()

    submit_button = tk.Button(master, text="Submit", command=show_answer)
    submit_button.pack()

    answer_label = tk.Text(root, wrap="word")
    answer_label.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, command=answer_label.yview)
    scrollbar.pack(side="right", fill="y")
    answer_label.configure(yscrollcommand=scrollbar.set)

    def answer_question(message):
        messages.append({"role": "user", "content": message},)
        chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        result = chat.choices[0].message.content
        answer_label.insert("end", "\n" + "ChatGPT: " + result)

    def clear_message():
        last_index = message_input.index(tk.END)
        message_input.delete("1.0", last_index)


root = tk.Tk()
create_app(root)
root.mainloop()
        


