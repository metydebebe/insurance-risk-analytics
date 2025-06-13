# src/eda_utils.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_histogram(df: pd.DataFrame, column: str, bins=30, save_path=None):
    """
    Plot histogram for a numerical column.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_boxplot(df: pd.DataFrame, column: str, by=None, save_path=None):
    """
    Plot boxplot for a numerical column, optionally grouped by a categorical column.
    """
    plt.figure(figsize=(10, 6))
    if by:
        sns.boxplot(x=by, y=column, data=df)
        plt.title(f'{column} by {by}')
    else:
        sns.boxplot(y=df[column])
        plt.title(f'Boxplot of {column}')
    if save_path:
        plt.savefig(save_path)
    plt.show()


def calculate_loss_ratio(df: pd.DataFrame) -> pd.Series:
    """
    Calculate Loss Ratio = TotalClaims / TotalPremium
    """
    return df['TotalClaims'] / df['TotalPremium']


def plot_correlation_matrix(df: pd.DataFrame, columns: list, save_path=None):
    """
    Plot correlation heatmap for specified columns.
    """
    corr = df[columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    if save_path:
        plt.savefig(save_path)
    plt.show()
