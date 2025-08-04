import gradio as gr
from search import search_questions  # Your existing search function

def chatbot_response(query):
    results = search_questions(query)
    if not results:
        return "I couldn't find any matching information."
    response = "I found these answers:\n\n"
    for i, result in enumerate(results, 1):
        response += f"{i}. Q: {result['question']}\n"
        response += f"   A: {result['answer']}\n"
        response += f"   (Confidence: {result['score']:.2f})\n\n"
    return response

# Create the interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask your healthcare question..."),
    outputs="text",
    title="Healthcare Chatbot",
    description="Ask questions about healthcare and get answers from our knowledge base"
)

iface.launch()