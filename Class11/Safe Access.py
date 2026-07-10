llm_config = {"model" : "gpt_4",
            "context_window" : 128000,
              ("version","minor"):4
            }



print(llm_config.get("api_key","key Missing"))

