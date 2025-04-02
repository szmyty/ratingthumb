import gradio as gr
from gradio_ratingthumb import RatingThumb

def handle_feedback(value):
    return f"You selected: {value}"

with gr.Blocks() as demo:
    gr.Markdown("### RatingThumb Component Demo")

    rating = RatingThumb(
        icon="frontend/assets/search.svg"
    )

    output = gr.Textbox(label="Selected Feedback")

    # Wire up the click event
    rating.click(fn=handle_feedback, inputs=rating, outputs=output)

demo.launch()
