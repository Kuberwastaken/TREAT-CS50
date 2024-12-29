# TREAT: Trigger Recognition for Enjoyable and Appropriate Television

![Treat_Banner](https://github.com/user-attachments/assets/eeae40eb-85f0-4976-b953-410a42d68038)

## Project Description
I was tired of getting grossed out watching unexpected scenes in movies and TV and losing my appetite, that's why I created TREAT.

The goal of this project is to empower viewers by forewarning them about potential triggers in the content they watch, making the viewing experience more enjoyable, inclusive, and appropriate for everyone.

TREAT is a web application that uses natural language processing to analyze movie and TV show scripts, identifying potential triggers to help viewers make informed choices.

[![Video Title](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

## Installation Instructions
### Prerequisites
 - Star the Repository to Show Your Support.

 - Clone the Repository to Your Local Machine:

    ```
   git clone https://github.com/Kuberwastaken/TREAT.git
    ```
### Hugging Face Login Instructions for FLAN-T5-Base Model
To use the FLAN-T5-Base model, you need to log in to your Hugging Face account and set up access:

 1. Login or Create a Hugging Face Account:

 -  Visit [Hugging Face](https://huggingface.co/) and create an account

 2. Get Your Access Token:

 - Navigate to your account settings and [generate an access token](https://huggingface.co/settings/tokens).

 3. Login to Hugging Face in Your Environment:
     
 - Run the following command in your terminal:

   ```
   huggingface-cli login
   ```
 - Enter your Hugging Face access token when prompted.


 4. Download the FLAN-T5-Base Model:

 - The model will be downloaded automatically when running the script analysis for the first time.

### Environment Setup
To set up the development environment, you will need to create a virtual environment and install the necessary dependencies.

1. Create a Virtual Environment:

   ```
   python3 -m venv treat-env
   ```
2. Activate the Virtual Environment:

   ```
   source treat-env/bin/activate   # On Unix or MacOS
   treat-env\Scripts\activate      # On Windows
   ```
3. Install Dependencies: 

   Navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```

## Project Usage
1. Start the Flask Server:

   ```
   python run.py
   ```
2. Open Your Browser: 

   Navigate to http://127.0.0.1:5000 to access the TREAT web interface.

3. Analyze Scripts:

   You can manually enter a script in the provided text area and click "Analyze Script."

## File Descriptions
- **app.py:** The main Flask application file that handles routing.

- **app/routes.py:** Contains the Flask routes for handling script uploads.

- **app/model.py:** Includes the script analysis functions using the FLAN-T5-Base model.

- **templates/index.html:** The main HTML file for the web interface.

- **static/css/style.css:** Custom CSS for styling the web interface.

- **static/js/app.js:** JavaScript for handling client-side interactions.

## Types of Triggers Detected
The TREAT application focuses on identifying a variety of potential triggers in scripts, including but not limited to:

- **Violence:** Scenes of physical aggression or harm.

- **Gore:** Graphic depiction of injury, blood, or dismemberment.

- **Abuse:** Instances of physical or emotional abuse

- **Substance Use:** Representation of drug or alcohol use.

- **Sensitive Topics:** Issues related to mental health, suicide, self-harm, or trauma.

These categories help address a very real-world problem by forewarning viewers about potentially distressing content, enhancing their viewing experience.

## Design Choices

- **Inspiration:** I aimed for a simple and intuitive user experience, focusing on simplicity and ease of use. This decision stemmed from the need to create a tool that is easy to navigate for all users, regardless of background or age.

- **Theme and Color Scheme:** The chosen theme and color scheme create a visually appealing and engaging environment. The chocolate and sweets theme is intended to stick to the TREAT theme and make the experience enjoyable and pleasant.

- **Script Analysis:** The FLAN-T5-Base model by Google from Hugging Face was chosen for its accuracy and performance in natural language understanding tasks, while also being open source. The decision was based on its ability to provide precise trigger recognition.

## To-Do List
- Integration with an API to Directly Search Scripts by Name of Movies/Shows

- Switching to the more Modern: Llama-3.2-1B Model for Better Efficiency and Results

- Introduce multiple themes to allow users to customize the appearance of the application according to their preferences.

- Expand the list of triggers to cover a broader range of sensitive topics and ensure comprehensive analysis.

## Open Source Contribution
This repository is completely open source and free to contribute. I intend to keep this project alive and evolve it into a tool that's extremely usable for all. Contributions are welcome to add new features, improve the user interface, or enhance the script analysis.

## Acknowledgements
I would like to thank:

- Dr. David J Malan: For teaching CS50 and inspiring countless students to pursue computer science.

- Google AI: For developing the FLAN-T5-Base model, a critical component of this project.

- Parasite (2019): For that unexpected jumpscare that ruined my appetite and ultimately inspired this project.

## License
This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md)
