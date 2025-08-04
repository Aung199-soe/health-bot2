from search import search_questions

print("Healthcare Chatbot (type 'exit' to quit)")
while True:
    query = input("\nYou: ")
    if query.lower() == 'exit':
        break
        
    results = search_questions(query)
    
    if not results:
        print("Bot: I couldn't find any matching information.")
    else:
        print(f"\nBot: I found {len(results)} relevant answers:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. Question: {result['question']}")
            print(f"Answer: {result['answer']}")
            print(f"Confidence: {result['score']:.2f}")