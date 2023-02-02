let something = prompt("Name: ")
let run = true
while (run) {
    if (something == "") {
        something = prompt(`Please enter your name \nName: `)
    } else {
        run = false
    }
}
alert(`Hello ${something}!`)
