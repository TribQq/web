anonF = (x) => {
   return String(x).replace(/ /gi, '').replace(/\n/, '').length
   }


res = anonF('\n ')
console.log(res)

