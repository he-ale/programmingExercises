type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    const res: ToBeOrNotToBe={
        toBe:(val2: any)=>{
            if(val2!==val){
                throw new Error("Not Equal");
            }
            return true;
            
        },
        notToBe:(val2: any)=>{
            if(val2===val){
                throw new Error("Equal");
            }
            return true
        }
    } 
    return res;
};

console.log(expect(5).toBe(5));