# PDF to Audio Conversion Project

The objective of this project is to facilitate the conversion of PDF documents into audio, streamlining the creation of audio books from PDF files. Utilizing this system, anyone can generate an audio version of a PDF with ease.

### Prerequisites

Before proceeding, ensure you have the following:

1. An **OpenAI API key** for processing.
2. Basic proficiency in executing commands for Docker environments.

### Setup and Execution Instructions

To utilize this tool, please follow the steps outlined below:

1. Clone or **download the project repository** to your local machine.
2. **Locate the PDF** document you wish to convert and copy it into the downloaded project directory. If present, feel free to discard the placeholder `sample.pdf`.
3. Edit the **Dockerfile**: navigate to line number 14, replace `sample.pdf` with the exact name of your PDF document, and save the modifications.
4. Ensure **Docker** is up and running on your system.
5. Open a terminal or command prompt, **navigate to the project folder** where the Dockerfile is located.

Execute the following Docker commands in your terminal:

```
- docker build -t create_audio_book .
- docker run -it create_audio_book
```

Once you've executed the commands, the Docker container will handle the process of converting the specified PDF file into an audio format. Upon successful audio book creation, you will be able to access the audio output as per the configuration detailed within the Docker container.

### Additional Notes

- It's crucial to replace `sample.pdf` in the Dockerfile with the actual name of your PDF file to prevent any discrepancies during the build process.
- Be mindful of the file path when you copy your PDF into the project folder to ensure the Dockerfile can locate it without issues.

Good luck with your conversion process, and enjoy your new audio book!