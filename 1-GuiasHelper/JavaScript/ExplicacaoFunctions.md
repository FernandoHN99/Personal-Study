O JavaScript possui várias funções embutidas que são amplamente usadas no dia a dia do desenvolvimento. Aqui estão algumas das principais categorias e funções mais importantes:  

---

## **1️⃣ Manipulação de Arrays**
Essas funções ajudam a iterar, transformar e manipular arrays.  

🔹 **`map()`** → Cria um novo array aplicando uma função a cada elemento.  
```js
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8]
```

🔹 **`filter()`** → Retorna um novo array apenas com os elementos que passam em uma condição.  
```js
const numbers = [1, 2, 3, 4, 5];
const even = numbers.filter(num => num % 2 === 0);
console.log(even); // [2, 4]
```

🔹 **`reduce()`** → Reduz um array a um único valor.  
```js
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // 10
```

🔹 **`find()`** → Retorna o primeiro elemento que satisfaz a condição.  
```js
const users = [{ name: 'Alice' }, { name: 'Bob' }];
const user = users.find(user => user.name === 'Bob');
console.log(user); // { name: 'Bob' }
```

🔹 **`some()`** → Retorna `true` se pelo menos um elemento satisfaz a condição.  
```js
const numbers = [1, 2, 3, 4];
const hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven); // true
```

🔹 **`every()`** → Retorna `true` se todos os elementos satisfazem a condição.  
```js
const numbers = [2, 4, 6];
const allEven = numbers.every(num => num % 2 === 0);
console.log(allEven); // true
```

---

## **2️⃣ Manipulação de Strings**
Essas funções ajudam a modificar e analisar strings.  

🔹 **`toUpperCase()` / `toLowerCase()`** → Converte para maiúsculas/minúsculas.  
```js
console.log('hello'.toUpperCase()); // 'HELLO'
console.log('WORLD'.toLowerCase()); // 'world'
```

🔹 **`trim()`** → Remove espaços em branco do início e do fim.  
```js
console.log('  hello  '.trim()); // 'hello'
```

🔹 **`split()`** → Divide uma string em um array.  
```js
console.log('apple,banana,grape'.split(',')); // ['apple', 'banana', 'grape']
```

🔹 **`replace()`** → Substitui parte da string.  
```js
console.log('I like cats'.replace('cats', 'dogs')); // 'I like dogs'
```

🔹 **`includes()`** → Verifica se uma string contém um valor específico.  
```js
console.log('Hello World'.includes('World')); // true
```

---

## **3️⃣ Manipulação de Objetos**
Objetos são fundamentais no JavaScript. Algumas funções úteis incluem:  

🔹 **`Object.keys()`** → Retorna um array com as chaves do objeto.  
```js
const user = { name: 'Alice', age: 25 };
console.log(Object.keys(user)); // ['name', 'age']
```

🔹 **`Object.values()`** → Retorna um array com os valores do objeto.  
```js
console.log(Object.values(user)); // ['Alice', 25]
```

🔹 **`Object.entries()`** → Retorna um array de pares `[chave, valor]`.  
```js
console.log(Object.entries(user)); // [['name', 'Alice'], ['age', 25]]
```

🔹 **`Object.assign()`** → Copia propriedades de um ou mais objetos para um objeto alvo.  
```js
const obj1 = { a: 1 };
const obj2 = { b: 2 };
const merged = Object.assign({}, obj1, obj2);
console.log(merged); // { a: 1, b: 2 }
```

---

## **4️⃣ Manipulação de Datas (`Date`)**
O JavaScript possui o objeto `Date` para lidar com datas e horários.  

🔹 **Criar uma data atual:**  
```js
const now = new Date();
console.log(now);
```

🔹 **Obter partes da data:**  
```js
console.log(now.getFullYear()); // Ano
console.log(now.getMonth()); // Mês (0-11)
console.log(now.getDate()); // Dia do mês
console.log(now.getDay()); // Dia da semana (0 = Domingo)
```

🔹 **Converter para string formatada:**  
```js
console.log(now.toISOString()); // '2025-02-02T12:00:00.000Z'
```

---

## **5️⃣ Manipulação de Números (`Math`)**
O objeto `Math` contém funções matemáticas úteis.  

🔹 **Arredondamento:**  
```js
console.log(Math.round(4.7)); // 5
console.log(Math.floor(4.7)); // 4
console.log(Math.ceil(4.2)); // 5
```

🔹 **Número aleatório entre 0 e 1:**  
```js
console.log(Math.random()); // Ex: 0.8475928374
```

🔹 **Máximo e mínimo:**  
```js
console.log(Math.max(10, 20, 30)); // 30
console.log(Math.min(10, 20, 30)); // 10
```

🔹 **Potência e raiz quadrada:**  
```js
console.log(Math.pow(2, 3)); // 8 (2³)
console.log(Math.sqrt(16)); // 4 (raiz quadrada)
```

---

## **6️⃣ Temporizadores (`setTimeout` e `setInterval`)**
Funções para agendar execução de código.  

🔹 **`setTimeout()`** → Executa código após um tempo.  
```js
setTimeout(() => {
  console.log('Executado após 2 segundos');
}, 2000);
```

🔹 **`setInterval()`** → Executa código repetidamente a cada intervalo.  
```js
setInterval(() => {
  console.log('Executado a cada 3 segundos');
}, 3000);
```

---

## **7️⃣ Trabalhando com Promises e Async/Await**
Para lidar com operações assíncronas, usamos Promises e `async/await`.  

🔹 **Exemplo de `Promise`**  
```js
const fetchData = () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve('Dados carregados'), 2000);
  });
};

fetchData().then((data) => console.log(data)); // 'Dados carregados' após 2s
```

🔹 **Exemplo de `async/await`**  
```js
const fetchData = async () => {
  const data = await new Promise((resolve) => {
    setTimeout(() => resolve('Dados carregados'), 2000);
  });
  console.log(data);
};

fetchData();
```

---

## **🔹 Conclusão**
Essas são algumas das funções mais importantes do JavaScript! Elas são essenciais para manipular arrays, strings, objetos, números, datas e lidar com operações assíncronas.

Se quiser mais detalhes sobre alguma delas, me avise! 🚀😃