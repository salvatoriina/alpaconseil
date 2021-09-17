import pandas as pd
import numpy as np
from myapp.traitment.saisons import *
from myapp.traitment.jours_feries import *
from myapp.traitment.functions import *
from myapp.traitment.langues import *
from myapp.traitment.metadonnes_fairguest import *
from myapp.traitment.modes_paiement import *
from myapp.traitment.moyens_de_communication import *
from myapp.traitment.salles_reunion import *
from myapp.traitment.sheets import *

global saisons
global langues
global moyens_de_communication
global all_df

saisons=["Printemps","Eté","Automne","Hiver"]
langues=["Langues parlées","Langues de documentation"]
moyens_de_communication=["Moyens de communication","Moyens de communication (information)","Moyens de communication (gestion)"]
colonnes_sheet=["Services","Équipements","Activités sur place","Types de clientèle","Conforts","Labels","Label"]
all_df=[]

def traitement(df):
    #exception
    categorie(df,"Catégories")
    #exception
    mc="Moyens de communication (Standard)"
    if mc in df.columns:
          df=df.rename(columns={'Moyens de communication (Standard)': 'Moyens de communication (Standard)'})

    #Latitude & longitude
    longitude_latitude(df)
    #------- langues
    all_df=[]
    for c in langues:
      new_columns=collect_data(df,c)
      create_column(df,c,new_columns)
      add_langue(df,c,new_columns)
    
    #---- saisons

    create_column(df,"Indications période / saisonnalité",saisons)
    add_columns_saisons(df,"Indications période / saisonnalité",saisons)

    #---- modes de paiement
    mp=collect_data(df,"Modes de paiement")
    create_column(df,"Modes de paiement",mp)
    add_columns_m_paiement(df,"Modes de paiement",mp)

    #----- jours fériés
    jf=collect_data(df,"Jours fériés")
    create_column(df,"Jours fériés",jf)
    add_columns_jf(df,"Jours fériés",jf)

    #----- moyens de communication
    
    for c in moyens_de_communication:
      new_columns=get_columns_mc(df,c)
      create_column(df,c,new_columns)
      add_columns_mc(df,c)
    
    #------ métadonnées-fairguest
    result=get_columns_fairguest(df,"Métadonnées - fairguest")
    create_column(df,"Métadonnées - fairguest",result)
    md_fairguest(df,"Métadonnées - fairguest")
    #convert_to_float(df)

    #------ salle_de_réunion
    create_column_sr(df,"Salles de réunion FR","Capacité maximum")
    insert_column_sr(df,"Salles de réunion FR","Capacité maximum")
    principal=df.replace(np.nan," ",regex=True)
    all_df.append(principal)

    #------- feuilles de calcul
    
    new_df=sheet(df)
    secondaire=new_df.replace(np.nan,"Vide",regex=True)
    all_df.append(secondaire)
   
    return all_df
        
        



