console.log("Hello")

fetch("https://raw.githubusercontent.com/Laboratoria/LIM011-data-lovers/master/src/data/potter/potter.json")
.then(x => x.json())
.then(y => megjelenit(y));


function megjelenit(tomb){
    console.log(tomb)
    let sz=""
    for (let elem of tomb) {
        sz+='<option value="">'+elem.name+'</option>'
    }
    document.getElementById("lenyilo").innerHTML=sz

    let sz2=""
    for (let elem of tomb) {
        sz2+='<tr>'
        sz2+='<td>'
        sz2+=elem.name
        sz2+='</td>'
        sz2+='<td>'
        sz2+=elem.gender
        sz2+='</td>'
        sz2+='<td>'
        sz2+=elem.house
        sz2+='</td>'
        sz2+='<td>'
        sz2+=elem.actor
        sz2+='</td>'
        sz2+='</tr>'
      
    }
    document.getElementById("torzs").innerHTML=sz2


}
