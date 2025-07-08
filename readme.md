This project is a smart assistant for plant health. Upload a leaf image, and it tells you whether your plant is healthy or infected — and if infected, which disease it has. Then it takes things a step further. It opens up a conversation with BotaniQ (powered by Gemini ), who explains the disease, offers recovery tips, and tells you how to prevent it in the future.
 
## Model Architecture
At its heart, there's a custom-built Convolutional Neural Network that powers the prediction. It includes:

5 convolutional blocks with increasing filter sizes from 32 → 256

MaxPooling layers for spatial reduction after every 2 conv layers

A fully connected layer with 1024 neurons

Final output layer with 38 classes (representing 38 types of plant leaf categories)

With over 17 million parameters, this model was trained using the Adam optimizer and categorical cross-entropy loss, achieving ~90% accuracy on the validation set.

## AI Intregation
But the real power unfolds after prediction.
Once the disease is identified (or the leaf is healthy), BotaniQ joins in. It’s not just an info dump — it’s a conversation. BotaniQ behaves like a virtual botanist, giving you a breakdown of what the disease means, how to treat it, and what steps to take to prevent future infections. The assistant adapts its response based on the exact diagnosis — be it Tomato Early Blight, Potato Leaf Curl, or even a healthy leaf needing just a pat on the back.

The front end is powered by Streamlit — a clean, responsive UI where users can:

Upload images

View prediction results

Interact with BotaniQ

Everything runs through a modular FastAPI backend — one endpoint for prediction, one for BotaniQ responses, keeping things clean and maintainable.

Setup is straightforward: install the dependencies, load the model, and provide your Gemini API key — BotaniQ takes care of the rest.

This isn't just a classifier — it's a plant health companion.

It listens. It diagnoses. It explains.
And it does all of this with a single image.

## Dataset Source
The model was trained on a publicly available dataset by:
J. Arun Pandian and Geetharamani Gopal (2019),
“Identification of Plant Leaf Diseases Using a 9-layer Deep Convolutional Neural Network”,
Published on Mendeley Data DOI: 10.17632/tywbtsjrjv.1