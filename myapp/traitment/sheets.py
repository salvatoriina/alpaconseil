def get_columns(df,column):
    result=[]
    if column in df.columns:
      index=df.columns.get_loc(column)
      for i in df.index:
        line=str(df.iloc[i,index])
        line=line.split("|")
        for j in line:
          if not j in result :
            result.append(j)
          else:
            continue
    result.reverse()
    if "nan" in result:
          result.remove("nan")
    return result

def get_copy(df,column):
  dataf=df[["Type d'objet touristique",column]]
  new_df=dataf.copy()
  return new_df


def insert_columns(df,column,liste):
  index=df.columns.get_loc(column)
  for i in liste:
    df.insert(index+1,column=column+"_"+i,value="")

def completing_columns(df,column,columns):
  index=df.columns.get_loc(column)
  for i in df.index:
    line=str(df.iloc[i,index])
    line=line.split("|")
    if "nan" in line:
          line.remove("nan")
    for c in columns:
          if c in line:
                df.loc[i,column+"_"+c]="Oui"
          else:
                df.loc[i,column+"_"+c]="Vide"

      

def sheet(df):
    colonnes_sheet=["Type d'objet touristique","Services","Équipements","Activités sur place","Types de clientèle","Conforts","Labels","Label"]
    l=[]
    for c in colonnes_sheet:
      if c in df.columns:
        l.append(df.columns.get_loc(c))
    l.sort()

    old_df=df.iloc[:,l[0]:l[-1]+1]
    new_df=old_df.copy()
    all_cols=new_df.columns
    for c in all_cols:
      if c not in colonnes_sheet:
        del new_df[c]
    colonnes_sheet_final=["Services","Équipements","Activités sur place","Types de clientèle","Conforts","Labels","Label"]
    for c in colonnes_sheet_final:
      if c in df.columns:
        col=get_columns(new_df,c)
        completing_columns(new_df,c,col)
    return new_df