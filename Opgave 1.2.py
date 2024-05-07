import os
import platform

def play_sound(file_path):
    if platform.system() == 'Windows':
        os.system(f'start {file_path}')
    else:
        os.system(f'xdg-open {file_path}')
def record_sound(duration, output_file):
    import sounddevice as sd
    from scipy.io.wavfile import write
    fs = 44100  
    print("Optagelse påbegyndt...")
    my_recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait() 
    write(output_file, fs, my_recording)  

def main():
    print("Velkommen til lydprogrammet!")

    while True:
        print("\nVælg en af følgende handlinger:")
        print("1. Afspil lyd fra en fil")
        print("2. Optag lyd fra mikrofonen")
        print("3. Afslut")

        choice = input("Indtast dit valg (1/2/3): ")

        if choice == '1':
            file_path = input("Indtast filstien til lydfilen: ")
            if os.path.exists(file_path):
                play_sound(file_path)
            else:
                print("Fejl: Filen blev ikke fundet.")
        elif choice == '2':
            duration = float(input("Indtast varigheden af optagelsen i sekunder: "))
            output_file = input("Indtast filstien til den gemte lydfil (uden .wav): ") + ".wav"
            record_sound(duration, output_file)
            print(f"Optagelse gemt som {output_file}")
        elif choice == '3':
            print("Programmet afsluttes.")
            break
        else:
            print("Ugyldigt valg. Prøv igen.")

if __name__ == "__main__":
    main()
