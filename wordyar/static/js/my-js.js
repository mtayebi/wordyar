function loadQuestion(){
    let request = new XMLHttpRequest()
    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){

            // get json responce from backend and parse it 
            const answers = JSON.parse(this.response)['answers']

            // put question and answers in their position in html page
            document.getElementById("question").innerHTML = JSON.parse(this.response)['question']
            document.getElementById("answer1").innerHTML = answers[0]
            document.getElementById("answer2").innerHTML = answers[1]
            document.getElementById("answer3").innerHTML = answers[2]
            document.getElementById("answer4").innerHTML = answers[3]

        }

    }
    const answers = {}
    for (let i=1; i<5; i++){
       answers[i] = document.getElementById("answer"+i).innerHTML

    }
    var data = JSON.stringify(answers)
    url = "http://127.0.0.1:8000/exams/api?data="+data
    request.open("GET", url)
    request.send()
}
