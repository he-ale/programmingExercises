type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache : Map<string, number> = new Map();
    let callCount = 0;

    return function (...args) {
        if (args.length == 0) {
            return callCount;
        } else if (cache.has(`${args}`)) {
            return cache.get(`${args}`);
        } else {
            callCount++;
            const res= fn(...args);
            cache.set(`${args}`, res);
            return res;
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
