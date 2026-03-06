import tensorflow as tf
from model import build_model


def train_model(model_name, train_data, val_data, num_classes):

    model = build_model(model_name, num_classes)

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    history = model.fit(
        train_data,
        validation_data=val_data,
        epochs=10
    )

    return model, history
