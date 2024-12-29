from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the Flan-T5 Base tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# Define uncertain response keywords
uncertain_keywords = ["maybe", "unclear", "i don't know", "not sure", "possibly", "could be"]

def analyze_script(script):
    try:
        # Define chunk size within token limits
        chunk_size = 350  # Adjusted to ensure it fits within the token limit after tokenization
        # Split the script into chunks
        script_chunks = [script[i:i + chunk_size] for i in range(0, len(script), chunk_size)]
        
        # Define trigger categories
        trigger_categories = [
            "Violence",
            "Death",
            "Substance Use",
            "Gore",
            "Vomit",
            "Sexual Content",
            "Sexual Abuse",
            "Self-Harm",
            "Gun Use",
            "Animal Cruelty",
            "Mental Health Issues"
        ]
        
        # Initialize a set to store identified triggers
        identified_triggers = set()

        # Analyze each chunk separately
        for chunk in script_chunks:
            for category in trigger_categories:
                # Create a more specific and detailed prompt for the model to analyze each category
                if category == "Sexual Content":
                    prompt = f"Does the following text describe clear and explicit sexual activity, behavior, or inappropriate content? Only agree if you are very confident. Respond 'yes' or 'no':\n\nText: {chunk}\n"
                else:
                    prompt = f"Does the following text contain {category}? Respond 'yes' or 'no':\n\nText: {chunk}\n"

                # Tokenize the prompt
                inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

                # Generate the response with improved parameters
                outputs = model.generate(
                    **inputs, 
                    max_length=25, 
                    temperature=0.2,  # Lower temperature for more deterministic responses
                    num_beams=4,      # Decreased number of beams for better efficiency
                    early_stopping=True,
                    pad_token_id=tokenizer.eos_token_id
                )

                # Decode the response
                response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
                
                # Print the response for debugging
                print(f"Response for {category}: {response_text}")
                
                # Check if the response contains any of the uncertain keywords
                if any(uncertain_keyword in response_text.lower() for uncertain_keyword in uncertain_keywords):
                    print(f"Skipping {category} due to uncertainty: {response_text}")
                    continue  # Skip adding the trigger if the response is uncertain

                # Check if the response contains a positive indication of the category
                if "yes" in response_text.lower().strip():
                    identified_triggers.add(category)
        
        return list(identified_triggers)
    except Exception as e:
        return {"error": str(e)}