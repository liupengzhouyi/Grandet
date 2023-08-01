#/bin/bash python3


from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl


class GenarationImage:
    
    
    def __init__(self) -> None:
         pass
    
    
    # def genaration_image(self, values: list, labels: list=None) -> None:

    #     x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    #     y = np.array([1, 4, 9, 16, 7, 11, 23, 18])

    #     plt.scatter(x, y)
    #     plt.show()

    @classmethod
    def genaration_month_image(cls, values: list, labels: list=None):
        
        means = values
        if labels is None:
            labels = range(len(values))
        ll = labels
        labels = []
        for i in ll:
            labels.append(i.replace('2023-', '').replace('2022-', '').replace('2021-', '').replace('2020-', ''))

        bar_width = 0.5
        bar_x = np.arange(len(labels))

        fig = plt.figure(figsize=(20, 5),tight_layout=True)

        ax1 = fig.add_subplot(111)
        bar1 = ax1.bar(x=bar_x, height=means, width=bar_width, color='green', tick_label=labels)
        for b in bar1:
                height = b.get_height()
                ax1.annotate('{}'.format(height),
                            xy=(b.get_x() + b.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            color='red',
                            ha='center',
                            va='bottom')

        plt.show()
    
# values= [11.30, 10.00, 38.60, 17.00, 46.08, 36.90, 27.72, -9]
# paly(valus=values)