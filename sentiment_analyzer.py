# A simple sentiment or intent analyzer dictionary
positive_words = ["good", "great", "awesome", "happy", "love", "fantastic"]
negative_words = ["bad", "sad", "awful", "hate", "terrible", "school"] # (relatable based on your test1.py!)

def analyze_text():
    print("AI Text Analyzer Initialized. Type a sentence to analyze (or type 'quit'):")
    
    while True:
        user_input = input("\nEnter text: ").lower()
        
        if user_input == "quit":
            print("Exiting analyzer. Goodbye!")
            break
            
        # Split sentence into a list of words
        words = user_input.split()
        
        pos_count = 0
        neg_count = 0
        
        # Loop through words and check against our data lists
        for word in words:
            if word in positive_words:
                pos_count += 1
            elif word in negative_words:
                neg_count += 1
                
        # Simple decision logic (Rule-based AI output)
        if pos_count > neg_count:
            print("AI Analysis: This text has a POSITIVE tone.")
        elif neg_count > pos_count:
            print("AI Analysis: This text has a NEGATIVE tone.")
        else:
            print("AI Analysis: Neutral or unclear tone.")

if __name__ == "__main__":
    analyze_text()