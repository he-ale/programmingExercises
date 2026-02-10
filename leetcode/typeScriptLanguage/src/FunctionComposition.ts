type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        let value= x
        
        for (let fun of functions.reverse()) {
            value=fun(value);
        }
        return value;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */