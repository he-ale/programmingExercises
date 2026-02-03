type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let num= init;
    const counter: Counter={
        increment: ()=> {
            num=num+1
            return num
        },
        decrement: ()=> {
            num= num-1
            return num
        },
        reset: ()=>{
            num=init
            return num
        }
    }
    return counter;
};