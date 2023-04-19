// ********************* Exemplo entender execução das coisas
function semAsync() {
    console.log("1-Iniciando chamada assíncrona...");
    setTimeout(() => {
      console.log("1-Chamada assíncrona concluída!");
    }, 2000);
    console.log("1-Continuando a execução do código...");
  }
  
  async function comAsync() {
    console.log("2-Iniciando chamada assíncrona...");
    await new Promise(resolve => setTimeout(() => { //forma diferente de determinar o resolve
      console.log("2-Chamada assíncrona concluída!");
      resolve();
    }, 2000));
    console.log("2-Continuando a execução do código...");
  }
  
  semAsync()
  comAsync()

// ********************* Exemplo de try e catch com assync e promisses *********************
async function f1() {
    return 1;
  }
  
  function f2() {
    return Promise.resolve(1);
  }
  
  function f3() {
    return Promise.reject(1);
  }
  
  async function teste() {
    try {
      const r1 = await f1();
      console.log(r1);
      const r2 = await f2();
      console.log(r2);
      const r3 = await f3();
      console.log(r3);
    } catch (e) {
      console.log('e');
    }
  }
  
  teste();
  