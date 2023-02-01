import customtkinter as ctk
import tkinter
from music21 import *
from arvo import tools
from arvo import isorhythm
from arvo import minimalism
from arvo import tintinnabuli
from arvo import transformations
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from tkinter import PhotoImage
from tkinter import filedialog
import random
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

# variabile di default per l'isorhythm
durations = tools.durations_to_stream([2, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1])
composizione = stream.Score()
stream1 = stream.Part()
# variabile per controllo esistenza della composizione piena
ok = False


# funzione che cambia l'aspetto grafico della GUI
def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


# funzione che effettua lo scaling della GUI
def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


# funzione che effettua prende in input la tonica e restituisce la stringa che rappresenta la scala
def sceltaScala(s):
    if (s == "Do" or s == "do" or s == "c" or s == "C"):
        scala = ["B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5"]
    elif (s == "Re" or s == "re" or s == "d" or s == "D"):
        scala = ["C#3", "D4", "E4", "F#4", "G4", "A4", "B4", "C#4", "D5", "E5"]
    elif (s == "Mi" or s == "mi" or s == "e" or s == "E"):
        scala = ["D#3", "E4", "F#4", "G#4", "A4", "B4", "C#4", "D#4", "E5", "F#5"]
    elif (s == "Fa" or s == "fa" or s == "f" or s == "F"):
        scala = ["E3", "F4", "G4", "A4", "Bb4", "C4", "D4", "E4", "F5", "G5"]
    elif (s == "Sol" or s == "sol" or s == "g" or s == "G"):
        scala = ["F#3", "G4", "A4", "B4", "C4", "D4", "E4", "F#4", "G5", "A5"]
    elif (s == "La" or s == "la" or s == "a" or s == "A"):
        scala = ["G#3", "A4", "B4", "C#4", "D4", "E4", "F#4", "G#4", "A5", "B5"]
    elif (s == "Si" or s == "si" or s == "b" or s == "B"):
        scala = ["A#3", "B4", "C#4", "D#4", "E4", "F#4", "G#4", "A#4", "B5", "C#5"]
    else:
        scala = ["null"]
    return scala


# funzione che prende in input uno strumento e restituisce lo strumento corrispettivo della libreria music21
def selectInstrument(s):
    strumento = instrument.Piano()
    if (s == 'Piano'):
        strumento = instrument.Piano()
    elif (s == 'Violino'):
        strumento = instrument.Violin()
    elif (s == 'Chitarra Acustica'):
        strumento = instrument.AcousticGuitar()
    elif (s == 'Fisarmonica'):
        strumento = instrument.Accordion()
    elif (s == 'Sassofono'):
        strumento = instrument.Saxophone()
    elif (s == 'Cornamusa'):
        strumento = instrument.Bagpipes()
    elif (s == 'Banjo'):
        strumento = instrument.Banjo()
    elif (s == 'Clarinetto'):
        strumento = instrument.Clarinet()
    elif (s == 'Chitarra Elettrica'):
        strumento = instrument.ElectricGuitar()
    elif (s == 'Coro'):
        strumento = instrument.Choir()
    else:
        return strumento

    return strumento


# funzione che stampa la scala scelta
def stampaScala(s):
    for i in s:
        print(i + ', ', end='')


# funzione che crea la melodia utilizzando la sequenza di fibonacci
def fibonacciComposer(scala, n):
    song = []
    a = 0
    b = 1

    for i in range(1, n + 1):
        fib = a + b
        a = b
        b = fib
        song = fib2Array(fib, song, scala)
        print(song)
        # text_msg.insert(tkinter.END, "\nNote inserite:  ")
        # text_msg.insert(tkinter.END, song)

    # print('Note nella canzone: ',end='')
    # for i in song:
    #   print (i + ', ', end='')
    text_msg.insert(tkinter.END, "\n  ")
    text_msg.insert(tkinter.END, "\n----------------- Note nella canzone --------------\n  ")
    text_msg.insert(tkinter.END, song)
    return song


# funzione che converte un numero della seq di fibonacci in array di interi
def fib2Array(seq, song, scala):
    # convert numeri in un array di interi
    res = [int(x) for x in str(seq)]
    # stampa risultato
    print("Numero estratto dalla seq di fibonacci ", res)
    # text_msg.insert(tkinter.END, "\nNumero estratto dalla seq di fibonacci:  ")
    # text_msg.insert(tkinter.END, res)

    # Analizza i singoli numeri che compongono un elemento della seq di fibonacci e assegna ad ogni numero una nota della scala
    i = 0
    while (i <= len(res) - 1):
        if (res[i] == 0):
            song.append(scala[0])
        elif (res[i] == 1):
            song.append(scala[1])
        elif (res[i] == 2):
            song.append(scala[2])
        elif (res[i] == 3):
            song.append(scala[3])
        elif (res[i] == 4):
            song.append(scala[4])
        elif (res[i] == 5):
            song.append(scala[5])
        elif (res[i] == 6):
            song.append(scala[6])
        elif (res[i] == 7):
            song.append(scala[7])
        elif (res[i] == 8):
            song.append(scala[8])
        elif (res[i] == 9):
            song.append(scala[9])
        i = i + 1
    return song


# funzione che crea gli accordi in base alla tonica della scala scelta
def getChords(s):
    chords = []
    if (s == "Do" or s == "do" or s == "c" or s == "C"):
        chords = [["Cmaj", "C", "E", "G"], ["Fmaj", "F", "A", "C"], ["Dmin", "D", "F", "A"], ["Emin", "E", "G", "B"]]
    elif (s == "Re" or s == "re" or s == "d" or s == "D"):
        chords = [["Dmaj", "D", "F#", "A"], ["Emin", "E", "G", "B"], ["F#min", "F#", "A", "C#"],
                  ["Gmaj", "G", "B", "D"]]
    elif (s == "Mi" or s == "mi" or s == "e" or s == "E"):
        chords = [["Emaj", "E", "G#", "B"], ["F#min", "F#", "A", "C#"], ["G#min", "G#", "B", "D#"],
                  ["Amaj", "A", "C#", "E"]]
    elif (s == "Fa" or s == "fa" or s == "f" or s == "F"):
        chords = [["Fmaj", "F", "A", "D"], ["Gmin", "G", "Bb", "D"], ["Amin", "A", "C", "E"], ["Bbmin", "Bb", "D", "F"]]
    elif (s == "Sol" or s == "sol" or s == "g" or s == "G"):
        chords = [["Gmaj", "G", "B", "D"], ["Amin", "A", "C", "E"], ["Bmin", "B", "D", "F#"], ["Cmaj", "C", "E", "G"]]
    elif (s == "La" or s == "la" or s == "a" or s == "A"):
        chords = [["Amaj", "A", "C#", "E"], ["Bmin", "B", "D", "F#"], ["C#min", "C#", "E", "G#"],
                  ["Dmaj", "D", "F#", "A"]]
    elif (s == "Si" or s == "si" or s == "b" or s == "B"):
        chords = [["Bmaj", "B", "D#", "F#"], ["C#min", "C#", "E", "G#"], ["D#min", "D#", "F#", "A#"],
                  ["Emaj", "E", "G#", "B"]]
    return chords


# funzione che crea lo stream.Part con gli accordi in base al numero di elementi nello stream della melodia
def createChordStream(chords, song, num_beats):
    chordStream = stream.Part()
    count = 0
    print("Accordi nella canzone: \n")
    text_msg.insert(tkinter.END, "\nAccordi nella canzone:  ")
    for i in range(num_beats):
        c = chord.Chord([chords[i % len(chords)][1], chords[i % len(chords)][2], chords[i % len(chords)][3]],
                        quarterLength=1.0)
        # print(c)
        if (count < 4): 
            print(c.pitchedCommonName)
            text_msg.insert(tkinter.END, "\n ")
            text_msg.insert(tkinter.END, c.pitchedCommonName) #stampa dei nomi degli accordi inseriti
            count += 1
        chordStream.append(c)
    return chordStream


# funzione che prende il bpm scelto dall'utente
def getVelocità(x):
    mm = tempo.MetronomeMark(number=x)
    if (mm.text == None):
        mm.text = 'adagio'
    # print('\nVelocità:' ,mm.text)

    return mm


# funzione che prende in input un intero che rappresente la scelta dell'utente e restituisce la duration utilizzata peer l'isorhythm
def getDurations(x):
    global durations
    if (x != ''):

        if (x == '1'):
            durations = tools.durations_to_stream([2, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1])
        elif (x == '2'):
            durations = tools.durations_to_stream([1.25, 0.5, 0.5, 1, 0.75, 1.25])
        elif (x == '3'):
            durations = tools.durations_to_stream([2, 0.5, 0.5, 1, 4, 1, 0.5])
        elif (x == '4'):
            durations = tools.durations_to_stream([0.25, 0.25, 0.5, 0.5, 0.5])
        elif (x == '5'):
            durations = tools.durations_to_stream([0.5, 0.5, 1, 1, 0.5, 2])
        elif (x == '6'):
            durations = tools.durations_to_stream([1, 1, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25])


# funzione che mette insieme due stream per creare la composizione
def showSong(song):
    global stream1
    counter = 0
    if (bpm_entry.get() != ''):
        v = int(bpm_entry.get())
        velocità = getVelocità(v)
        print('\nVelocità:', velocità.text)
    else:
        velocità = tempo.MetronomeMark(number=90)

    while counter <= len(song) - 1:
        n = note.Note(song[counter])
        stream1.append(n)
        counter += 1
    # arvo
    '''
    Si utilizza la libreria minimalism per generare una melodia utilizzando un processo additivo in modo tale che verranno usate note in ordine
    inverso e verrà ripetuta 2 volte.
    Poi si utilizza la libreria isorhythm per generare un pattern di durate in modo da creare un isoritmo,
    per finire si utilizza la libreria transformations per generare la melodia al contrario.
    Infine il tutto viene aggiunto allo stream melody.
    '''
    getDurations(isorhythm_menu.get()) #prende il pattern scelto dall'utente e setta la variabile globale durations

    global durations

    chords = getChords(keys_button.get())

    melody = minimalism.additive_process(stream1, direction=minimalism.Direction.BACKWARD, repetitions=2)
    melody = isorhythm.create_isorhythm(melody, durations)
    melody.append(transformations.retrograde(melody))

    chordStream = stream.Part()
    num_beats = int(melody.duration.quarterLength)  # numero elementi nella battuta
    chordStream = createChordStream(chords, song, num_beats)

    strumento = selectInstrument(instrument_menu.get())

    melody.insert(0, strumento)
    melody.insert(0.0, velocità)
    melody.insert(0, dynamics.Dynamic(r_Volume.get()))

    strum = selectInstrument(instrument_menu.get())

    chordStream.insert(0, clef.BassClef())
    chordStream.insert(0, strum)
    chordStream.insert(0.0, velocità)
    chordStream.insert(0, dynamics.Dynamic(l_Volume.get()))

    global composizione

    composizione = tools.merge_streams(melody, chordStream, stream_class=stream.Score)

    composizione.metadata = metadata.Metadata()
    composizione.metadata.title = " Progetto Musimatica"
    composizione.metadata.composer = "Roberto"

    piano_staff_group = layout.StaffGroup(
        [stream1],
        name="Piano",
        abbreviation="Pno.",
        symbol="brace",
    )

    composizione.insert(0.0, piano_staff_group)

    global ok
    ok = True


# funzione stampa intesità volume
def getNomeVolume(vol):
    if (vol == 'p'):
        print("\nNome volume: piano")
        text_msg.insert(tkinter.END, "piano")
    elif (vol == 'mp'):
        print("\nNome volume: Medio piano")
        text_msg.insert(tkinter.END, "medio piano")
    elif (vol == 'mf'):
        print("\nNome volume: medio forte")
        text_msg.insert(tkinter.END, "medio forte")
    elif (vol == 'f'):
        print("\nNome volume: forte")
        text_msg.insert(tkinter.END, "forte")


# bottone di tkinter per gestire gli input
def button_callback():
    text_msg.delete("0.0", "end")
    text_msg.insert(tkinter.END, "\nScala di: ")
    text_msg.insert(tkinter.END, keys_button.get())
    text_msg.insert(tkinter.END, "\nStrumento usato: ")
    text_msg.insert(tkinter.END, instrument_menu.get())
    text_msg.insert(tkinter.END, "\nLunghezza sequenza fibonacci:  ")
    text_msg.insert(tkinter.END, fib_len_Entry.get())
    text_msg.insert(tkinter.END, "\nVelocità inserita:  ")
    text_msg.insert(tkinter.END, bpm_entry.get())
    text_msg.insert(tkinter.END, "  nome: ")
    if (bpm_entry.get() != ''):
        text_msg.insert(tkinter.END, getVelocità(int(bpm_entry.get())).text)
    else:
        text_msg.insert(tkinter.END, " maestoso  ")
    text_msg.insert(tkinter.END, "\nIntensità volume R:  ")
    getNomeVolume(r_Volume.get())
    text_msg.insert(tkinter.END, "\nIntensità volume L:  ")
    getNomeVolume(l_Volume.get())
    scala = sceltaScala(keys_button.get())
    print()
    lenComposition = 1
    if (fib_len_Entry.get() == ''):
        lenComposition = 3
    else:
        lenComposition = int(fib_len_Entry.get())
    song = fibonacciComposer(scala, lenComposition)
    print()
    # chords=getChords(keys_button.get())
    # print("\nAccordi Scala di ",keys_button.get(),chords)
    # cStream=createChordStream(chords,song)
    # print(cStream)
    showSong(song)


# bottone per l'apertura della composizione su un app che legge i file MusicXML
def button_openApp():
    global composizione
    global ok

    if (ok == True):
        text_msg.insert(tkinter.END, "\n  ")
        text_msg.insert(tkinter.END, "\n----------------- Apertura su App --------------\n  ")

        composizione.show()
    else:
        text_msg.delete("0.0", "end")
        text_msg.insert(tkinter.END, "\n  ")
        text_msg.insert(tkinter.END, "\n----------------- Attenzione --------------\n  ")
        text_msg.insert(tkinter.END, "\nCrea prima una composizione attraverso i tasti sopra")


# bottone per salvare la composizione come file midi
def button_saveMidi():
    global composizione
    global ok

    if (ok == True):
        filepath = filedialog.asksaveasfilename(defaultextension=".mid", filetypes=[("MIDI file", "*.mid")])
        if filepath:
            mf = midi.translate.streamToMidiFile(composizione)
            mf.open(filepath, 'wb')
            mf.write()
            mf.close()

            text_msg.insert(tkinter.END, "\n  ")
            text_msg.insert(tkinter.END,
                            "\n----------------- File salvato con Successo --------------\n  ")

    else:
        text_msg.delete("0.0", "end")
        text_msg.insert(tkinter.END, "\n  ")
        text_msg.insert(tkinter.END, "\n----------------- Attenzione --------------\n  ")
        text_msg.insert(tkinter.END, "\nCrea prima una composizione attraverso i tasti sopra")


# bottone per creare partitura su assi cartesiani delle sole note create con fibonacci senza le alterazioni della libreria arvo
def button_AxAy():
    global composizione
    global ok
    global stream1
    new_window=ctk.CTk()
    new_window.title("Piano Cartesiano")
    new_window.wm_iconbitmap("fib.ico")
    if (ok == True):

        comp2 = stream.Part()
        comp2 = stream1

        # estrae le informazioni sulla posizione e la durata delle note ecrea il grafico a barre orizzontali

        for n in comp2.flat.notes:
            plt.broken_barh([(n.offset, n.duration.quarterLength)], (n.pitch.frequency, 1), facecolors='blue')

        plt.xlabel("Tempo ")
        plt.ylabel("Frequenza (Hz)")
        plt.suptitle("Partitura su Piano Cartesiano")
        #plt.show()
        fig = plt.gcf()
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        new_window.mainloop()
        
         
        text_msg.insert(tkinter.END, "\n  ")
        text_msg.insert(tkinter.END, "\n----------------- Partitura creata con successo --------------\n  ")

    else:
        text_msg.delete("0.0", "end")
        text_msg.insert(tkinter.END, "\n  ")
        text_msg.insert(tkinter.END, "\n----------------- Attenzione --------------\n  ")
        text_msg.insert(tkinter.END, "\nCrea prima una composizione attraverso i tasti sopra")
    
   

root = ctk.CTk()
root.geometry("1080x1080 ")
root.title("Fibonacci Composer")
root.wm_iconbitmap("fib.ico")


sidebar_frame = ctk.CTkFrame(root)
sidebar_frame.pack(pady=10, padx=10, fill="both", side="left")

main_frame = ctk.CTkFrame(root)
main_frame.pack(pady=10, padx=10, expand=True, side="top")

text_frame = ctk.CTkFrame(root)
text_frame.pack(pady=10, padx=10, fill="both", expand=True, side="bottom")
# text_msg = tkinter.Text(text_frame)
text_msg = ctk.CTkTextbox(text_frame)
text_msg.pack(pady=10, padx=10, expand=True, fill="both")
text_msg.insert(tkinter.END, "\nBenvenuto! \nEcco alcuni esempi di configurazioni: \nSI - CHITARRA ACUSTICA - 8 - 80 - 6 - MF - P\nDO - SASSOFONO - 7 - 90 - 5 -MF - P\nMI- VIOLINO - 7 - 60 - 4- MF- P\nRE - PIANO - 9 -90 - 3 - MF - P\n")


logo_label = ctk.CTkLabel(sidebar_frame, text="Fibonacci Composer", font=ctk.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
# bottoni



open_app_button = ctk.CTkButton(sidebar_frame, text="Apri sull' App", command=button_openApp)
open_app_button.grid(row=1, column=0, padx=20, pady=10)
save_midi_button = ctk.CTkButton(sidebar_frame, text="Salva file midi", command=button_saveMidi)
save_midi_button.grid(row=2, column=0, padx=20, pady=10)
alternative_Score_button = ctk.CTkButton(sidebar_frame, text="Partitura Alternativa", command=button_AxAy)
alternative_Score_button.grid(row=3, column=0, padx=20, pady=10)

appearance_mode_label = ctk.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
appearance_mode_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"],
                                                command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
scaling_label = ctk.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
scaling_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                        command=change_scaling_event)
scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


img = ImageTk.PhotoImage(Image.open("fib.png"))

label = ctk.CTkLabel(sidebar_frame, image = img, text='')
label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="s")


label_name = ctk.CTkLabel(main_frame, text="Compositore di Fibonacci ", font=("Arial Black", 25), anchor=tkinter.CENTER)
label_name.grid(row=0, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

key_name = ctk.CTkLabel(main_frame, text="Scegli una scala con cui comporre ", justify=tkinter.LEFT,
                        font=("Helvetica", 15))
key_name.grid(row=2, column=0, pady=10, padx=10)
keys_button = ctk.CTkSegmentedButton(main_frame, values=["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"])
keys_button.grid(row=2, column=1, pady=10, padx=10)
instrument_label = ctk.CTkLabel(main_frame, text="Seleziona uno strumento ", justify=tkinter.LEFT,
                                font=("Helvetica", 15))
instrument_label.grid(row=3, column=0, pady=10, padx=10)
instrument_menu = ctk.CTkOptionMenu(main_frame,
                                    values=["Piano", 'Violino', 'Chitarra Acustica', 'Fisarmonica', 'Sassofono',
                                            'Cornamusa', 'Banjo', 'Clarinetto', 'Chitarra Elettrica', 'Coro'])
instrument_menu.grid(row=3, column=1, pady=10, padx=10)

composition_len_label = ctk.CTkLabel(main_frame, text="Inserisci lunghezza composizione (num seq fib)",
                                     justify=tkinter.LEFT, font=("Helvetica", 15))
composition_len_label.grid(row=4, column=0, pady=10, padx=10)
fib_len_Entry = ctk.CTkEntry(main_frame, placeholder_text="Numero seq fib")
fib_len_Entry.grid(row=4, column=1, pady=10, padx=10)

bmp_label = ctk.CTkLabel(main_frame, text="Inserisci velocità (bmp)  ", justify=tkinter.LEFT, font=("Helvetica", 15))
bmp_label.grid(row=5, column=0, pady=10, padx=10)
bpm_entry = ctk.CTkEntry(main_frame, placeholder_text="120")
bpm_entry.grid(row=5, column=1, pady=10, padx=10)

isorhythm_label = ctk.CTkLabel(main_frame, text="Seleziona pattern isoritmia ", justify=tkinter.LEFT,
                               font=("Helvetica", 15))
isorhythm_label.grid(row=6, column=0, pady=10, padx=10)
isorhythm_menu = ctk.CTkOptionMenu(main_frame, values=['1', '2', '3', '4', '5', '6'])
isorhythm_menu.grid(row=6, column=1, pady=10, padx=10)

intensity_label = ctk.CTkLabel(main_frame, text="Seleziona intensità volume R ", justify=tkinter.LEFT,
                               font=("Helvetica", 15))
intensity_label.grid(row=7, column=0, pady=10, padx=10)
r_Volume = ctk.CTkOptionMenu(main_frame, values=['p', 'mp', 'mf', 'f'])
r_Volume.grid(row=7, column=1, pady=10, padx=10)

intensity_label2 = ctk.CTkLabel(main_frame, text="Seleziona intensità volume L ", justify=tkinter.LEFT,
                                font=("Helvetica", 15))
intensity_label2.grid(row=8, column=0, pady=10, padx=10)
l_Volume = ctk.CTkOptionMenu(main_frame, values=['p', 'mp', 'mf', 'f'])
l_Volume.grid(row=8, column=1, pady=10, padx=10)

start_button = ctk.CTkButton(main_frame, text="Avvia", height=50, width=200, command=button_callback)

start_button.grid(row=10, column=1, pady=10, padx=10)

# default values
appearance_mode_optionemenu.set("Light")
scaling_optionemenu.set("100%")
instrument_menu.set("Piano")
isorhythm_menu.set("1")
r_Volume.set("mf")
l_Volume.set("mf")
keys_button.set("Do")

if __name__ == "__main__":
    root.mainloop()
    
    

