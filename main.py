"""
Well tis the main file
"""

if __name__ == "__main__":
    from keras.models import model_from_json    
    #inicializar el modelo
    with open("model.json", "r") as model_file:
        model = model_from_json(model_file.read())
    #cargar los pesos de la LSTM
    model.load_weights("weights.h5")
