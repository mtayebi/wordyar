# wordyar

## wordyar is a simple web application for **online test exams**

### this project was originally writen to help in Learning vocabulary beacause of this, it's name is wordyar 

## features

- the question data base contains simply question and answer for each, this table dont have any other restriction that it will help to creat various independent exams
-  all users can see the webpage but only registered users can take exams
-  each question has only one answer
-  false answers will cause decreasing the final score so it is rational to dont answer an question
-  i try to simulate real world exams but of course any program has some shortages, im open to recive messages from you or you can improve that yourself it is opensource but dont forget to give star
-  real isue that i can point to is frontend designing i know this, im not really good in front it is not my main field. 

## how future can be for this project

- **improve frontend**
- fix probably bugs
- add new features
- and use costomer ideas 

## technical view

- > the project contains three main apps (core, exams, accounts), this help to use this project as a ***micro service*** project.
- > exam pages use ***json*** and ***ajax*** to comunicate with view part this speed up loading the pages and make better feel for user. and bring ***RESTAPI*** architecture in our service
- > thanks to ***Django authentication system*** featues not registered users can not see exams and participate in them. this help us contorol users authentication  
- > the ***ERD*** of project tries to be written flexible, so it is open to changing Application in various kind of exams.

## how to use?

- clone the project as below:
```
git clone https://github.com/mtayebi/wordyar.git
```
- go to wordyar directory
```
cd wordyar
```
- run cmmand below
```
python3 manage.py runserver
```

- > **_NOTE:_** you should have installed django in your running system.
- > **_NOTE:_** database of questions need to be peresented you can create one by
  ``` python3 mange.py createsuperuser ``` or you can connect your own by changing database settings
  

