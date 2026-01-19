
const sumDigits= (num:number):number=>{
    let sum=0;
    while(num>0){
        sum= sum + (num%10);
        num = Math.trunc(num/10);
    }
    return sum;
}

function addDigits(num: number): number {
    let res= num;
    while(res>=10){
        res= sumDigits(res);
    }

    return res;
};

console.log(addDigits(38));
console.log(addDigits(10));

