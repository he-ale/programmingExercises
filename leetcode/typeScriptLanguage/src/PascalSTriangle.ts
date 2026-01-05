function generate(numRows: number): number[][] {
    let triangle: number[][]= [[1]];
    if(numRows===1){
        return triangle;
    }
    triangle= [...triangle,[1,1]]
    if(numRows===2){
        return triangle;
    }
    for (let index = 2; index < numRows; index++) {
        let row: number[]= [1];
        for(let i= 1; i<triangle[index-1]!.length; i++){
            row= [...row, (triangle[index-1]![i]!+triangle[index-1]![i-1]!)];
        }
        row= [...row, 1];
        triangle=[...triangle, row]
    }
    return triangle
};

console.log(generate(1));
console.log(generate(5));
