hyperparams={"layers":3, "units":256,"dropout":0.2}
hyperparams= {key:value * 2 for key,value in hyperparams.items()}

print(hyperparams)

#conditional Transormation
hyperparams={"layers":3, "units":256,"dropout":0.2}

hyperparams= {key.upper():value for key,value in hyperparams.items() if value>0.2}
print(hyperparams)