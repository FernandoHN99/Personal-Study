function getUser() {
    return new Promise((resolve, reject) => { //Aqui a promisse é criada com status pending
      // console.log("DEU CERTO"); //Síncrono
      const user = { name: "John", age: 30 };
      resolve(user);
    });
  }

getUser().then(res => console.log(res))