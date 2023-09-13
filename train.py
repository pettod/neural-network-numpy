import matplotlib.pyplot as plt
import numpy as np

from loss_functions import MSE_Loss
from model import Model
from optimizers import Gradient_Decent


def main():
    input = np.random.uniform(-0.5, 0.5, 4)
    ground_truth = np.array(1)

    loss_function = MSE_Loss()
    model = Model(input.shape)
    learning_rate = 0.01
    optimizer = Gradient_Decent(learning_rate, model)

    losses = []

    # Train
    epochs = 20
    for epoch in range(epochs):
        prediction = model(input)
        loss = loss_function(prediction, ground_truth)
        losses.append(loss)
        print(model.model[0].weights, prediction)
        model.zero_grad()
        model.backward(loss_function)
        optimizer.step()
    print()
    print(prediction, ground_truth)

    plt.plot(losses)
    plt.show()


main()
