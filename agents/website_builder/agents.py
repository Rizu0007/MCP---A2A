

from utilities.common.file_loader import load_instructions_file
from utilities.agents.llagent import LLagent

class WebsiteBuilderSimple:
      """
       A simple website builder agent that can create basic web pages 
       and is built using google's agent development framework.
       """
      def __init__(self):
          self.system_instruction = load_instructions_file('agents/website_builder/instructions.txt', default="You are a helpful website builder agent.")
          self.description = load_instructions_file('agents/website_builder/description.txt', default="A simple website builder agent.")
      
      def  _build_agent(self)->LLagent:
           return LLagent(
             
              name="website_builder_simple",
              model="gemini-2.5-flash",
              instruction=self.system_instruction,
              description=self.description,
           )
          
      
      
      
      
      
      
      
      
      
