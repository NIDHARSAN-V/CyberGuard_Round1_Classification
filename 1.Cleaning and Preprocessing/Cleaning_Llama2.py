from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from deep_translator import GoogleTranslator

# Initialize the Ollama LLM
llm = Ollama(model='llama2')

def start(question):
    try: 
        print(f"Your input: {question}\n")
        
        # Define the prompt template
        prompt = PromptTemplate(
            input_variables=["question"],
            template="""You are an expert at preprocessing CSV data. Your task is to correct sentence formation. 
                        Even if the content is large, make it short. The goal is to create a concise sentence 
                        that retains the main content. All data is related to a cybercrime report."""
        )
        
        # Create the LLM chain and get the response
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(question=question)
        
        # Clean up the response by removing newlines
        response = response.replace("\n", "").strip()
        return response
    
    except Exception as e:
        raise RuntimeError(f"Failed to get response: {str(e)}")

def translate_to_english(text):
    try:
        # Translate the text to English
        translation = GoogleTranslator(source='auto', target='en').translate(text)
        return translation
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

if __name__ == "__main__":
    input_text = """RapeGang Rape RGRSexually Abusive Content,,Sir namaskar  mein Ranjit Kumar PatraPaise nehi the tho sir kuch din pehele online loan aap Credit pearl loan aap se money loan kiya thalekin sir  loan bolke jub  loan diye tho mein turant return kar diya thalekin din baad whats app pe message aya payment karomein bola  diye the aap mein wo de diyawo gali diye tho  v return kar diyafir v message karke bolte hai full payment karo half payment nehi chalegarape case mein daldenge etcFake or illigal se contact number v hack kar dete haibol rahehai sab ko message karenge ye rapist hai bolke sirpls sir small ammount ke liye goggle play store se loan apply kiya thaFake loan aap v hai socha nehi thapls sir request kar rahahun action lo Sir  mera number  hai jo v proof chahiye dunga Sir"""
    
    # First, process the input text with LLM to preprocess
    processed_text = start(input_text)
    print(f"Processed Output: {processed_text}")
    
    # Optionally, translate it to English if necessary
    translated_text = translate_to_english(processed_text)
    if translated_text:
        print(f"Translated Output: {translated_text}")
