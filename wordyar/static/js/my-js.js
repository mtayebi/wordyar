var answer = ""

function loadQuestion(){
    
    document.getElementById("answer-1").checked = false
    document.getElementById("answer-2").checked = false
    document.getElementById("answer-3").checked = false
    document.getElementById("answer-4").checked = false

    clearAnswer()

    let request = new XMLHttpRequest()
    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){

            // if number of questions finished hide next button
            if (!(JSON.parse(this.response)['continue'])){
                document.getElementById("next").hidden = true 
                document.getElementById("question").innerHTML = "پایان آزمون"
                document.getElementById("answer-1").innerHTML = ""
                document.getElementById("answer-2").innerHTML = ""
                document.getElementById("answer3").innerHTML = ""
                document.getElementById("answer4").innerHTML = ""
            }


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

    const data = {}
    data['question'] = document.getElementById("question").innerHTML
    data['answer'] = answer
    var response_data = JSON.stringify(data)

    url = "http://127.0.0.1:8000/exams/api?data="+response_data

    request.open("GET", url)
    request.send()
}

// get answer clicked in page and save as answer variable
function saveAnswer(ans){
    answer = document.getElementById(ans).innerHTML
    console.log(answer)
}


function clearAnswer(){
    answer = ""
    console.log("cleared")
}