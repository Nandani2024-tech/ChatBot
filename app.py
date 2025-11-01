import os
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "microsoft/DialoGPT-medium")
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

# Initialize Flask
app = Flask(__name__)

# Load model + tokenizer once
print(f"✅ Loading model: {MODEL_NAME}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please say something!"})

    try:
        # Encode user message and generate reply
        input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
        output = model.generate(
            input_ids,
            max_length=150,
            pad_token_id=tokenizer.eos_token_id,
            temperature=0.7,
            top_p=0.9
        )

        reply = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return jsonify({"reply": reply.strip()})

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"reply": f"Error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)
