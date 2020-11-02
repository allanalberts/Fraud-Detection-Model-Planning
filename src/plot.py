import helpers as h
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.ticker as mtick
import matplotlib.gridspec as gs


def plot_pval_for_model(ax, grp1, grp2, Features, title):
    '''
        Prints individual plot of p-values for each feature.

        ARGS:
            ax - axis to print on
            grp1 - pandas dataframe containing sample of
                   dataset for ttest comparison
            grp2 - pandas dataframe containing sample of
                   dataset for ttest comparison
            Features - features to plot
            title - plot title

        Return:
            ax - axis with plot
    '''
    df = h.ttest(grp1, grp2, Features)
    y = df['p_val']
    ax.bar(Features, y)
    ax.set_ylim(0, 0.05)
    ax.set_ylabel("p-value")
    ax.set_xlabel("Features")
    ax.set_title(title)


def plot_pval_all(data, amount_threshold):
    '''
        Prints multiple plots of p-values for each feature

        ARGS:
            data - pandas dataframe containing dataset
            amount_threshold - dollar amount for segmenting comparison groups

        Return:
            None
    '''
    fig, axs = plt.subplots(2, 1, figsize=(14, 4))
    grp1 = data[(data['Class'] == 1) & (data['Amount'] <= amount_threshold)]
    grp2 = data[(data['Class'] == 0) & (data['Amount'] <= amount_threshold)]
    title = f'Feature p-value (fraud vs. non-fraud) for amount <= ${amount_threshold}'
    plot_pval_for_model(axs[0], grp1, grp2, Features, title)

    grp3 = data[(data['Class'] == 1) & (data['Amount'] > amount_threshold)]
    grp4 = data[(data['Class'] == 0) & (data['Amount'] > amount_threshold)]
    title = f'Feature p-value (fraud vs. non-fraud) for amount > ${amount_threshold}'
    plot_pval_for_model(axs[1], grp3, grp4, Features, title)

    plt.tight_layout()
    fig.savefig("../img/features_pval.png")


def plot_dataset_overview(data):
    '''
        Creates a timeseries image of the dataset showing
        fraud and legitimate transaction trends

        ARGS:
            data - pandas dataframe

        Return:
            None
    '''
    trends = data[['Time', 'Amount', 'Class']].copy()
    trends['TimeSeries'] = pd.to_datetime(trends.Time, unit='s', origin='2013-09-01')
    trends.set_index('TimeSeries', drop=False, inplace=True)

    fraud = trends[(trends.Class == 1)][['Amount']].resample('H').count().dropna()
    fraud.columns = ['Trans_cnt']
    legit = trends[(trends.Class == 0)][['Amount']].resample('H').count().dropna()
    legit.columns = ['Trans_cnt']

    fig, ax = plt.subplots(figsize=(12, 4))
    fraud['Trans_cnt'].plot(color='r', kind='area', alpha=0.5, label='Fraud Transactions')
    legit['Trans_cnt'].plot(secondary_y=True, color='b', label='Sales Transactions')
    ax.set_ylabel('Fraud Count', color='r')
    ax.tick_params(axis='y', colors='red')
    plt.ylabel('Sales Count', color='b')
    plt.yticks(color='b')
    plt.axvline(x='2013-09-02 00:00:00', color='black', linestyle='dashed')
    plt.legend(frameon=False, loc='upper right')
    plt.title('Transaction Counts by hour', color='black')
    plt.savefig('intro_fig.png')


def graph_amount_cdf(ax, x, y1, y2, ymax):
    '''
        Creates plot representing the cdf of the fraud amounts

        ARGS:
            ax - plot axis
            x - list of features names to plot against
            y1 - list of cummulative amounts for fraud transactions
            y2 - list containing cdf values for fraud transactions
            ymax - the upper limit for y axis on plot

        Return:
           ax - plot axis
    '''

    percent = ticker.FormatStrFormatter('%1.0f')
    currency = mtick.StrMethodFormatter('${x:,.0f}')

    ax.plot(x, y1, color='red', label="Cummulative Fraud Loss")
    ax.xaxis.set_major_formatter(currency)
    ax.set_xlabel("Transaction Amount")
    ax.yaxis.set_major_formatter(currency)
    ax.set_ylabel("Cummulative Fraud Losses", c="r")
    ax.tick_params(axis='y', colors='red')

    ax.fill_between(np.arange(0, 100, 1), 0, ymax, facecolor='lightgreen')

    ax.set_xlim(0, right=None)
    ax.set_ylim(0, ymax)
    ax_2 = ax.twinx()
    ax_2.plot(x, y2, color='blue', label="Percent of Fraud Transactions")
    ax_2.set_ylabel("Percent of Fraud Transactions", color="blue")
    ax_2.yaxis.set_major_formatter(percent)
    ax_2.tick_params(axis='y', colors='blue')
    ax_2.set_ylim(0, 100)

    plt.title("Cummulative Fraud Losses and Transactions", fontsize=20)
    plt.axvline(x=100, color='green', linestyle='dashed', linewidth=1, label='$100')
    plt.legend(loc='lower center', frameon=False)
    plt.tight_layout()


def amount_cdf_data(data):
    '''
        Creates 3 lists used for plotting fraud eda chart

        ARGS:
            data -> pandas df

        Return:
            x - list of features names to plot against
            y1 - list of cummulative amounts for fraud transactions
            y2 - list of cdf values for fraud transactions
    '''
    max_amt = data['Amount'].max()
    transaction_cnt = data['Amount'].count()
    x = [n for n in range(1, int(max_amt), int(max_amt/100))]
    y1 = []
    y2 = []
    for n in range(102):
        y1.append(data[data['Amount'] < (.01*n*max_amt)]['Amount'].sum())
        y2.append(((data[data['Amount'] < (.01*n*max_amt)]['Amount'].count())/transaction_cnt)*100)
    ymax = np.max(y1)
    return x, y1, y2, ymax


def graph_amounts_frequency(ax, data, xlimit):
    '''
        Creates plots showing frequency of fraud at different transaction amounts

        ARGS:
            ax - plot axis
            y2 - list of cdf values to plot
            data - pandas df
            xlimit - x-axis graph upper limit

        Return:
            ax - axis with plot
    '''
    transaction_cnt = data['Amount'].count()
    y2 = []
    for n in range(102):
        y2.append(((data[data['Amount'] < (.01*n*xlimit)]['Amount'].count())/transaction_cnt)*100)

    gr_data = data[data['Class'] == 1].copy()
    gr_data[gr_data['Amount'] < xlimit]['Amount'].hist(ax=ax, bins=100, color='red', alpha=0.7)
    ax.set_title("Frequency of Fraud by Transaction Dollar Amount (0-100)", fontsize=20)
    ax.set_xlabel('Fraud Transaction Amount')
    ax_2 = ax.twinx()
    ax_2.plot(y2)
    currency = mtick.StrMethodFormatter('${x:,.0f}')
    ax.xaxis.set_major_formatter(currency)
    ax.set_ylabel('Transactions')
    ax.set_xlim(-1, 101)
    ax.set_facecolor('lightgreen')


def plot_fraud_amount_eda(data, gs):
    '''
        Creates image with multiple plots for Fraud Amount EDA Visualatioin

        ARGS:
            data - pandas df
            gs - instantiated Gridspec

        Return:
            None
    '''
    df_fraud = data[data['Class'] == 1]
    df_legit = data[data['Class'] == 0]

    fig = plt.figure(figsize=(20, 6))
    ax1 = fig.add_subplot(gs[0:-1])

    x, y1, y2, ymax = amount_cdf_data(df_fraud)
    graph_amount_cdf(ax1, x, y1, y2, ymax)

    ax2 = fig.add_subplot(gs[1:])
    graph_amounts_frequency(ax2, data, xlimit=100)

    plt.tight_layout()
    fig.savefig("../img/AmountPlots.png")


if __name__ == '__main__':
    data, Features = h.load_data("../data/creditcard.csv")

    # create p-value comparison plot: features_pval.png
    plot_pval_all(data, amount_threshold=1.00)

    # create the fraud amount eda charts: AmountPlots.png
    gs = gs.GridSpec(1, 2)
    plot_fraud_amount_eda(data, gs)

    # create plot of dataset overview
    plot_dataset_overview(data)
