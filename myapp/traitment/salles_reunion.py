def create_column_sr(df,col,new_col):
    if col in df.columns:
      index=df.columns.get_loc(col)
      if not col+"_"+new_col in df.columns:
        df.insert(index+1,column=col+"_"+new_col,value="NaN")
      


def insert_column_sr(df,col,new_col):
    if col in df.columns:
      ind=df.columns.get_loc(col)
      for i in df.index:
        line=str(df.iloc[i,ind])
        line=line.split("¤")
        for new_line in line:
          if "Capacité maximum" in new_line:
            value=new_line.split(":",1)[1]
            df.loc[i,col+"_"+new_col]=value
            break