function solution(str) {
    str = str.split(" ")
    const s = str[0]
    const t = str[1]

    let answer = [];
    let p = 1000;

    for (let x of s) {
        if (x=== t){
            p = 0;
            answer.push(p);
        } else {
            p ++;
            answer.push(p);
        }
    }
    p =1000;

    for(let i = s.length-1; i >=0; i--){
        if(s[i]===t){
            p = 0
        } else {
            p ++;
            answer[i] = Math.min(answer[i], p) 
        }
    }

    return answer

}

 
const test = "teachermode e"
console.log(solution(test))