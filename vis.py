def visualize_data(file):
    from pymysql import connect
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.feature_selection import SelectKBest, f_classif
    import warnings
    warnings.filterwarnings("ignore")
    import pandas as pd
    data=connect(host="localhost",user="root",password="@Harini123",database="loan")
    query=f"select * from {file};"
    df=pd.read_sql(query,data)
    data.close()

    
    sns.countplot(x = df[" loan_status"])
    plt.show()
    
    sns.histplot(df[' loan_amount'])
    plt.show()
    
    sns.distplot(df[' income_annum'])
    plt.show()
    
    counts=df[' loan_term'].value_counts()
    plt.pie(counts,labels=counts.index,autopct='%1.1f%%')
    plt.title('piechart of loan term')
    plt.show()
    
    g = df[df[' loan_status']==' Approved'].groupby(' cibil_score')[' loan_status'].count().reset_index()
    sns.barplot(y=' cibil_score', x=' loan_status', data=g)
    plt.xlabel('Number of approves')
    plt.ylabel('cibil score')
    plt.show()

    
    numeric_col=df.select_dtypes(include=["int","float"])
    correlation_matrix=numeric_col.corr()
    sns.heatmap(correlation_matrix,annot=True,cmap='Blues')
    plt.title('correlation Heatmap')
    plt.show()
