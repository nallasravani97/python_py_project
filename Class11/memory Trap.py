master_config = {"rate_limit": 100}

#dev_config=master_config

#dev_config["rate_limit"]=500
#print(master_config)

master_config = {"rate_limit": 100}
safe_config=master_config.copy()
safe_config["rate_limit"]=999
print(master_config)