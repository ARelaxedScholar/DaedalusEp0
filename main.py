from google import genai
from pocketflow import Node, Flow
from utils import call_gemini

class ChatBotNode(Node):
    def prep(self, shared):
        user_message = input("You: ")    
        if "messages" not in shared:
            shared["messages"] = [shared["system_prompt"]] # list containing, the system prompt
        shared["messages"].append({"role": "user", "message": f"{user_message}"})
        
        if user_message.lower() == "exit":
            return None
        return shared["messages"]
        
    def exec(self, prep_res):
        llm_response = call_gemini(prep_res)
        print(f"Astro: {llm_response}")
        return llm_response
        
        
    def post(self, shared, prep_res, exec_res):
        if prep_res:
            shared["messages"].append({"role": "llm", "message": f"{exec_res}"})
            return "continue"
        else:
            return None

chatnode = ChatBotNode()
chatnode - "continue" >> chatnode
flow = Flow(start=chatnode)

if __name__ == "__main__":
    shared = {}
    shared["system_prompt"] = "You are a cool dude, doing cool things. You know you are the shit. Nobody can tell you otherwise."
    # Then run
    flow.run(shared)



