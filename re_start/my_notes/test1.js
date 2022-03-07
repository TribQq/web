anonF = (x) => {
   if (x===5) return 'x==5'
   else if(x<5) return 'x<5'
   else return 'x>5'
   }

res = anonF(5)
console.log(res)
res = anonF(4)
console.log(res)
res = anonF(10)
console.log(res)