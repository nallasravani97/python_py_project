llm_config = {"model" : "gpt_4",
            "context_window" : 128000,
              ("version","minor"):4
            }

print(llm_config)

llm_config = {"model" : "gpt_4",
            "context_window" : 128000,
              ("version","minor"):4,
              ["version","minor"]:2
            }