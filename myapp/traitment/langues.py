def add_langue(df,column,columns):
      if column in df.columns:
        ind=df.columns.get_loc(column)
        for i in df.index:
          line=str(df.iloc[i,ind])
          line_split=line.split("|")
          for c in columns:
             if c in line_split:
              df.loc[i,column+"_"+c]="Oui"
             else:
               df.loc[i,column+"_"+c]="Vide"
