import tensorflow as tf
from tensorflow.keras.applications import InceptionV3, MobileNetV3Small, DenseNet121, EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model


def build_model(model_name, num_classes):
    
    if model_name == "InceptionV3":
        base_model = InceptionV3(weights="imagenet", include_top=False)

    elif model_name == "MobileNetV3":
        base_model = MobileNetV3Small(weights="imagenet", include_top=False)

    elif model_name == "DenseNet121":
        base_model = DenseNet121(weights="imagenet", include_top=False)

    elif model_name == "EfficientNetB0":
        base_model = EfficientNetB0(weights="imagenet", include_top=False)

    else:
        raise ValueError("Unknown model")

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    predictions = Dense(num_classes, activation="softmax")(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    return model
