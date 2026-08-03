
# ! embedding model setting and capability

# change provider 
# provider install
# .env set contant variable
# provider name change
# change model name 

# ! extara
# check model capabilty
# multilingual
# document parse (pdf , image + text , text , documents  , database) 
# dimension
# ! LLM model setting and capability

# change provider 
# provider install
# .env set contant variable to = API_KEY
# provider name change
# change model name 

# ! extara
# check model capabilty
# multimodel support (vision model)
# structured output
# tool calling 
# built in tool like (web_serch , file_system)
# input (text , files , ) 

# ! file code structure

# import sys
# # Aapke logger file se components ko import kiya ja raha hai
# from src.ml.logger import log_info, log_error, log_warning, logger


# def process_agent_workflow() -> bool:
#     """
#     Core production workflow orchestrating Agent tasks and Machine Learning inference.
#     """
#     try:
#         log_info("Starting Agentic MLOps workflow execution...")
        
#         # --- APKI CORE LOGIC YAHAN AAYEGI ---
#         # Example: 
#         # data = qdrant_client.fetch_context()
#         # response = cohere_client.generate(prompt=data)
        
#         # Test warning simulation
#         log_warning("Resource utilization monitoring is approaching limits.")
        
#         log_info("Workflow transaction executed and recorded successfully.")
#         return True
        
#     except Exception as e:
#         # exc_info=True use karne se logger automatic complete traceback details 
#         # aapki running_logs.log file aur console dono mein push kar dega.
#         logger.error(f"Critical operational error occurred: {str(e)}", exc_info=True)
        
#         # Production systems mein errors ko chupayein nahi, hamesha raise karein
#         raise e 


# if __name__ == "__main__":
#     try:
#         process_agent_workflow()
#         sys.exit(0) # Success state code for CI/CD pipelines
        
#     except KeyboardInterrupt:
#         log_warning("Process execution manually terminated by user loop.")
#         sys.exit(0)
        
#     except Exception:
#         # Agar koi unexpected error aayega toh container/runner ko alerts bhejega
#         sys.exit(1) 


#  ! import sops

# built-in modules
# external modules
# custom modules