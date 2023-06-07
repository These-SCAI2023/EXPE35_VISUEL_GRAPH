#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:22:26 2023

@author: obtic2023
"""

import glob
import json
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import venn
# from matplotlib_venn import venn2



def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)
        
        return dist
    

        
path_corpora = "../DATA/ELTeC-Fra_spacy3.5.1_CONCAT_DISTANCES/*"
# dans "corpora" un subcorpus = toutes les versions 'un texte'

# liste_EN_ocr=[]
# liste_EN_pp=[]


#for subcorpus in sorted(glob.glob("%s/*"%path_corpora)):
for autor in sorted(glob.glob(path_corpora)):
    # nameautor=re.sub("/|\.\.","__",autor)
    nameautor=autor.split("/")[3]
    dico_inter={}
    for subcorpus in sorted(glob.glob("%s/*/*"%autor)): 
        
        # liste_ocr_ver=[]
        for path in sorted(glob.glob("%s/*-concat.json"%subcorpus)):
            # print(path)
            version=path.split("/")[-1]
            ocr_version=version.split("_")[2]
            ocr_version=ocr_version.split(".")[0]
            if ocr_version=="PP":
                ocr_version=re.sub("PP","Référence",ocr_version)
            if ocr_version=="Kraken-base":
                ocr_version=re.sub("Kraken-base","Kraken",ocr_version)
            if ocr_version=="TesseractFra-PNG":
                ocr_version=re.sub("TesseractFra-PNG","Tess. fr",ocr_version)
            ner_version=version.split("_")[3]
            ner_version=ner_version.split(".")[0]
            # print(ocr_version)
            texte = lire_fichier(path)  
            # liste_ocr_ver.append([ner_version,ocr_version,texte])
            dico_inter.setdefault(ner_version,{})
            dico_inter[ner_version][ocr_version]=set(texte)
        
    for ner_version, toto in dico_inter.items():
        
        liste_names=sorted(list(toto.keys()))
        liste_toto=[x+str(len(toto[x])) for x in liste_names]
        liste_res=[]
        for n in liste_names:
            liste_res.append(toto[n])
        print([len(x) for x in liste_res])
        # print(len(liste_names))
        # print(len(liste_res))
        labels = venn.get_labels(liste_res, fill=['number'])
        path_output=f"../RES/{nameautor}_{ner_version}.png"
        print(path_output)
        # fig, ax = venn.venn2(labels, names=liste_toto)
        fig, ax = venn.venn2(labels, names=liste_names)
        fig.savefig(path_output, bbox_inches='tight')
    #     # 1/0
                
         
            

          
            
                   
               
 



          


    
    
    