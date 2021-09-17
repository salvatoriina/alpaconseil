def remove_cs(line):
  line=str(line)
  line=line.replace("\n","").replace('"',"").replace("{","").replace("}","").replace("'","").replace(" ","")
  lis=line.split(",")
  return lis
def get_columns_fairguest(df,column):
  result=[]
  if column in df.columns:
    index=df.columns.get_loc(column)
    for i in df.index:
      line=df.iloc[i,index]
      new_line=remove_cs(line)
      for i in new_line:
        ret=i.split(":",1)[0]
        if not ret in result :
          result.append(ret)
        else:
          continue
  return result

def md_fairguest(df,column):
      if column in df.columns:
        index=df.columns.get_loc(column)
        for i in df.index:
            line=df.iloc[i,index]
            if not (line != line):

                line=remove_cs(line)
                for l in line:
                    key=l.split(":",1)[0]
                    value=l.split(":",1)[-1]
                    df.loc[i,column+"_"+key]=value
            else:
                continue
def convert_to_float(df):
  column="Métadonnées - fairguest_note"
  if column in df.columns:
    for i in df.index:
      df.loc[i,column]=float(df.loc[i,column])