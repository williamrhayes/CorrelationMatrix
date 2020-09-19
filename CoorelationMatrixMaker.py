import os
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 6}) # Specify all fonts this size unless explicitly told otherwise


def main():
    path1 = 'D:/_UltraLearning/2020/9.2020/CoorelationMatrix/Data/WorldHappinessReport/'

    # For each year in our Data
    for file_name in os.listdir(path1):
        # Get the path for each of the csv files
        path = path1 + file_name

        # Generate the correlation matrix data
        corrMatrix = pd.read_csv(path).corr()

        # Create a mask to cover redundant parts
        # of the heat map
        mask = np.zeros_like(corrMatrix)
        mask[np.triu_indices_from(mask)] = True

        # Apply the mask
        with sn.axes_style('white'):
            fig, ax = plt.subplots(figsize=(10,10))
            ax = sn.heatmap(corrMatrix, annot=True,
                            mask=mask)

        # Add a title
        plt.title('Happiness Correlations, ' + file_name.replace('.csv', ''),
                  fontsize=12)

        # Display our plot
        plt.show()


main()

# References:
# https://datatofish.com/correlation-matrix-pandas/ (This made me a coorelation matrix VERY quickly!!)
# https://seaborn.pydata.org/generated/seaborn.heatmap.html (Used to cut off the mirror half of our correlation matrix)
# https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot (used to fit x and y lables into charts)
# https://www.kaggle.com/unsdsn/world-happiness (Happiness Data source)