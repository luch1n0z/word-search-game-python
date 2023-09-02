from random import randint
import time
import pygame

def stampa_griglia(griglia):
    separatore = '+--+--+--+--+--+--+--+--+--+--+'
    barra = '|' 
    for sep in range(10):
        print(separatore)
        for bar in range(10):
            print(barra,griglia[sep][bar],end='')
        print(barra)
        print(separatore)

def generatore_griglia(griglia):#crea la griglia 
    separatore = '+--+--+--+--+--+--+--+--+--+--+'
    barra = '|'
    lettere=['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z']
    for sep in range(10):
        print(separatore)
        for bar in range(10):
            lettera=lettere[randint(0 , len(lettere) - 1 )]
            griglia[sep][bar] = lettera
            print(barra,griglia[sep][bar],end='')
        print(barra)
        print(separatore)
    return griglia

def incrementa_punteggio():
    global punteggio_totale
    punteggio_totale += 1
    print('Punteggio: ',punteggio_totale)

def calcolo_lunghezza_righe(griglia):
    for i in griglia:
        lunghezza_righe = len(i)
    return lunghezza_righe

def generatore_griglia_con_none(griglia):
    for i in range(10):
        righe = [None] * 10
        griglia.append(righe)

def indice_ultimo_carattere(parola,lunghezza_parola):
    j=1
    for i in parola:
        if j == lunghezza_parola:
            return j
        j+=1

def controllo_parola_in_colonne(griglia,parola,suono_vittoria):
    #CONTROLLO COLONNE
    for righe in range(10):
        concatenazione=''
        for colonne in  range(10):
            concatenazione += griglia[colonne][righe]


        if parola in concatenazione:
            start_row = concatenazione.index(parola)
            suono_vittoria.play()
            return [True,start_row]
        
    return [False,None]

def evidenziazione_colonne(griglia,start_row,lunghezza_parola_trovata,lunghezza_colonne,sottofondo,suono_fine_tempo,tempo_generale_complessivo):
    for offset in range(lunghezza_parola_trovata):
        griglia[start_row+offset][lunghezza_colonne - lunghezza_parola_trovata - start_row] = '*'
    stampa_griglia(griglia)
    tempo = time.time()
    tempo_impiegato = tempo - tempo_generale_complessivo
    print('Il tempo impiegato e: ',tempo_impiegato)
    if tempo_impiegato > 10:
        sottofondo.stop()
        suono_fine_tempo.play()
        time.sleep(3)
        return True
    
    return False
    
def controllo_parola_in_righe(griglia,parola,suono_vittoria):
    #CONTROLLO RIGHE 
    for righe in griglia:
        st = ''.join(righe)
        if parola in st:
            i_r = griglia.index(righe)
            suono_vittoria.play()
            return [True,i_r,st]
        
    return [False,None,None]

def evidenziazione_righe(griglia,parola,suono_vittoria,tempo_generale_complessivo):
    
    valori_di_ritorno = controllo_parola_in_righe(griglia,parola,suono_vittoria)
    if valori_di_ritorno[0]:
        i_riga = valori_di_ritorno[1]
        st = valori_di_ritorno[2]
        suono_vittoria.play()
        start_col = st.index(parola_trovata)
        
        for righe in griglia:
            indice_riga = griglia.index(righe)
            for offset in range(lunghezza_parola_trovata):
                if indice_riga == i_riga: 
                    griglia[indice_riga][start_col + offset] = '*'  
                else:                 
                    break
        stampa_griglia(griglia)
        tempo = time.time()
        tempo_impiegato = tempo - tempo_generale_complessivo
        print('Il tempo impiegato e: ',tempo_impiegato)
        if tempo_impiegato > 10:
            sottofondo.stop()
            suono_fine_tempo.play()
            time.sleep(3)
            return True
        
    return False

def controllo_parole_in_diagonale_principale(griglia,parola):
    diag_principale = ''
    for righe in range(10):
        for colonne in range(10):
            if righe == colonne:
                diag_principale += griglia[righe][colonne]
            
    if parola in diag_principale:
        suono_vittoria.play()
        return [True,diag_principale]
    
    return [False,None]

def evidenziazione_diagonale_principale(griglia,parola,tempo_generale_complessivo):
    valori_ritorno_controllo_diagonale_principale = controllo_parole_in_diagonale_principale(griglia,parola)
    
    start_row = valori_ritorno_controllo_diagonale_principale[1].index(parola_trovata)
    start_col = valori_ritorno_controllo_diagonale_principale[1].index(parola_trovata)
    
    for offset in range(lunghezza_parola_trovata):
        griglia[start_row + offset][start_col + offset] = '*'

    stampa_griglia(griglia)
    tempo = time.time()
    tempo_impiegato = tempo - tempo_generale_complessivo
    print('Il tempo impiegato e: ',tempo_impiegato)
    if tempo_impiegato > 10:
        sottofondo.stop()
        suono_fine_tempo.play()
        time.sleep(3)
        return True
    
    return False

def controllo_parole_in_diagonale_secondaria(griglia,parola):
#CONTROLLO DIAGONALE SECONDARIA
    lunghezza_righe = calcolo_lunghezza_righe(griglia)
    diag_secondaria=''
    for d in range(10):
        diag_secondaria += griglia[d][lunghezza_righe-d-1]
    if parola in diag_secondaria:
        return [True,diag_secondaria]
    
    return [False,None]
    
def evidenziazione_diagonale_secondaria(griglia,parola,tempo_generale_complessivo):
    valori_ritorno_controllo_parole_in_diagonale_secondaria = controllo_parole_in_diagonale_secondaria(griglia,parola)
    # Calcolo dell'indice iniziale della riga e della colonna
    start_row = valori_ritorno_controllo_parole_in_diagonale_secondaria[1].index(parola_trovata)
    start_col = 9 - valori_ritorno_controllo_parole_in_diagonale_secondaria[1].index(parola_trovata) 
    for i in range(lunghezza_parola_trovata):
        griglia[start_row + i][start_col - i] = '*'
    # Stampo la griglia modificata
    stampa_griglia(griglia)
    tempo = time.time()
    tempo_impiegato = tempo - tempo_generale_complessivo
    print('Il tempo impiegato e: ',tempo_impiegato)
    if tempo_impiegato > 10:
        sottofondo.stop()
        suono_fine_tempo.play()
        time.sleep(3)
        return True
    
    return False

def controllo_parole_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx(griglia,parola):
    #CONTROLLO DIAGONALI (A DESTRA DELLA PRINCIPALE), DA IN ALTO SINISTRA AD IN BASSO A DESTRA
    for offset in range(1, 10):
        conc_diagonale_generale_da_sx_a_dx = ''
        for righe in range(10 - offset):
            colonne = righe + offset
            conc_diagonale_generale_da_sx_a_dx += griglia[righe][colonne]

            if parola in conc_diagonale_generale_da_sx_a_dx:
                return [True,conc_diagonale_generale_da_sx_a_dx]
    return [False,None]


            
#WORK IN PROGRESS     
def evidenziazione_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx(griglia,tempo_generale_complessivo,parola,lunghezza_parola):
    valori_ritorno_controllo_parole_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx = controllo_parole_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx(griglia,parola)
    conc_diagonale_generale_da_sx_a_dx = valori_ritorno_controllo_parole_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx[1]
    ultimo_indice = indice_ultimo_carattere(parola,lunghezza_parola)
    indici = []
    start_row = conc_diagonale_generale_da_sx_a_dx.index(parola)
    end_row = conc_diagonale_generale_da_sx_a_dx.rindex(parola)
    print('ultimo indice: ' ,ultimo_indice)
    #for i in range(start_row, ultimo_indice + 1): #offset: 1 start_row: 1 end_row + 1: 4
       #colonna = offset + start_row #colonna: 1 + 1 = 2
      #  print('i: ',i,'start_row: ',start_row,'ultimo_indice: ',ultimo_indice)
        #griglia[offset][colonna - start_row] = '*'  # Aggiunta dell'asterisco in base all'offset #griglia[1][2-1] = griglia[1][1]
     #   griglia[i][i*2] = '*'
    start_row = conc_diagonale_generale_da_sx_a_dx.index(parola) + 1
    end_row = conc_diagonale_generale_da_sx_a_dx.rindex(parola)
    for i in range(start_row, end_row + 1):
        if i >= start_row + 1 and i <= end_row - 1:
            griglia[i][i + 1] = '*'


    stampa_griglia(griglia)
    tempo = time.time()
    tempo_impiegato = tempo - tempo_generale_complessivo
    print('Il tempo impiegato e: ',tempo_impiegato)
    if tempo_impiegato > 10:
        time.sleep(3)
        return True

def controllo_diagonali_a_sinistra_della_principale(griglia,parola):
    for offset in range(1,10):
        conc_diagonale_generale_da_sx_a_dx_2 = ''
        for righe in range(10-offset):
            colonne = righe + offset
            conc_diagonale_generale_da_sx_a_dx_2 += griglia[colonne][righe]

            if parola_trovata in conc_diagonale_generale_da_sx_a_dx_2:
                start_row = conc_diagonale_generale_da_sx_a_dx_2.index(parola)
                return [True,conc_diagonale_generale_da_sx_a_dx_2,start_row]
            
    return [False,None,None]

#WORK IN PROGRESS
def evidenziazione_diagonali_a_sinistra_della_principale(griglia,tempo_generale_complessivo,parola,lunghezza_parola):
    valori_ritorno_controllo_diagonali_a_sinistra_della_principale = controllo_diagonali_a_sinistra_della_principale(griglia,parola)
    diagonale_generale_da_sc_a_dx_2 = valori_ritorno_controllo_diagonali_a_sinistra_della_principale[1]
    start_row = valori_ritorno_controllo_diagonali_a_sinistra_della_principale[2] - 1
    #start_row = diagonale_a_sinistra_della_principale.index(parola)
    #print('diagonale a sinistra della principale: ',diagonale_a_sinistra_della_principale)
    #print('start_row: ',start_row)
    #for i in range(start_row,lunghezza_parola_trovata + start_row ):
     #   colonne = start_row + 1
      #  griglia[i + 1][colonne] = '*'
    print('start_row:' ,start_row)
    if controllo_diagonali_a_sinistra_della_principale(griglia,parola):
        for i in range(1,lunghezza_parola+start_row):
            for j in range(start_row,lunghezza_parola+start_row):
                if j == i+1: 
                    griglia[j][i] = '*'
                    print('i: ',i,'j',j)
                if start_row == 2:
                    if j == i + 2:
                        print('ciao')
                        griglia[i][j] = '*'
                
    stampa_griglia(griglia)
    tempo = time.time()
    tempo_impiegato = tempo - tempo_generale_complessivo
    print('Il tempo impiegato e: ',tempo_impiegato)
    if tempo_impiegato > 10:
        time.sleep(3)
        return True
    
punteggio_totale = 0
griglia = []
lunghezza_colonne = 10
iterazione = 0
pygame.init()
sottofondo=pygame.mixer.Sound('C:\\Users\\lucag\\Downloads\\file_example_WAV_1MG.wav')
suono_fine_tempo = pygame.mixer.Sound('C:\\Users\\lucag\\Downloads\\mixkit-retro-arcade-lose-2027.wav')
suono_vittoria = pygame.mixer.Sound('C:\\Users\\lucag\\Downloads\\short-success-sound-glockenspiel-treasure-video-game-6346 (1).mp3')
sottofondo.play(loops=-1)

generatore_griglia_con_none(griglia)
griglia_piena = generatore_griglia(griglia)#modifichiamo la griglia precedente con lettere casuali
tempo_generale_complessivo = time.time()

while True:
    scelta = int(input('Inserisci 0 se vuoi giocare, 1 se vuoi uscire.\n'))
    
    if scelta == 0:
        tempo_generale = time.time()
        parola_trovata = input('Inserisci la parola che hai trovato\n').lower()
                
        lunghezza_parola_trovata = len(parola_trovata)
    
        risultato_controllo_parola_trovata_in_colonne = controllo_parola_in_colonne(griglia_piena,parola_trovata,suono_vittoria)
        risultato_controllo_parola_trovata_in_righe = controllo_parola_in_righe(griglia_piena,parola_trovata,suono_vittoria)
        risultato_controllo_parola_trovata_in_diagonale_principale = controllo_parole_in_diagonale_principale(griglia,parola_trovata)
        risultato_controllo_parola_trovata_in_diagonale_secondaria = controllo_parole_in_diagonale_secondaria(griglia,parola_trovata)
        risultato_controllo_parola_trovata_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx = controllo_parole_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx(griglia,parola_trovata)
        risultato_controllo_parola_trovata_in_diagonali_a_sinistra_della_principale = controllo_diagonali_a_sinistra_della_principale(griglia,parola_trovata)
        valori_ritorno_evidenziazione_righe = evidenziazione_righe(griglia,parola_trovata,suono_vittoria,tempo_generale)

        if risultato_controllo_parola_trovata_in_colonne[0]:
            print('Parola trovata in una colonna!')
            incrementa_punteggio()
            
            if evidenziazione_colonne(griglia_piena,risultato_controllo_parola_trovata_in_colonne[1],lunghezza_parola_trovata,lunghezza_colonne,sottofondo,suono_fine_tempo,tempo_generale):
                print('Tempo esaurito.Uscita dal gioco...')
                break

        elif risultato_controllo_parola_trovata_in_righe[0]:
            print('Parola trovata in una riga!')
            incrementa_punteggio()

            if evidenziazione_righe(griglia_piena,parola_trovata,suono_vittoria,tempo_generale):
                print('Tempo esaurito. Uscita dal gioco...')
                break
        
        elif risultato_controllo_parola_trovata_in_diagonale_principale[0]:
            print('Parola trovata in diagonale principale!')
            incrementa_punteggio()

            if evidenziazione_diagonale_principale(griglia,parola_trovata,tempo_generale):
                print('Tempo esaurito. Uscita dal gioco...')
                break

        elif risultato_controllo_parola_trovata_in_diagonale_secondaria[0]:
            print('Parola trovata in diagonale secondaria!')
            incrementa_punteggio()

            if evidenziazione_diagonale_secondaria(griglia,parola_trovata,tempo_generale):
                print('Tempo esaurito. Uscita dal gioco...')
                break

        elif risultato_controllo_parola_trovata_in_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx[0]:
            print('Parola trovata nelle diagonali (a destra della principale) da in alto a sinistra ad in basso a destra!')
            incrementa_punteggio()

            if evidenziazione_diagonali_a_destra_della_principale_da_in_alto_a_sx_ad_in_basso_a_dx(griglia,tempo_generale,parola_trovata,lunghezza_parola_trovata):
                print('Tempo esaurito. Uscita dal gioco...')
                break

        elif risultato_controllo_parola_trovata_in_diagonali_a_sinistra_della_principale[0]:
            print('Parola trovata nelle diaagonali a sinistra dellaa diagonale principale!')
            incrementa_punteggio()

            if evidenziazione_diagonali_a_sinistra_della_principale(griglia,tempo_generale,parola_trovata,lunghezza_parola_trovata):
                print('Tempo esaurito. Uscita dal gioco...')
                break

        else:
            print('Parola non presente nella griglia, riprova!')
            suono_fine_tempo.play()
            

    elif scelta == 1: 
        print('Fine, punteggio totale: ',punteggio_totale)
        break

    else:
        suono_fine_tempo.play()
        print('Inserisci 0 o 1')
        
    iterazione += 1
