import gradio as gr

def sayhello(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=sayhello, inputs="text", outputs="text")
demo.launch()
