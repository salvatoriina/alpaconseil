def get_columns_mc(df,column):
  if column in df.columns:
    list_final=[]
    if column=="Moyens de communication (Standard)":
        column="Moyens de communications"          
    ind=df.columns.get_loc(column)
    for i in df.index:
      line=df.iloc[i,ind]
      line=str(line)
      line_split=line.split("|")
      for i in line_split:
        new_line=i.split(":",1)[0]
        if not new_line in list_final:
          list_final.append(new_line)
        else:
          continue
    
    return list_final

def add_columns_mc(df,column):
  if column in df.columns:
    ind=df.columns.get_loc(column)
    for i in df.index:
      line=str(df.iloc[i,ind])
      line_split=line.split("|")
      for c in line_split:
        key=c.split(":",1)[0]
        value=c.split(":",1)[-1]
        df.loc[i,column+"_"+key]=value