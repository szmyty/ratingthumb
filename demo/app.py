
import gradio as gr
from gradio_ratingthumb import RatingThumb


example = RatingThumb().example_value()

demo = gr.Interface(
    lambda x:x,
    RatingThumb(),  # interactive version of your component
    RatingThumb(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
