const createHelloWorld= () => (...args: any[])=>"Hello World";
    
const f = createHelloWorld();
console.log(f());
