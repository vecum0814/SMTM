#%%
import FinanceDataReader as fdr
df_krx = fdr.StockListing('KRX')


df = fdr.DataReader('001250', '2020')
print(df.head(10))
df['Close'].plot()


# %%
