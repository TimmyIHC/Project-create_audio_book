import fitz  # PyMuPDF
import requests
import tqdm
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import os


def main():
    inputs = get_input()
    filename_to_create_audio = os.path.splitext(os.path.basename(inputs["file_path"]))[0]
    total_audios_created_count = readlines_from_pdf(filename_to_create_audio=filename_to_create_audio,
                                                    file_path=inputs["file_path"], voice=inputs["voice"],
                                                    open_api_key=inputs["open_api_key"])
    audio_name = combine_audios(total_audios_created_count=total_audios_created_count,
                                filename_to_create_audio=filename_to_create_audio)
    final_audio_name = f"{audio_name[:-5]}.mp3"
    os.rename(audio_name,final_audio_name)

    print("\033[2;32m_________________________________________________________________________________\033[0;0m")
    print("\033[2;32mAUDIO CREATION COMPLETE \033[0;0m")
    print("\033[2;32mFILE NAME : \033[0;0m", final_audio_name)

def get_input():
    print("\033[2;35m*********  *******    ********             **             ************")
    print("**     **  **    **   **                     ***          **        **")
    print("*********  **     **  ********     **************         **        **")
    print("**         **    **   **                    ****       ** **     ** **")
    print("**         ******     **                   **          ** **     ** **\033[0;0m")

    file_path = input("\n\nPlease provide the \033[2;32mFILE PATH\033[0;0m for the PDF document that you intend to convert into an audio format : ")
    # Possible Voices = alloy, echo, fable, onyx, nova, and shimmer
    print("\nKindly refer to the accompanying link to explore the available selections for the OPEN API Voice Options: "
          "https://platform.openai.com/docs/guides/text-to-speech/voice-options")
    print("Please input the precise name of the desired voice from the list of available options. In the event that "
          "OPEN AI has introduced additional voices, you are welcome to specify the exact name of the new voice. The "
          "code is designed to accommodate and process any such updates accordingly.")

    print("\nPlease select your preferred voice from the following list of currently available options: alloy, "
          "echo, fable, onyx, nova, and shimmer. Enter the name of the desired voice you wish to use : ")
    print(
        "\033[2;31mNOTE: When entering the voice name, accuracy is paramount as the field is case-sensitive. For example, "
        "if the intended voice is 'alloy,' it must be entered exactly as shown. Any variation in capitalization "
        "will result in an error or unintended outcomes\n\033[0;0m")
    voice = input("\033[2;32mVOICE NAME : \033[0;0m")

    open_api_key = input("\nKindly input the \033[2;32mOpen API Key\033[0;0m you intend to utilize : ")
    return {
        "file_path": file_path,
        "voice": voice,
        "open_api_key": open_api_key
    }


def readlines_from_pdf(filename_to_create_audio, file_path, voice, open_api_key):
    print("\nFILE READING INITIALISATION STARTED :")
    with fitz.open(file_path) as pdf:
        # Iterate over each page
        total_audios_created_count = 0

        for page_num in tqdm.tqdm(range(pdf.page_count)):
            # Get the page
            page = pdf.load_page(page_num)

            # Get the text of the page
            text = page.get_text()
            audio_name = f"{filename_to_create_audio}{page_num + 1}.mp3"
            text_to_speech(text=text, audio_name=audio_name, voice=voice, open_api_key=open_api_key)
            total_audios_created_count += 1

    return total_audios_created_count


def text_to_speech(text, audio_name, voice, open_api_key):
    # Possible Voices = alloy, echo, fable, onyx, nova, and shimmer
    import requests
    headers = {
        'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY', open_api_key),
        'Content-Type': 'application/json',
    }
    json_data = {
        'model': 'tts-1',
        'input': text,
        'voice': voice,
    }
    response = requests.post(url='https://api.openai.com/v1/audio/speech', headers=headers, json=json_data)
    with open(audio_name, 'wb') as f:
        f.write(response.content)


def combine_audios(total_audios_created_count, filename_to_create_audio):
    print("\nAUDIO RENDERING INITIALISATION STARTED :")
    main_audio = f"{filename_to_create_audio}1.mp3"
    # for audio in range(1, total_audios_created_count):
    for audio in tqdm.tqdm(range(1, total_audios_created_count)):
        try:
            audio_name_to_merge = f"{filename_to_create_audio}{audio + 1}.mp3"

            audio1 = AudioSegment.from_file(main_audio,  format="mp3")
            audio2 = AudioSegment.from_file(audio_name_to_merge,  format="mp3")

            # Merge (concatenate) the audio files
            combined = audio1 + audio2

            # Export the result and overwrite audio1 with the combined audio
            combined.export(main_audio, format="mp3")
            os.remove(audio_name_to_merge)
        except CouldntDecodeError as e:
            print(e)

    return main_audio


if __name__ == '__main__':
    main()