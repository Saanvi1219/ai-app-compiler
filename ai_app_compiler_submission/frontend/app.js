const promptInput=document.getElementById("promptInput");

const output=document.getElementById("output");

const generateBtn=document.getElementById("generateBtn");

const evaluateBtn=document.getElementById("evaluateBtn");

const confidenceBar=document.getElementById("confidenceBar");

const chaosBar=document.getElementById("chaosBar");

const themeToggle=document.getElementById("themeToggle");



let latestData=null;



async function generateArchitecture(){

generateBtn.innerText="Compiling...";

output.innerText=
"Running Compiler Pipeline...\n";

try{

const response=await fetch(
"https://ai-app-compiler-1-6q6t.onrender.com/generate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

prompt:promptInput.value

})

}

);


const data=await response.json();

console.log("BACKEND RESPONSE:",data);

if(
!data ||
typeof data !== "object"
){

throw new Error(
"Backend returned invalid data"
);

}

latestData=data;

showData(
data || {}
);

updateMeters(
data || {}
);


generateBtn.innerText=
"Generate Architecture";


}
catch(error){

generateBtn.innerText=
"Generate Architecture";

console.log(error);

output.innerText=
"Error:\n\n"+
(
error.message ||
JSON.stringify(error)
);

}

}






function showData(data){

let display={

pipeline:
data.pipeline || [],

app:
data.app || {},

validation:
data.validation || {},

repair_log:
data.repair_log || [],

runtime:
data.runtime || {},

insight:
data.insight || {},

metrics:
data.metrics || {}

};


output.innerText=
JSON.stringify(
display,
null,
2
);

document.getElementById(
"intentText"
).innerText=

data.app?.name
||
"Waiting";


document.getElementById(
"intentConfidence"
).innerText=

"Confidence: "+
(
data.insight?.confidence
||
0
)
+"%";


document.getElementById(
"runtimePages"
).innerText=

"Pages: "+
(
data.runtime?.pages
||
0
);


document.getElementById(
"runtimeApis"
).innerText=

"APIs: "+
(
data.runtime?.apis
||
0
);


document.getElementById(
"repairCount"
).innerText=

"Fixes: "+
(
data.metrics?.repair_count
||
0
);


document.getElementById(
"retryCount"
).innerText=

"Retries: "+
(
data.metrics?.retries
||
0
);

document.getElementById(
"compileStatus"
).innerText=

data.metrics?.success

?

"Architecture Generated"

:

"Compilation Failed";


document.getElementById(
"riskLevel"
).innerText=

data.app?.risk
||
"Standard";


document.getElementById(
"confidenceLive"
).innerText=

(
data.insight?.confidence
||
0
)
+"%";


document.getElementById(
"executionMode"
).innerText=

data.adaptive_execution
?.selected_strategy

||

"Fast Mode";



if(
data.insight
){

updateMeters(data);

}

}








function updateMeters(data){

let confidence=
data.insight?.confidence ?? 0;

let chaos=
data.insight?.chaos ?? 0;


confidenceBar.style.width=
confidence+"%";


chaosBar.style.width=
chaos+"%";

}




async function runEvaluation(){

evaluateBtn.innerText=
"Evaluating...";


output.innerText=
"Running evaluation dataset...\n";


try{


const response=
await fetch(
"https://ai-app-compiler-1-6q6t.onrender.com/evaluate",
);


const data=
await response.json();


output.innerText=
JSON.stringify(
data,
null,
2
);


evaluateBtn.innerText=
"Run Evaluation";

}

catch(error){

evaluateBtn.innerText=
"Run Evaluation";

console.log(error);

output.innerText=
"Error:\n\n"+
(
error.message ||
JSON.stringify(error)
);

}


}




generateBtn.addEventListener(

"click",

generateArchitecture

);



evaluateBtn.addEventListener(

"click",

runEvaluation

);




themeToggle.addEventListener(

"click",

()=>{


document.body.classList.toggle(
"light"
);


if(
document.body.classList.contains(
"light"
)
){

themeToggle.innerText=
"Day Mode";

}

else{

themeToggle.innerText=
"Night Mode";

}


}

);





document.querySelectorAll(
".idea-grid button"
)

.forEach(button=>{


button.addEventListener(

"click",

()=>{


let text=
button.innerText;


if(
text==="Social Impact"
){

promptInput.value=
"Build a child rescue service platform with login, missing child reporting, facial recognition matching, dashboard, role based access, emergency alerts, geo intelligence and NGO workflows.";

}


else if(
text==="Fintech"
){

promptInput.value=
"Build a portfolio risk platform with dashboards, analytics, login, admin permissions and alerts.";

}


else if(
text==="Healthcare"
){

promptInput.value=
"Build a healthcare triage platform with patients, doctors, admin workflows and reports.";

}


else{


promptInput.value=
"Build a disaster response platform with geo alerts, rescue teams and authority approval systems.";

}


window.scrollTo({

top:
document.querySelector(
"#studio"
)
.offsetTop-100,

behavior:
"smooth"

});


}

);


});






document.querySelectorAll(
".pipeline-grid div"
)

.forEach(

(card,index)=>{


card.addEventListener(

"mouseenter",

()=>{


card.animate(

[

{

transform:
"translateY(0px)"

},

{

transform:
"translateY(-12px)"

}

],

{

duration:300,

fill:"forwards"

}

);


}

);


card.addEventListener(

"mouseleave",

()=>{


card.animate(

[

{

transform:
"translateY(-12px)"

},

{

transform:
"translateY(0px)"

}

],

{

duration:300,

fill:"forwards"

}

);


}

);


}

);





window.addEventListener(

"scroll",

()=>{


const cards=
document.querySelectorAll(
".floating-card"
);


cards.forEach(

(card,index)=>{


const offset=
window.scrollY*.02*(index+1);


card.style.transform=
`translateY(${offset}px)`;


}

);


}

);





generateArchitecture();