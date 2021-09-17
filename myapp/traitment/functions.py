from geopy.geocoders import Nominatim
import geocoder

def create_column(df,col,new_columns):
      if col in df.columns:
        new_columns.reverse()
        c=df.columns.get_loc(col)
        for i in new_columns:
          if not col+"_"+i in df.columns:
            df.insert(c+1,column=col+"_"+i,value="")
          else: 
            continue


def collect_data(df,column):
    l=[]
    if column in df.columns:
      for i in df.index:
        line=str(df.at[i,column])
        lis=line.split("|")
        if "nan" in lis:
              lis.remove("nan")
        for j in lis:
          if not j in l:
           l.append(j)
          else:
            continue
    return l


def categorie(df,column):
  if column in df.columns:
    ic=df.columns.get_loc("Catégories")
    df.insert(ic+1,column="Nouvelle catégories",value="NaN")
    for i in df.index:
      line=str(df.loc[i,"Catégories"])
      if line=="":
            df.loc[i,"Nouvelle catégories"]="Vide"
      else:
        line=line.split("|")
        df.loc[i,"Nouvelle catégories"]=line[0]
  else:
       return None


def longitude_latitude(df):
      long="Longitude"
      lat="Latitude"
      if long in df.columns and lat in df.columns:
        for i in df.index:
          if str(df.loc[i,"Latitude"])=="nan" or str(df.loc[i,"Longitude"])=="nan":
            commune=df.loc[i,"Commune"]
            code_postal=df.loc[i,"Code postal"]
            adress=commune+","+str(code_postal)+" , France"
            location=geocoder.arcgis(adress)
            df.loc[i,"Latitude"]=location.x      
            df.loc[i,"Longitude"]=location.y

def activites(df,columns):
  for i in df.index:
      line=str(df.loc[i,"Activités culturelles"])
      line2=str(df.loc[i,"Activités sportives"])
      line3=str(df.loc[i,"Catégories"])

      if line!="nan":
        l=line.split("|")
        df.loc[i,"Label"]=l[0]
      if line=="nan" and line2!="nan"  and line3!="nan":
        l2=line2.split("|")
        df.loc[i,"Label"]=l2[0]
      if line=="nan" and line2=="nan" and line3!="nan":
        l3=line3.split("|")
        df.loc[i,"Label"]=l3[0]
      if line=="nan" and line2!="nan" and line3=="nan":
        l2=line2.split("|")
        df.loc[i,"Label"]=l2[0]