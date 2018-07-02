import json
import matplotlib.pyplot as plt
import fire

def visualize(file):

    with open(file) as f:
        text = f.readlines()

    json_stats = [line[11:] for line in text if line[:10] == 'json_stats']

    losses = []
    iters = []
    accuracys = []

    for item in json_stats:
        data = json.loads(item)
        losses.append(data['loss'])
        iters.append(data['iter'])
        accuracys.append(data['accuracy_cls'])




    fig,(ax1,ax2) = plt.subplots(2,1,figsize=(16,10),sharex=True)

    ax1.plot(iters,losses,color='C1')
    ax1.set(xlabel='iter',ylabel='loss',title='Loss per iter:')


    ax2.plot(iters,accuracys,color='C4')
    ax2.set(xlabel='iter', ylabel='accuracy',title='Accuracy per iter:')
    plt.show()

if __name__ == '__main__':
    fire.Fire(visualize)
