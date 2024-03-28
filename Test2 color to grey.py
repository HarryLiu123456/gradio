import gradio as gr
import cv2

def color2black(image):
    output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return output

interface = gr.Interface(fn=color2black, inputs="image", outputs="image")
interface.launch()

