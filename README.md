# ein einfacher Chatbot

<img width="340" alt="image" src="https://user-images.githubusercontent.com/14870896/197070856-6547d5d8-1ea7-4f84-8ad5-82c4618cb374.png">

- Rasa installieren (siehe https://github.com/michaeleggers/RasaIntro)

- ```git clone https://github.com/ID-Start-Winter22/einfacherChatbot.git```
- ```cd einfacherChatbot```
- ```conda activate rasaenv```
- ```rasa train```
- ```rasa run --cors "*"```

in einem zweiten Terminal:
- ```python -m http.server```

im Browser http://localhost:8000/
