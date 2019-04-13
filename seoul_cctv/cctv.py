import pandas as pd
import xlrd
import numpy as np

ctx='../data/'
filename=ctx+'CCTV_in_Seoul.csv'
df_cctv=pd.read_csv(filename,encoding='UTF-8')
#print(seoul_cctv)
seoul_cctv_idx=df_cctv.columns
print(seoul_cctv_idx)
df_cctv.rename(columns={df_cctv.columns[0]:'구별'},inplace=True)
df_pop = pd.read_excel(ctx+"population_in_Seoul.xls",
                            encoding='UTF-8',header = 2, usecols='B,D,G,J,N' )

df_pop.rename(columns={df_pop.columns[0] : '구별',
                    df_pop.columns[1] : '인구수',
                    df_pop.columns[2] : '한국인',
                    df_pop.columns[3] : '외국인',
                    df_pop.columns[4] : '고령자' }, inplace=True)

df_cctv.sort_values(by='소계', ascending=True).head(5)
df_pop.drop([0], inplace=True)
df_pop['구별'].unique()
df_pop.drop([26],inplace=True) # NaN 있는 행 삭제

df_pop['외국인비율']=df_pop['외국인']/df_pop['인구수']*100
df_pop['고령자비율']=df_pop['고령자']/df_pop['인구수']*100

df_cctv.drop(["2013년도 이전","2014년","2015년","2016년"],1,inplace=True) #1은 열을 지우라는 의미
df_cctv_pop=pd.merge(df_cctv,df_pop,on='구별')
df_cctv_pop.set_index('구별',inplace=True)
cor1=np.corrcoef(df_cctv_pop['고령자비율'],df_cctv_pop['소계'])
cor2=np.corrcoef(df_cctv_pop['외국인비율'],df_cctv_pop['소계'])
print('고령자비율 상관계수 {} \n 외국인비율 상관계수 {}'.format(cor1,cor2))

df_cctv_pop.to_csv(ctx+'cctv_pop.csv')


#google map api: AIzaSyD_JQpVdO1C6rjYO2xH_eTtc-YzNV4_0m4