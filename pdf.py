import matplotlib.pyplot as plt
from numpy import mean, std
from scipy.stats import norm
import pandas as pd

# read one series from xlsx file
# and convert ndarray
def read_series(file_path, column):    
    df = pd.read_excel(file_path)
    data = df[column].to_numpy()
    return data

# get PDF of data
def get_PDF(data):
    data_mean = mean(data)
    data_std = std(data)
    dist = norm(data_mean, data_std)
    values = [value for value in range(min(data), max(data))]
    pdf = [dist.pdf(value) for value in values]
    return pdf, values

# get CDF of data
def get_CDF(data):
    data_mean = mean(data)
    data_std = std(data)
    dist = norm(data_mean, data_std)
    values = [value for value in range(min(data), max(data))]
    cdf = [dist.cdf(value) for value in values]
    return cdf, values

# def plot values
def plot_data(probs, values, title, save_name = None, save = False):
    plt.title(title)
    plt.plot(values, probs)
    if save:
        plt.savefig(save_name)
    plt.show()

# read data
l_max_data = read_series("L_max.xlsx", "L_MAX")
l_min_data = read_series("L_min.xlsx", "L_MIN")

# get pdf and cdf
l_max_pdf, values = get_PDF(l_max_data)
plot_data(l_max_pdf, values, "L_MAX PDF Graph")
l_max_cdf, values = get_CDF(l_max_data)
plot_data(l_max_cdf, values, "L_MAX CDF Graph")
l_min_pdf, values = get_PDF(l_min_data)
plot_data(l_min_pdf, values, "L_MIN PDF Graph")
l_min_cdf, values = get_CDF(l_min_data)
plot_data(l_min_cdf, values, "L_MIN CDF Graph")

